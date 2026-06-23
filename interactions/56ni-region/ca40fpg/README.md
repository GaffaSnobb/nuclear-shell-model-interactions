# ca40fpg

`CA40FPG` is documented in Midtboe's dissertation and the reprinted `70Ni` paper as a `40Ca`-core full-`fpg` interaction used with `NUSHELLX@MSU`. No matching `CA40FPG` KSHELL `.snt` file is included in the local source set checked for this entry.

## Orbital Space

No local KSHELL file is available for generating an exact diagram with SPEs. The model space reported in the `70Ni` paper is a full `fpg` space for both protons and neutrons, built on a `40Ca` core.

```text
CA40FPG reported orbital space
Core: Z=20, N=20

            proton orbitals                           neutron orbitals
    major  orbital             SPE             major  orbital             SPE
          active model space                         active model space

  sdg  0g9/2   [10]  not listed            sdg  0g9/2   [10]  not listed
  pf   1p1/2   [ 2]  not listed            pf   1p1/2   [ 2]  not listed
  pf   0f5/2   [ 6]  not listed            pf   0f5/2   [ 6]  not listed
  pf   1p3/2   [ 4]  not listed            pf   1p3/2   [ 4]  not listed
  pf   0f7/2   [ 8]  not listed            pf   0f7/2   [ 8]  not listed

  ------------------------- closed-shell boundary -------------------------

  sd   0d3/2   [ 4]  inert core            sd   0d3/2   [ 4]  inert core
  sd   1s1/2   [ 2]  inert core            sd   1s1/2   [ 2]  inert core
  sd   0d5/2   [ 6]  inert core            sd   0d5/2   [ 6]  inert core
  p    0p1/2   [ 2]  inert core            p    0p1/2   [ 2]  inert core
  p    0p3/2   [ 4]  inert core            p    0p3/2   [ 4]  inert core
  s    0s1/2   [ 2]  inert core            s    0s1/2   [ 2]  inert core
```

## Provenance

In the `70Ni` paper reprinted in Midtboe's dissertation, `CA40FPG` is described as a `NUSHELLX@MSU` interaction based on the `GXPF1A` `pf`-shell interaction, extended with many-body-perturbation-theory generated TBMEs to cover the full `fpg` model space for both protons and neutrons.

The same paper says the interaction had also been used to predict `70Co` beta-decay intensities for the `70Ni` experiment.

## Notes

For the `70Ni` calculations, the paper states that the `CA40FPG` model space was truncated because of its size. The stated restriction allowed limited proton excitations from `0f7/2` into the upper `fp g9/2` space and limited neutron excitations involving `g9/2`; the `g7/2` neutron occupancy was kept at zero in the expression printed in the paper.

No local KSHELL file named `ca40fpg.snt` was found in the source set checked for this entry.

## Relevant Literature

- A. C. Larsen, J. E. Midtboe, M. Guttormsen, T. Renstrom, S. N. Liddick, A. Spyrou, S. Karampagia, B. A. Brown, O. Achakovskiy, S. Kamerdzhiev, et al., "Enhanced low-energy gamma-decay strength of 70Ni and its robustness within the shell model," Phys. Rev. C 97, 054329 (2018). DOI: [10.1103/PhysRevC.97.054329](https://doi.org/10.1103/PhysRevC.97.054329)
- B. A. Brown and W. D. M. Rae, "The Shell-Model Code NuShellX@MSU," Nucl. Data Sheets 120, 115-118 (2014). DOI: [10.1016/j.nds.2014.07.022](https://doi.org/10.1016/j.nds.2014.07.022)
- M. Honma, T. Otsuka, B. A. Brown, and T. Mizusaki, "Shell-model description of neutron-rich pf-shell nuclei with a new effective interaction GXPF1," Eur. Phys. J. A 25, 499-502 (2005). DOI: [10.1140/epjad/i2005-06-032-2](https://doi.org/10.1140/epjad/i2005-06-032-2)
- J. E. Midtboe, "The low-energy enhancement: An experimental and theoretical study of nuclear level densities and gamma-ray strength functions," PhD dissertation, University of Oslo (2019), Paper I.

## Files

No raw interaction file is included because no matching local KSHELL `.snt` file was found.

## Citation

For calculations using `CA40FPG`, cite the application paper that describes the interaction and record the exact external interaction source used in the calculation workflow.
