# gxpf1

`gxpf1` is a KSHELL-format interaction for full `pf`-shell calculations outside a `40Ca` core. The file uses the same proton and neutron valence space: `0f7/2`, `1p3/2`, `0f5/2`, and `1p1/2`.

## Orbital Space

```text
GXPF1 orbital space (KSHELL file convention)
Core: Z=20, N=20

            proton orbitals                           neutron orbitals
    major  orbital             SPE             major  orbital             SPE
          active model space                         active model space

  pf   0f5/2   [ 6]   -1.383 MeV           pf   0f5/2   [ 6]   -1.383 MeV
  pf   1p1/2   [ 2]   -4.137 MeV           pf   1p1/2   [ 2]   -4.137 MeV
  pf   1p3/2   [ 4]   -5.679 MeV           pf   1p3/2   [ 4]   -5.679 MeV
  pf   0f7/2   [ 8]   -8.624 MeV           pf   0f7/2   [ 8]   -8.624 MeV

  ------------------------- closed-shell boundary -------------------------

  sd   0d3/2   [ 4]  inert core            sd   0d3/2   [ 4]  inert core
  sd   1s1/2   [ 2]  inert core            sd   1s1/2   [ 2]  inert core
  sd   0d5/2   [ 6]  inert core            sd   0d5/2   [ 6]  inert core
  p    0p1/2   [ 2]  inert core            p    0p1/2   [ 2]  inert core
  p    0p3/2   [ 4]  inert core            p    0p3/2   [ 4]  inert core
  s    0s1/2   [ 2]  inert core            s    0s1/2   [ 2]  inert core
```

## Provenance

The local KSHELL header identifies the file as:

```text
GXPF1 for pf-shell
M. Honma, T. Otsuka, B.A. Brown, and T. Mizusaki
Phys. Rev. C 65, 061301(R) (2002)
```

Midtboe's PhD dissertation describes `GXPF1` as a standard `pf`-shell interaction obtained by starting from a theoretical effective interaction and fitting a subset of linear combinations of the interaction parameters. In the dissertation's summary, the `pf` shell has four single-particle energies and 195 two-body matrix elements, and the `GXPF1` fit varied 70 linear combinations.

## Notes

The dissertation states that the original `GXPF1` fit gives an rms deviation of about `168 keV` between calculated and experimental levels, with some caveat because parts of the fit involved Monte Carlo Shell Model calculations with an empirical FDA* correction.

Local source checksum:

```text
6e92dc644cbf73a762899df33db89915a0ad2b5c  gxpf1.snt
```

## Relevant Literature

- M. Honma, T. Otsuka, B. A. Brown, and T. Mizusaki, "Full pf-shell calculations with a new effective interaction," Nucl. Phys. A 704, 134C-143C (2002). DOI: [10.1016/S0375-9474(02)00774-1](https://doi.org/10.1016/S0375-9474(02)00774-1)
- M. Honma, T. Otsuka, B. A. Brown, and T. Mizusaki, Phys. Rev. C 65, 061301(R) (2002). This is the reference named in the local KSHELL header.
- J. E. Midtboe, "The low-energy enhancement: An experimental and theoretical study of nuclear level densities and gamma-ray strength functions," PhD dissertation, University of Oslo (2019), Sec. 2.8.2.

## Files

- [files/kshell/gxpf1.snt](files/kshell/gxpf1.snt)

## Citation

For calculations using this exact file, cite the local file name and checksum together with the Honma-Otsuka-Brown-Mizusaki `GXPF1` literature.
