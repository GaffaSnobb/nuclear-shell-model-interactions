# KH5082

`KH5082` is a Chou-Warburton shell-model interaction for nuclei near `132Sn`, using a `Z=50, N=82` core. It is documented here from the source paper; no raw KSHELL interaction file is included.

## Orbital Space

```text
KH5082 orbital space
Core: Z=50, N=82

            proton orbitals                           neutron orbitals
    major  orbital                              major  orbital
          active model space                         active model space

  pfh  0h11/2                              sdgi 0i13/2
  sdg  1d3/2                               pfh  1f5/2
  sdg  2s1/2                               pfh  0h9/2
  sdg  1d5/2                               pfh  2p1/2
  sdg  0g7/2                               pfh  2p3/2
                                           pfh  1f7/2
```

## Provenance

Chou and Warburton define `KH5082` as the conventional `132Sn`-region interaction built from the Kuo-Herling two-body matrix elements for the `208Pb` region.

The paper states that:

- the Kuo-Herling TBMEs were scaled by `(132/208)^(-1/3)`,
- six neutron-neutron `J=0` TBMEs were multiplied by `0.6`,
- proton single-particle energies were taken from experimental yrast states,
- neutron single-particle energies were inferred using experimental and theoretical `(d,p)` spectroscopic-strength centroids in `N=83` isotones.

## Notes

This entry is useful for tracing the `CW/KH` interaction family, but it is not currently a ready-to-run KSHELL entry in this repository.

`KH5082` should not be confused with `sn100pn.snt`. The `KH5082` bookkeeping uses neutron particles above `N=82`; `sn100pn.snt` uses a `Z=50, N=50` KSHELL convention with neutron particles in the `50-82` shell.

## Relevant Literature

- W.-T. Chou and E. K. Warburton, "Construction of shell-model interactions for Z=50, N=82 nuclei: Predictions for A=133-134 beta decays," Phys. Rev. C 45, 1720 (1992). DOI: [10.1103/PhysRevC.45.1720](https://doi.org/10.1103/PhysRevC.45.1720)
- T. T. S. Kuo and G. Herling, U.S. Naval Research Laboratory Report No. 2258 (1971). Source of the Kuo-Herling interaction cited by Chou and Warburton.
- J. B. McGrory, Phys. Rev. C 8, 693 (1973). Cited by Chou and Warburton in connection with the Kuo-Herling interaction.
- E. K. Warburton and B. A. Brown, Phys. Rev. C 43, 602 (1991). Cited by Chou and Warburton in connection with the Kuo-Herling interaction and local spectroscopy.

## Files

No raw interaction file is included.

## Citation

For `KH5082`, cite Chou and Warburton, Phys. Rev. C 45, 1720 (1992), together with the Kuo-Herling source cited in that paper.
