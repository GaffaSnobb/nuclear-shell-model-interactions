# jun45

`jun45` is a KSHELL-format interaction for the `f5/2 p3/2 p1/2 g9/2` valence space outside a `56Ni` core. It is often used for nuclei around the `N = 50` region where the lower `0f7/2` orbital is treated as part of the inert core.

## Orbital Space

```text
JUN45 orbital space (KSHELL file convention)
Core: Z=28, N=28

            proton orbitals                           neutron orbitals
    major  orbital             SPE             major  orbital             SPE
          active model space                         active model space

  sdg  0g9/2   [10]   -6.262 MeV           sdg  0g9/2   [10]   -6.262 MeV
  pf   1p1/2   [ 2]   -7.839 MeV           pf   1p1/2   [ 2]   -7.839 MeV
  pf   0f5/2   [ 6]   -8.709 MeV           pf   0f5/2   [ 6]   -8.709 MeV
  pf   1p3/2   [ 4]   -9.828 MeV           pf   1p3/2   [ 4]   -9.828 MeV

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

The local KSHELL header identifies the file as:

```text
JUN45 for f5pg9 shell
M. Honma, T. Otsuka, T. Mizusaki, and M. H.-Jensen
Phys. Rev. C 80, 064323 (2009)
```

Midtboe's PhD dissertation describes `JUN45` as an interaction for the `f5/2`, `p`, and `g9/2` orbitals built on a `56Ni` core. The dissertation states that the fit used about 400 experimental energies concentrated around `Z = 30-32` isotopes and `N = 46-50` isotones, with 45 varied linear combinations and an rms deviation of about `185 keV`.

## Notes

The model space splits the normal `pf` and `sdg` oscillator families: `0f7/2` and `0g7/2` are outside the active space. The dissertation notes that this split has consequences for magnetic observables and quenching choices. In particular, the `JUN45` paper found better agreement with magnetic moments using a stronger spin `g`-factor quench than commonly used with `GXPF`.

For `70Ni`, the dissertation's reprinted paper notes that `JUN45` overestimates low-energy level energies and underestimates `B(E2)` strengths, likely because proton excitations from `0f7/2` are absent in this `56Ni`-core model space.

Local source checksum:

```text
bab3bafbc12251c696cb20fc78253d0d7b85344b  jun45.snt
```

## Relevant Literature

- M. Honma, T. Otsuka, T. Mizusaki, and M. Hjorth-Jensen, "New effective interaction for f5pg9-shell nuclei," Phys. Rev. C 80, 064323 (2009). DOI: [10.1103/PhysRevC.80.064323](https://doi.org/10.1103/PhysRevC.80.064323)
- J. E. Midtboe, "The low-energy enhancement: An experimental and theoretical study of nuclear level densities and gamma-ray strength functions," PhD dissertation, University of Oslo (2019), Sec. 2.8.4.

## Files

- [files/kshell/jun45.snt](files/kshell/jun45.snt)

## Citation

For calculations using this exact file, cite the local file name and checksum together with Honma et al., Phys. Rev. C 80, 064323 (2009).
