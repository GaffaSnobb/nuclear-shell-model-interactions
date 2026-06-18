# cwg2

`cwg2` is a KSHELL interaction file for the 132Sn region on the `N >= 82` side. It uses a `Z=50, N=82` core, with proton particles above `Z=50` and neutron particles above `N=82`.

This makes it a sibling interaction to `sn100pn` in the same mass region, but it is not the appropriate bookkeeping for neutron-hole nuclei such as `133Xe`.

## Model Space

Core in the KSHELL file:

```text
Z = 50, N = 82
```

Proton orbitals:

```text
0g7/2, 1d5/2, 1d3/2, 2s1/2, 0h11/2
```

Neutron orbitals:

```text
0h9/2, 1f7/2, 1f5/2, 2p3/2, 2p1/2, 0i13/2
```

## Orbital Space

```text
CWG2 orbital space (KSHELL file convention)
Core: Z=50, N=82

            proton orbitals                           neutron orbitals
    major  orbital             SPE             major  orbital             SPE
          active model space                         active model space

  pfh  0h11/2  [12]   -6.870 MeV           sdgi 0i13/2  [14]    0.250 MeV
  sdg  1d3/2   [ 4]   -6.995 MeV           pfh  1f5/2   [ 6]   -0.450 MeV
  sdg  2s1/2   [ 2]   -7.323 MeV           pfh  2p1/2   [ 2]   -0.799 MeV
  sdg  1d5/2   [ 6]   -8.701 MeV           pfh  0h9/2   [10]   -0.894 MeV
  sdg  0g7/2   [ 8]   -9.663 MeV           pfh  2p3/2   [ 4]   -1.601 MeV
                                           pfh  1f7/2   [ 8]   -2.455 MeV

  ------------------------- closed-shell boundary -------------------------

  sdg  0g9/2   [10]  inert core            pfh  0h11/2  [12]  inert core
  pf   1p1/2   [ 2]  inert core            sdg  2s1/2   [ 2]  inert core
  pf   1p3/2   [ 4]  inert core            sdg  1d3/2   [ 4]  inert core
  pf   0f5/2   [ 6]  inert core            sdg  1d5/2   [ 6]  inert core
  pf   0f7/2   [ 8]  inert core            sdg  0g7/2   [ 8]  inert core
  sd   0d3/2   [ 4]  inert core            sdg  0g9/2   [10]  inert core
  sd   1s1/2   [ 2]  inert core            pf   1p1/2   [ 2]  inert core
  sd   0d5/2   [ 6]  inert core            pf   1p3/2   [ 4]  inert core
  p    0p1/2   [ 2]  inert core            pf   0f5/2   [ 6]  inert core
  p    0p3/2   [ 4]  inert core            pf   0f7/2   [ 8]  inert core
  s    0s1/2   [ 2]  inert core            sd   0d3/2   [ 4]  inert core
                                           sd   1s1/2   [ 2]  inert core
                                           sd   0d5/2   [ 6]  inert core
                                           p    0p1/2   [ 2]  inert core
                                           p    0p3/2   [ 4]  inert core
                                           s    0s1/2   [ 2]  inert core
```

## Provenance

The local KSHELL file header identifies the interaction as `cwg.int`, says it is the interaction used in Brown et al., Phys. Rev. C 71, 044317 (2005), and notes that the single-particle energies were modified to reproduce later mass and spectra data.

## Relevant Literature

- B. A. Brown, N. J. Stone, J. R. Stone, I. S. Towner, and M. Hjorth-Jensen, "Magnetic moments of the 2+1 states around 132Sn," Phys. Rev. C 71, 044317 (2005). Source paper cited by the local KSHELL `cwg2.snt` header. DOI: [10.1103/PhysRevC.71.044317](https://doi.org/10.1103/PhysRevC.71.044317)
- S. Sarkar and M. Saha Sarkar, "Structure of A=138 isobars above the 132Sn core and the N-N interaction in the neutron-rich environment," Phys. Rev. C 78, 024308 (2008). Discusses calculations with the realistic `CWG` interaction and compares it with related 132Sn-region interactions. DOI: [10.1103/PhysRevC.78.024308](https://doi.org/10.1103/PhysRevC.78.024308); arXiv: [0802.3740](https://arxiv.org/abs/0802.3740)
- S. Das and M. Saha Sarkar, "Cross-shell excitations in doubly magic 132Sn and its nearest neighbours," Nucl. Phys. A 999, 122262 (2021). Constructs a cross-shell interaction from the widely used `sn100pn` and `CWG` interactions. DOI: [10.1016/j.nuclphysa.2021.122262](https://doi.org/10.1016/j.nuclphysa.2021.122262); arXiv: [2005.09411](https://arxiv.org/abs/2005.09411)

## Files

- [files/kshell/cwg2.snt](files/kshell/cwg2.snt)

## Citation

B. A. Brown, N. J. Stone, J. R. Stone, I. S. Towner, and M. Hjorth-Jensen, "Magnetic moments of the 2+1 states around 132Sn," Phys. Rev. C 71, 044317 (2005). DOI: [10.1103/PhysRevC.71.044317](https://doi.org/10.1103/PhysRevC.71.044317)
