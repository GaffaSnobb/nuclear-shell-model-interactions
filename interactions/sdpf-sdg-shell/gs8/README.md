# gs8

`gs8` is a KSHELL-format interaction for the same large `sd-pf-sdg` valence space as `SDPFSDG-MU`, above a `16O` core. The raw `.snt` file is not included in this repository.

The local header says that `gs8.snt` was made from the SDPFSDG-MU file `GCLSTsdpfsdgix5pn.snt` with modified upper-shell single-particle energies. The active proton and neutron spaces are identical and contain the full `sd` shell, full `pf` shell, and the `sdg` orbitals `0g9/2`, `0g7/2`, `1d5/2`, `1d3/2`, and `2s1/2`.

## Orbital Space

```text
GS8 orbital space (KSHELL file convention)
Core: Z=8, N=8

            proton orbitals                           neutron orbitals
    major  orbital             SPE             major  orbital             SPE
          active model space                         active model space

  sdg  0g7/2   [ 8]   12.782 MeV           sdg  0g7/2   [ 8]   12.782 MeV
  sdg  0g9/2   [10]    9.419 MeV           sdg  0g9/2   [10]    9.419 MeV
  sdg  2s1/2   [ 2]    6.453 MeV           sdg  2s1/2   [ 2]    6.453 MeV
  sdg  1d3/2   [ 4]    5.402 MeV           sdg  1d3/2   [ 4]    5.402 MeV
  sdg  1d5/2   [ 6]    4.119 MeV           sdg  1d5/2   [ 6]    4.119 MeV
  pf   0f5/2   [ 6]   10.022 MeV           pf   0f5/2   [ 6]   10.022 MeV
  pf   0f7/2   [ 8]    5.063 MeV           pf   0f7/2   [ 8]    5.063 MeV
  pf   1p1/2   [ 2]    1.903 MeV           pf   1p1/2   [ 2]    1.903 MeV
  pf   1p3/2   [ 4]    1.184 MeV           pf   1p3/2   [ 4]    1.184 MeV
  sd   0d3/2   [ 4]    1.647 MeV           sd   0d3/2   [ 4]    1.647 MeV
  sd   1s1/2   [ 2]   -3.164 MeV           sd   1s1/2   [ 2]   -3.164 MeV
  sd   0d5/2   [ 6]   -3.948 MeV           sd   0d5/2   [ 6]   -3.948 MeV

  ------------------------- closed-shell boundary -------------------------

  p    0p1/2   [ 2]  inert core            p    0p1/2   [ 2]  inert core
  p    0p3/2   [ 4]  inert core            p    0p3/2   [ 4]  inert core
  s    0s1/2   [ 2]  inert core            s    0s1/2   [ 2]  inert core
```

## Provenance

The local KSHELL header says:

```text
2015/07/13
from GCLSTsdpfsdgix5pn.snt
```

and records the intended changes:

```text
8 0g9/2  -0.8MeV
9 0g7/2  -3.2MeV
10 1d5/2  -2.5MeV
11 1d3/2  -5.7MeV
12 2s1/2  -4.0MeV
```

The file keeps the same model-space source (`sdpfsdg_64.sps`) and interaction-source label (`GCLSTsdpfsdgix5pn.int`) as the parent SDPFSDG-MU local file. No paper title, DOI, author list, or public download URL is included in the header. The exact provenance of the local `gs8` file label is therefore not established here.

## Difference From SDPFSDG-MU

A direct comparison of `gs8.snt` with the SDPFSDG-MU file shows that the core, orbital definitions, TBME header, and all `18,170` TBME rows are identical. The difference is confined to the one-body single-particle energies of the five `sdg` orbitals, shifted by the amounts listed in the header for both protons and neutrons.

| Orbital | SDPFSDG-MU SPE | gs8 SPE | Shift |
| --- | ---: | ---: | ---: |
| `0g9/2` | 10.21930 MeV | 9.41930 MeV | -0.80000 MeV |
| `0g7/2` | 15.98180 MeV | 12.78180 MeV | -3.20000 MeV |
| `1d5/2` | 6.61930 MeV | 4.11930 MeV | -2.50000 MeV |
| `1d3/2` | 11.10250 MeV | 5.40250 MeV | -5.70000 MeV |
| `2s1/2` | 10.45290 MeV | 6.45290 MeV | -4.00000 MeV |

No explanatory note has been found beyond the header. The practical effect is to lower the `sdg` shell relative to the `sd` and `pf` shells, making cross-shell configurations involving `sdg` orbitals less costly.

## Notes

The raw KSHELL interaction file is not included in this repository.

Local source checksum:

```text
54dc201e2e4409c976f19625484df415f6806e24  gs8.snt
```

## Relevant Literature

- Y. Utsuno, T. Otsuka, B. A. Brown, M. Honma, T. Mizusaki, and N. Shimizu, "Shape transitions in exotic Si and S isotopes and tensor-force-driven Jahn-Teller effect," Phys. Rev. C 86, 051301(R) (2012). Origin/reference paper for the related SDPF-MU interaction in the `sd-pf` space. DOI: [10.1103/PhysRevC.86.051301](https://doi.org/10.1103/PhysRevC.86.051301)
- T. Otsuka, T. Suzuki, M. Honma, Y. Utsuno, N. Tsunoda, K. Tsukiyama, and M. Hjorth-Jensen, "Novel Features of Nuclear Forces and Shell Evolution in Exotic Nuclei," Phys. Rev. Lett. 104, 012501 (2010). Reference for the monopole-based universal interaction used in SDPF-MU-style developments. DOI: [10.1103/PhysRevLett.104.012501](https://doi.org/10.1103/PhysRevLett.104.012501)
- Y. Utsuno, T. Otsuka, T. Mizusaki, and M. Honma, "Varying shell gap and deformation in N ~ 20 unstable nuclei studied by the Monte Carlo shell model," Phys. Rev. C 60, 054315 (1999). Origin/reference paper for the older SDPF-M interaction. DOI: [10.1103/PhysRevC.60.054315](https://doi.org/10.1103/PhysRevC.60.054315)

## Files

No raw interaction file is included.

## Citation

For calculations using this exact local file, record the filename, local checksum, parent SDPFSDG-MU relation, and the fact that the raw interaction file is restricted. Until the exact file-label provenance is resolved, cite the relevant SDPFSDG-MU / VMU literature above rather than treating this README as an origin reference.
