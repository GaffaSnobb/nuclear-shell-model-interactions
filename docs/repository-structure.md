# Repository structure

Interactions are grouped primarily by the nuclear mass region or shell-model region they are used for. The inert core is recorded in each interaction's metadata instead of being the top-level grouping, because the core can be partly a bookkeeping convention.

The intended layout is:

```text
interactions/
  132sn-region/
    sn100pn/
      README.md
      metadata.yml
      files/
        kshell/
          sn100pn.snt
```

Only directories with actual content should be created. For example, if an interaction is only available in KSHELL format, create `files/kshell/` but do not create empty `nushellx/`, `oxbash/`, or `original/` directories.

Some interactions may be documented without embedding the raw interaction file when the file is restricted or not meant for public redistribution. In those cases, keep `README.md` and `metadata.yml`, omit `files/kshell/`, and state explicitly that the local `.snt` file is intentionally not included.

Each interaction entry should contain:

- `README.md`: human-readable description, orbital-space diagram, provenance, notes, caveats, relevant literature, and recommended citation.
- `metadata.yml`: structured facts such as region, core, valence space, source publication, DOI, and available file formats.
- `files/kshell/`: KSHELL `.snt` files.

Each interaction `README.md` should include an ASCII orbital-space diagram generated from the KSHELL file:

```text
python3 tools/render_orbital_ascii.py interactions/<region>/<interaction>/files/kshell/<interaction>.snt --name <NAME>
```

The `.snt` file provides the core particle numbers, model-space orbitals, and single-particle energies. The script labels oscillator-major-shell families such as `sd`, `pf`, and `sdg`, and expands the inert core from the core closure down to `0s1/2`.

A top-level `index.md` gives a short table of all documented interactions.
