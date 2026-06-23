# gxpf1a

`gxpf1a` is a KSHELL-format interaction for full `pf`-shell calculations outside a `40Ca` core. It is the revised `GXPF1` interaction used for improved descriptions of neutron-rich `pf`-shell nuclei.

## Orbital Space

```text
GXPF1A orbital space (KSHELL file convention)
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
GXPF1A pf-shell
M. Honma, T. Otsuka, B. A. Brown, and T. Mizusaki
Eur. Phys. J. A 25, Suppl. 1, 499 (2005)
```

Midtboe's PhD dissertation describes `GXPF1A` as a modified `GXPF1` interaction introduced to improve the description of newer experimental data on neutron-rich `pf`-shell nuclei. The dissertation notes that `GXPF1A` was used for the `59,60Ni` calculations in that thesis.

## Notes

The active model space and single-particle energies in the local `gxpf1a.snt` file match the local `gxpf1.snt` file; the distinction is in the two-body matrix elements.

Local source checksum:

```text
f48757b1bd8a7c588d824b2298708f4028811e2d  gxpf1a.snt
```

## Relevant Literature

- M. Honma, T. Otsuka, B. A. Brown, and T. Mizusaki, "Shell-model description of neutron-rich pf-shell nuclei with a new effective interaction GXPF1," Eur. Phys. J. A 25, 499-502 (2005). DOI: [10.1140/epjad/i2005-06-032-2](https://doi.org/10.1140/epjad/i2005-06-032-2)
- M. Honma, T. Otsuka, B. A. Brown, and T. Mizusaki, "Full pf-shell calculations with a new effective interaction," Nucl. Phys. A 704, 134C-143C (2002). DOI: [10.1016/S0375-9474(02)00774-1](https://doi.org/10.1016/S0375-9474(02)00774-1)
- J. E. Midtboe, "The low-energy enhancement: An experimental and theoretical study of nuclear level densities and gamma-ray strength functions," PhD dissertation, University of Oslo (2019), Sec. 2.8.2.

## Files

- [files/kshell/gxpf1a.snt](files/kshell/gxpf1a.snt)

## Citation

For calculations using this exact file, cite the local file name and checksum together with the Honma-Otsuka-Brown-Mizusaki `GXPF1A` literature.
