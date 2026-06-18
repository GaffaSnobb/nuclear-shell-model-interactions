#!/usr/bin/env python3
"""Generate an ASCII orbital-space diagram from a KSHELL .snt file."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


L_LETTERS = {
    0: "s",
    1: "p",
    2: "d",
    3: "f",
    4: "g",
    5: "h",
    6: "i",
    7: "j",
}

# KSHELL .snt files list the inert-core particle numbers, not all orbitals in
# that core. This table names filled shells between common closures,
# approximately top-to-bottom within each closure gap.
CORE_SHELLS = {
    2: ["0s1/2"],
    8: ["0p1/2", "0p3/2"],
    20: ["0d3/2", "1s1/2", "0d5/2"],
    28: ["0f7/2"],
    50: ["0g9/2", "1p1/2", "1p3/2", "0f5/2"],
    82: ["0h11/2", "2s1/2", "1d3/2", "1d5/2", "0g7/2"],
    126: ["0i13/2", "2p1/2", "2p3/2", "1f5/2", "1f7/2", "0h9/2"],
}

SHELL_CLOSURES = sorted(CORE_SHELLS)
LETTER_TO_L = {letter: l for l, letter in L_LETTERS.items()}
ORBIT_RE = re.compile(r"^(?P<n>\d+)(?P<letter>[a-z])(?P<two_j>\d+)/2$")


def orbit_label(n: int, l: int, two_j: int) -> str:
    letter = L_LETTERS.get(l, f"l{l}")
    return f"{n}{letter}{two_j}/2"


def capacity_from_two_j(two_j: int) -> int:
    return two_j + 1


def capacity_from_label(label: str) -> int | None:
    match = ORBIT_RE.match(label)
    if not match:
        return None
    return int(match.group("two_j")) + 1


def major_shell_label(major_n: int) -> str:
    first_l = major_n % 2
    return "".join(L_LETTERS[l] for l in range(first_l, major_n + 1, 2))


def orbital_major_shell(n: int, l: int) -> tuple[int, str]:
    major_n = 2 * n + l
    return major_n, major_shell_label(major_n)


def orbital_major_shell_from_label(label: str) -> tuple[int, str]:
    match = ORBIT_RE.match(label)
    if not match:
        return -1, "?"
    n = int(match.group("n"))
    l = LETTER_TO_L[match.group("letter")]
    return orbital_major_shell(n, l)


def inert_core_orbitals(closure: int) -> list[dict[str, object]]:
    orbitals = []
    for shell_closure in reversed([item for item in SHELL_CLOSURES if item <= closure]):
        for label in CORE_SHELLS[shell_closure]:
            major_n, major_label = orbital_major_shell_from_label(label)
            orbitals.append(
                {
                    "label": label,
                    "capacity": capacity_from_label(label),
                    "major_n": major_n,
                    "major_label": major_label,
                }
            )
    return orbitals


def read_snt(path: Path) -> tuple[dict[str, int], dict[str, list[dict[str, object]]]]:
    rows = []
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        body = raw.split("!", 1)[0].strip()
        if body:
            rows.append(body.split())

    if not rows:
        raise ValueError(f"No data rows found in {path}")

    n_proton_orbits, n_neutron_orbits, core_z, core_n = map(int, rows[0][:4])
    n_orbits = n_proton_orbits + n_neutron_orbits
    orbit_rows = rows[1 : 1 + n_orbits]

    one_body_header_idx = 1 + n_orbits
    n_one_body = int(rows[one_body_header_idx][0])
    one_body_rows = rows[one_body_header_idx + 1 : one_body_header_idx + 1 + n_one_body]

    single_particle_energies = {}
    for row in one_body_rows:
        i, j, value = int(row[0]), int(row[1]), float(row[2])
        if i == j:
            single_particle_energies[i] = value

    orbitals = {"protons": [], "neutrons": []}
    for row in orbit_rows:
        idx, n, l, two_j, tz = map(int, row[:5])
        major_n, major_label = orbital_major_shell(n, l)
        entry = {
            "label": orbit_label(n, l, two_j),
            "capacity": capacity_from_two_j(two_j),
            "major_n": major_n,
            "major_label": major_label,
            "spe": single_particle_energies.get(idx),
        }
        if tz == -1:
            orbitals["protons"].append(entry)
        elif tz == 1:
            orbitals["neutrons"].append(entry)
        else:
            raise ValueError(f"Unexpected tz={tz} for orbital index {idx}")

    for species in orbitals.values():
        species.sort(
            key=lambda item: (
                int(item["major_n"]),
                item["spe"] is not None,
                float(item["spe"]) if item["spe"] is not None else float("-inf"),
            ),
            reverse=True,
        )

    return {"z": core_z, "n": core_n}, orbitals


def format_model_space_row(entry: dict[str, object]) -> str:
    spe = entry.get("spe")
    spe_text = "" if spe is None else f"{float(spe):8.3f} MeV"
    return f"{str(entry['major_label']):<4} {entry['label']:<7} [{int(entry['capacity']):>2}] {spe_text:>12}"


def format_core_row(entry: dict[str, object]) -> str:
    capacity = entry.get("capacity")
    if capacity is None:
        return f"{str(entry['major_label']):<4} {entry['label']:<7}       inert core"
    return f"{str(entry['major_label']):<4} {entry['label']:<7} [{int(capacity):>2}]  inert core"


def pad_rows(rows: list[str], n_rows: int) -> list[str]:
    return rows + [""] * (n_rows - len(rows))


def render_ascii(name: str, snt_path: Path) -> str:
    core, orbitals = read_snt(snt_path)

    proton_model = [format_model_space_row(entry) for entry in orbitals["protons"]]
    neutron_model = [format_model_space_row(entry) for entry in orbitals["neutrons"]]
    proton_core = [format_core_row(entry) for entry in inert_core_orbitals(core["z"])]
    neutron_core = [format_core_row(entry) for entry in inert_core_orbitals(core["n"])]

    if not proton_core:
        proton_core = [f"Z={core['z']} core orbitals not listed in script"]
    if not neutron_core:
        neutron_core = [f"N={core['n']} core orbitals not listed in script"]

    width = 39
    model_rows = max(len(proton_model), len(neutron_model))
    core_rows = max(len(proton_core), len(neutron_core))
    proton_model = pad_rows(proton_model, model_rows)
    neutron_model = pad_rows(neutron_model, model_rows)
    proton_core = pad_rows(proton_core, core_rows)
    neutron_core = pad_rows(neutron_core, core_rows)

    lines = [
        f"{name} orbital space (KSHELL file convention)",
        f"Core: Z={core['z']}, N={core['n']}",
        "",
        f"{'proton orbitals':^{width}}    {'neutron orbitals':^{width}}",
        f"{'major  orbital             SPE':^{width}}    {'major  orbital             SPE':^{width}}",
        f"{'active model space':^{width}}    {'active model space':^{width}}",
        "",
    ]

    for left, right in zip(proton_model, neutron_model):
        lines.append(f"  {left:<{width}}  {right:<{width}}")

    lines.extend(
        [
            "",
            "  ------------------------- closed-shell boundary -------------------------",
            "",
        ]
    )

    for left, right in zip(proton_core, neutron_core):
        lines.append(f"  {left:<{width}}  {right:<{width}}")

    return "\n".join(line.rstrip() for line in lines).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snt_file", type=Path, help="Path to a KSHELL .snt file")
    parser.add_argument("--name", help="Interaction name to use in the diagram")
    args = parser.parse_args()

    name = args.name or args.snt_file.stem
    print(render_ascii(name, args.snt_file), end="")


if __name__ == "__main__":
    main()
