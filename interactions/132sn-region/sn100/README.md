# sn100

`sn100` is a KSHELL-format interaction file using a `Z=50, N=50` core and symmetric proton and neutron valence spaces in the `50-82` shell.

The origin of the file is not yet resolved. KSHELL repository history indicates that Jørgen Midtbø uploaded `sn100.snt` about 9 years ago.

## Orbital Space

```text
SN100 orbital space (KSHELL file convention)
Core: Z=50, N=50

            proton orbitals                           neutron orbitals
    major  orbital             SPE             major  orbital             SPE
          active model space                         active model space

  pfh  0h11/2  [12]    3.000 MeV           pfh  0h11/2  [12]    3.000 MeV
  sdg  1d3/2   [ 4]    2.550 MeV           sdg  1d3/2   [ 4]    2.550 MeV
  sdg  2s1/2   [ 2]    2.450 MeV           sdg  2s1/2   [ 2]    2.450 MeV
  sdg  0g7/2   [ 8]    0.200 MeV           sdg  0g7/2   [ 8]    0.200 MeV
  sdg  1d5/2   [ 6]    0.000 MeV           sdg  1d5/2   [ 6]    0.000 MeV

  ------------------------- closed-shell boundary -------------------------

  sdg  0g9/2   [10]  inert core            sdg  0g9/2   [10]  inert core
  pf   1p1/2   [ 2]  inert core            pf   1p1/2   [ 2]  inert core
  pf   1p3/2   [ 4]  inert core            pf   1p3/2   [ 4]  inert core
  pf   0f5/2   [ 6]  inert core            pf   0f5/2   [ 6]  inert core
  pf   0f7/2   [ 8]  inert core            pf   0f7/2   [ 8]  inert core
  sd   0d3/2   [ 4]  inert core            sd   0d3/2   [ 4]  inert core
  sd   1s1/2   [ 2]  inert core            sd   1s1/2   [ 2]  inert core
  sd   0d5/2   [ 6]  inert core            sd   0d5/2   [ 6]  inert core
  p    0p1/2   [ 2]  inert core            p    0p1/2   [ 2]  inert core
  p    0p3/2   [ 4]  inert core            p    0p3/2   [ 4]  inert core
  s    0s1/2   [ 2]  inert core            s    0s1/2   [ 2]  inert core
```

## Provenance

The local KSHELL header says:

```text
../bin/nushell2snt.py sn100.sp sn100.int in proton-neutron formalism
```

The file has `862` TBME rows and symmetric proton/neutron one-body energies.

Current provenance lead:

- KSHELL repository history indicates that Jørgen Midtbø uploaded `sn100.snt` about 9 years ago.

## Notes

This file is not currently identified with `SN100PN`, `CW4082`, `CW5082`, `KH4082`, or `KH5082`.

Compared with `sn100pn.snt`, this file has symmetric proton and neutron SPEs and does not cite Brown et al. 2005 in the header. It should therefore be documented as a separate interaction until its origin is resolved.

Local checksum:

```text
c778111553ec3e244dd881df04c83f219318486b  sn100.snt
```

## Relevant Literature

No definitive source paper has been identified yet.

Potentially related context under investigation:

- W.-T. Chou and E. K. Warburton, "Construction of shell-model interactions for Z=50, N=82 nuclei: Predictions for A=133-134 beta decays," Phys. Rev. C 45, 1720 (1992). DOI: [10.1103/PhysRevC.45.1720](https://doi.org/10.1103/PhysRevC.45.1720)
- B. A. Brown, N. J. Stone, J. R. Stone, I. S. Towner, and M. Hjorth-Jensen, "Magnetic moments of the 2+1 states around 132Sn," Phys. Rev. C 71, 044317 (2005). DOI: [10.1103/PhysRevC.71.044317](https://doi.org/10.1103/PhysRevC.71.044317)

## Files

- [files/kshell/sn100.snt](files/kshell/sn100.snt)

## Citation

Do not cite this entry as the origin of the interaction. Until the provenance is resolved, cite the local KSHELL file explicitly and record the checksum above.
