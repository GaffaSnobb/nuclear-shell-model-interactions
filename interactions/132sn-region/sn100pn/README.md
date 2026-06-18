# sn100pn

`sn100pn` is a shell-model interaction for the 132Sn region on the `N <= 82` side. The KSHELL file uses a `Z=50, N=50` core convention, so nuclei are represented with proton and neutron particles in the 50-82 shell.

For example, `133Xe` can be represented as 4 valence protons and 29 valence neutrons outside a `100Sn`-like core. This avoids explicit hole bookkeeping, although the source paper often discusses the same physics using a 132Sn closed-shell reference and neutron holes.

## Model Space

Core in the KSHELL file:

```text
Z = 50, N = 50
```

Proton orbitals:

```text
0g7/2, 1d5/2, 1d3/2, 2s1/2, 0h11/2
```

Neutron orbitals:

```text
0g7/2, 1d5/2, 1d3/2, 2s1/2, 0h11/2
```

## Orbital Space

```text
SN100PN orbital space (KSHELL file convention)
Core: Z=50, N=50

            proton orbitals                           neutron orbitals
    major  orbital             SPE             major  orbital             SPE
          active model space                         active model space

  pfh  0h11/2  [12]    3.605 MeV           pfh  0h11/2  [12]   -8.815 MeV
  sdg  1d3/2   [ 4]    3.316 MeV           sdg  2s1/2   [ 2]   -8.694 MeV
  sdg  2s1/2   [ 2]    3.224 MeV           sdg  1d3/2   [ 4]   -8.717 MeV
  sdg  1d5/2   [ 6]    1.562 MeV           sdg  1d5/2   [ 6]  -10.289 MeV
  sdg  0g7/2   [ 8]    0.807 MeV           sdg  0g7/2   [ 8]  -10.609 MeV

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

The local KSHELL file header says that `SN100PN` comes from `nushell@msu`, is based on `sn132g.int`, and is the interaction used in Brown et al., Phys. Rev. C 71, 044317 (2005).

The literal name `sn100pn` appears to be a NuShell/OXBASH/NuShellX interaction-library identifier rather than a name introduced in the paper itself.

## Notes

Brown et al. discuss `N <= 82` systems using a 132Sn closed-shell reference with neutron holes. The KSHELL file instead uses a `Z=50, N=50` core and places both proton and neutron particles in the 50-82 shell.

For `133Xe`, this means:

```text
Z = 54 -> 4 valence protons
N = 79 -> 29 valence neutrons
```

This is equivalent to the paper's `4 proton particles + 3 neutron holes` description, but the file itself uses particle-on-top bookkeeping.

The interaction physics is attributed to Brown et al. (2005). The exact `sn100pn` name appears to come from the NuShell@MSU interaction library, but a public source identifying who coined the file name has not yet been found.

## Relevant Literature

- B. A. Brown, N. J. Stone, J. R. Stone, I. S. Towner, and M. Hjorth-Jensen, "Magnetic moments of the 2+1 states around 132Sn," Phys. Rev. C 71, 044317 (2005). Source paper for the CD-Bonn-based 132Sn-region interaction. DOI: [10.1103/PhysRevC.71.044317](https://doi.org/10.1103/PhysRevC.71.044317)
- S. Das and M. Saha Sarkar, "Cross-shell excitations in doubly magic 132Sn and its nearest neighbours," Nucl. Phys. A 999, 122262 (2021). Constructs a cross-shell interaction from the widely used `sn100pn` and `CWG` interactions. DOI: [10.1016/j.nuclphysa.2021.122262](https://doi.org/10.1016/j.nuclphysa.2021.122262); arXiv: [2005.09411](https://arxiv.org/abs/2005.09411)
- B. Bhoy and P. C. Srivastava, "Systematic shell model study for N=82 and N=126 isotones and nuclear isomers," J. Phys. G: Nucl. Part. Phys. (2022). Uses `SN100PN` for systematic N=82 isotone calculations and summarizes the interaction components and SPEs. DOI: [10.1088/1361-6471/ac76da](https://doi.org/10.1088/1361-6471/ac76da); arXiv: [2205.11451](https://arxiv.org/abs/2205.11451)

## Files

- [files/kshell/sn100pn.snt](files/kshell/sn100pn.snt)

## Citation

B. A. Brown, N. J. Stone, J. R. Stone, I. S. Towner, and M. Hjorth-Jensen, "Magnetic moments of the 2+1 states around 132Sn," Phys. Rev. C 71, 044317 (2005). DOI: [10.1103/PhysRevC.71.044317](https://doi.org/10.1103/PhysRevC.71.044317)
