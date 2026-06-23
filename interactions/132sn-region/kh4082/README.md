# KH4082

`KH4082` is the Chou-Warburton `KH` interaction enlarged to include the proton `0g9/2` orbit below the `Z=50` shell closure. It uses a `Z=40, N=82` bookkeeping core in the source paper. This entry is documentation-only; no raw KSHELL interaction file is included.

## Orbital Space

```text
KH4082 orbital space
Core: Z=40, N=82

            proton orbitals                           neutron orbitals
    major  orbital                              major  orbital
          active model space                         active model space

  pfh  0h11/2                              sdgi 0i13/2
  sdg  1d3/2                               pfh  1f5/2
  sdg  2s1/2                               pfh  0h9/2
  sdg  1d5/2                               pfh  2p1/2
  sdg  0g7/2                               pfh  2p3/2
  sdg  0g9/2                               pfh  1f7/2
```

## Provenance

Chou and Warburton created `KH4082` by expanding the `KH5082` model space to include the proton `0g9/2` orbit.

The source paper states that:

- the `0g9/2` orbit can have a strong role in first-forbidden beta decay,
- the `Z=50, N=82` spaces were expanded to a `Z=40, N=82` model-space convention,
- the `1043` TBMEs involving proton `0g9/2` were generated with the H7B bare G-matrix potential plus Coulomb,
- calculations in this space allowed an inert full `0g9/2` proton orbit plus one particle-hole excitation out of that orbit.

## Notes

`KH4082` is useful for tracing how H7B entered the Chou-Warburton interaction family. It should not be treated as a direct match to the plain `sn100.snt` file without further evidence.

## Relevant Literature

- W.-T. Chou and E. K. Warburton, "Construction of shell-model interactions for Z=50, N=82 nuclei: Predictions for A=133-134 beta decays," Phys. Rev. C 45, 1720 (1992). DOI: [10.1103/PhysRevC.45.1720](https://doi.org/10.1103/PhysRevC.45.1720)
- A. Hosaka, K.-I. Kubo, and H. Toki, Nucl. Phys. A 244, 76 (1985). H7B source cited by Chou and Warburton for the added `0g9/2` TBMEs.

## Files

No raw interaction file is included.

## Citation

For `KH4082`, cite Chou and Warburton, Phys. Rev. C 45, 1720 (1992), and note that the added proton `0g9/2` TBMEs were generated with H7B plus Coulomb.
