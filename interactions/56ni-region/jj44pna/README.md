# jj44pna

`jj44pna` is a KSHELL-format interaction for the `f5/2 p3/2 p1/2 g9/2` model space outside a `56Ni` core.

## Orbital Space

```text
JJ44PNA orbital space (KSHELL file convention)
Core: Z=28, N=28

            proton orbitals                           neutron orbitals
    major  orbital             SPE             major  orbital             SPE
          active model space                         active model space

  sdg  0g9/2   [10]   -8.905 MeV           sdg  0g9/2   [10]   -5.255 MeV
  pf   1p1/2   [ 2]  -12.044 MeV           pf   1p1/2   [ 2]   -8.361 MeV
  pf   1p3/2   [ 4]  -13.437 MeV           pf   0f5/2   [ 6]   -9.153 MeV
  pf   0f5/2   [ 6]  -14.938 MeV           pf   1p3/2   [ 4]   -9.988 MeV

  ------------------------- closed-shell boundary -------------------------

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
../bin/nushell2snt.py jj44pn.sp jj44pna.int  in proton-neutron formalism
```

The header does not name a paper. Midtboe's dissertation links the `JJ44PNA` interaction parameters to Lisetskiy, Brown, Horoi, and Grawe's `T = 1` effective-interaction work in the `f5/2 p3/2 p1/2 g9/2` model space. The dissertation also notes that `CA48MH2` is obtained from `CA48MH1` by replacing the neutron-neutron TBMEs with `JJ44PNA`-type parameters and modifying diagonal proton `0f7/2` matrix elements.

## Notes

The local file has proton and neutron spaces with the same orbital labels, but different proton and neutron SPEs.

Local source checksum:

```text
33d6a6a64703451a593c8261190c8187ff79935b  jj44pna.snt
```

## Relevant Literature

- A. F. Lisetskiy, B. A. Brown, M. Horoi, and H. Grawe, "New T = 1 effective interactions for the f5/2 p3/2 p1/2 g9/2 model space: Implications for valence-mirror symmetry and seniority isomers," Phys. Rev. C 70, 044314 (2004). DOI: [10.1103/PhysRevC.70.044314](https://doi.org/10.1103/PhysRevC.70.044314)
- J. E. Midtboe, "The low-energy enhancement: An experimental and theoretical study of nuclear level densities and gamma-ray strength functions," PhD dissertation, University of Oslo (2019), Secs. 2.8.5 and Paper I.

## Files

- [files/kshell/jj44pna.snt](files/kshell/jj44pna.snt)

## Citation

For calculations using this exact file, cite the local file name and checksum. For the interaction family, cite Lisetskiy et al., Phys. Rev. C 70, 044314 (2004).
