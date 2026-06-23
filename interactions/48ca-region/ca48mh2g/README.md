# ca48mh2g

`ca48mh2g` is a KSHELL-format interaction for calculations around a `48Ca` core. The file uses a `Z=20, N=28` core, with proton particles in the full `pf` shell and neutron particles in the upper-`pf` orbitals plus `0g9/2`.

This entry is a local `ca48mh2`-family variant with a shifted neutron `0g9/2` SPE.

## Orbital Space

```text
CA48MH2G orbital space (KSHELL file convention)
Core: Z=20, N=28

            proton orbitals                           neutron orbitals
    major  orbital             SPE             major  orbital             SPE
          active model space                         active model space

  pf   1p1/2   [ 2]   -5.133 MeV           sdg  0g9/2   [10]    1.400 MeV
  pf   0f5/2   [ 6]   -5.554 MeV           pf   0f5/2   [ 6]   -0.366 MeV
  pf   1p3/2   [ 4]   -6.542 MeV           pf   1p1/2   [ 2]   -1.989 MeV
  pf   0f7/2   [ 8]   -9.626 MeV           pf   1p3/2   [ 4]   -4.282 MeV

  ------------------------- closed-shell boundary -------------------------

  sd   0d3/2   [ 4]  inert core            pf   0f7/2   [ 8]  inert core
  sd   1s1/2   [ 2]  inert core            sd   0d3/2   [ 4]  inert core
  sd   0d5/2   [ 6]  inert core            sd   1s1/2   [ 2]  inert core
  p    0p1/2   [ 2]  inert core            sd   0d5/2   [ 6]  inert core
  p    0p3/2   [ 4]  inert core            p    0p1/2   [ 2]  inert core
  s    0s1/2   [ 2]  inert core            p    0p3/2   [ 4]  inert core
                                           s    0s1/2   [ 2]  inert core
```

## Provenance

The local KSHELL header says:

```text
../bin/nushell2snt.py ca48pn.sp ca48mh2.int  in proton-neutron formalism
```

No paper title, DOI, or author list is included in the header. The file is therefore documented here as a local KSHELL conversion of the NuShellX-style `ca48pn.sp` and `ca48mh2.int` inputs.

The model space matches the `48Ca`-core `fpg9/2` space commonly described in the literature around the Sorlin et al. `fpg` interaction. The exact origin of the local `ca48mh2g` file label is not established from the KSHELL header or from a public exact-name search.

Midtboe's dissertation describes the base `CA48MH2` interaction as a `CA48MH1`-family variant where the neutron-neutron TBMEs are replaced by `JJ44PNA`-type parameters and diagonal proton `0f7/2` matrix elements are modified using the `54Fe` spectrum.

## Notes

`ca48mh2g` uses the same active orbitals as `ca48mh2`, and the same proton SPEs. Relative to `ca48mh2`, the neutron `0g9/2` SPE is moved from `-0.173 MeV` to `1.400 MeV` in the copied file.

Local source checksum:

```text
7bd10ba29a5ad80532c6362968a13c3b3760af27  ca48mh2g.snt
```

## Relevant Literature

- O. Sorlin et al., "`^{68}_{28}Ni_{40}: Magicity versus Superfluidity`," Phys. Rev. Lett. 88, 092501 (2002). Standard literature trail for the `48Ca`-core `fpg` interaction family; not named in the local `ca48mh2g.snt` header. DOI: [10.1103/PhysRevLett.88.092501](https://doi.org/10.1103/PhysRevLett.88.092501)
- A. Poves, J. Sanchez-Solano, E. Caurier, and F. Nowacki, "Shell model study of the isobaric chains A=50, A=51 and A=52," Nucl. Phys. A 694, 157-198 (2001). Source for the KB3G/full-`pf` interaction ingredients cited in the `fpg` literature. DOI: [10.1016/S0375-9474(01)00967-8](https://doi.org/10.1016/S0375-9474(01)00967-8)
- S. Kahana, H. C. Lee, and C. K. Scott, "Effect of Woods-Saxon Wave Functions on the Calculation of A=18, 206, 210 Spectra with a Realistic Interaction," Phys. Rev. 180, 956-966 (1969). Cited in the `fpg` literature for cross-shell two-body matrix elements involving `g9/2`. DOI: [10.1103/PhysRev.180.956](https://doi.org/10.1103/PhysRev.180.956)
- M. Hjorth-Jensen, T. T. S. Kuo, and E. Osnes, "Realistic effective interactions for nuclear systems," Phys. Rep. 261, 125-270 (1995). General background for realistic shell-model effective interactions. DOI: [10.1016/0370-1573(95)00012-6](https://doi.org/10.1016/0370-1573(95)00012-6)
- P. C. Srivastava and V. K. B. Kota, "Shell-model results in fp and fpg9/2 spaces for 61,63,65Co isotopes," Physics of Atomic Nuclei 74, 971-978 (2011). Useful secondary description of the `48Ca`-core `fpg9/2` setup and its relation to Sorlin et al. DOI: [10.1134/S1063778811070143](https://doi.org/10.1134/S1063778811070143), arXiv: [1004.4443](https://arxiv.org/abs/1004.4443)
- A. F. Lisetskiy, B. A. Brown, M. Horoi, and H. Grawe, "New T = 1 effective interactions for the f5/2 p3/2 p1/2 g9/2 model space: Implications for valence-mirror symmetry and seniority isomers," Phys. Rev. C 70, 044314 (2004). Literature trail for the `JJ44PNA`-type neutron-neutron TBMEs discussed in the dissertation. DOI: [10.1103/PhysRevC.70.044314](https://doi.org/10.1103/PhysRevC.70.044314)
- A. C. Larsen, J. E. Midtboe, M. Guttormsen et al., "Enhanced low-energy gamma-decay strength of 70Ni and its robustness within the shell model," Phys. Rev. C 97, 054329 (2018). Discusses the `CA48MH` interaction family in the `70Ni` calculation context. DOI: [10.1103/PhysRevC.97.054329](https://doi.org/10.1103/PhysRevC.97.054329)
- J. E. Midtboe, "The low-energy enhancement: An experimental and theoretical study of nuclear level densities and gamma-ray strength functions," PhD dissertation, University of Oslo (2019), Sec. 2.8.5.

## Files

- [files/kshell/ca48mh2g.snt](files/kshell/ca48mh2g.snt)

## Citation

For calculations using this exact file, record the local file name and checksum. Until the exact NuShellX `ca48mh2g` label provenance is resolved, cite the `48Ca`-core `fpg` interaction literature beginning with Sorlin et al., Phys. Rev. Lett. 88, 092501 (2002), DOI: [10.1103/PhysRevLett.88.092501](https://doi.org/10.1103/PhysRevLett.88.092501).
