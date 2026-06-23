# sdpf-mu

`sdpf-mu` is a KSHELL-format interaction for the combined `sd` and `pf` shells outside a `16O` core. It is a cross-shell interaction intended for calculations where excitations across the `sd`-`pf` shell gap are important.

This entry is for `SDPF-MU`, not the larger `SDPFSDG-MU` interaction documented separately.

## Orbital Space

```text
SDPF-MU orbital space (KSHELL file convention)
Core: Z=8, N=8

            proton orbitals                           neutron orbitals
    major  orbital             SPE             major  orbital             SPE
          active model space                         active model space

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

The local KSHELL header identifies the file as:

```text
SDPF-MU interaction for sd+pf  0hw/1hw model space
Y. Utsuno, T. Otsuka, B. A. Brown, M. Honma, T. Mizusaki, and N. Shimizu
Phys. Rev. C 86, 051301(R) (2012)
```

Midtboe's PhD dissertation describes `SDPF-MU` as a construction combining existing `USD` and `GXPF1` components. The cross-shell TBMEs are supplied by the monopole-based universal interaction, `VMU`, based on a central mean-field potential plus a tensor component from meson-exchange terms.

## Notes

The local header describes the model space as `sd+pf 0hw/1hw`. In Midtboe's work, `SDPF-MU` was used in a `1 hbar omega` truncation for calculations involving `29Si`, `44Sc`, and `51Ti`, including total dipole-strength calculations with both `M1` and `E1` components.

Local source checksum:

```text
823c7944eb66e0bf75dddba7a1e63d847dd957aa  sdpf-mu.snt
```

## Relevant Literature

- Y. Utsuno, T. Otsuka, B. A. Brown, M. Honma, T. Mizusaki, and N. Shimizu, "Shape transitions in exotic Si and S isotopes and tensor-force-driven Jahn-Teller effect," Phys. Rev. C 86, 051301(R) (2012). DOI: [10.1103/PhysRevC.86.051301](https://doi.org/10.1103/PhysRevC.86.051301)
- T. Otsuka, T. Suzuki, M. Honma, Y. Utsuno, N. Tsunoda, K. Tsukiyama, and M. Hjorth-Jensen, "Novel Features of Nuclear Forces and Shell Evolution in Exotic Nuclei," Phys. Rev. Lett. 104, 012501 (2010). DOI: [10.1103/PhysRevLett.104.012501](https://doi.org/10.1103/PhysRevLett.104.012501)
- J. E. Midtboe, "The low-energy enhancement: An experimental and theoretical study of nuclear level densities and gamma-ray strength functions," PhD dissertation, University of Oslo (2019), Secs. 2.8.3 and 3.4.

## Files

- [files/kshell/sdpf-mu.snt](files/kshell/sdpf-mu.snt)

## Citation

For calculations using this exact file, cite the local file name and checksum together with Utsuno et al., Phys. Rev. C 86, 051301(R) (2012).
