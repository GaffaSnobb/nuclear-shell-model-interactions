# CW5082

`CW5082` is the locally tuned Chou-Warburton interaction for the `132Sn` region, using a `Z=50, N=82` core. It is documented here from the source paper; no raw KSHELL interaction file is included.

## Orbital Space

```text
CW5082 orbital space
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

Chou and Warburton construct `CW5082` from `KH5082` in order to tune the interaction to local `132Sn`-region spectroscopy.

The paper states that `CW5082` was obtained by:

- replacing the proton `Q'=4` TBMEs with the Kruse-Wildenthal effective interaction,
- adopting the Kruse-Wildenthal proton single-particle energies,
- decreasing the neutron-orbit binding energies by `100 keV`,
- modifying five selected proton-neutron TBMEs to better reproduce the known `J=0` and `J=1` levels of `134Sb`.

## Notes

This is the `5082` version of the Chou-Warburton tuned interaction. It does not include the proton `0g9/2` hole orbit; that enlarged space is documented as `CW4082`.

The Warburton-Towner axial-charge paper later states that its shell-model interaction is `CW4082`, not `CW5082`.

## Relevant Literature

- W.-T. Chou and E. K. Warburton, "Construction of shell-model interactions for Z=50, N=82 nuclei: Predictions for A=133-134 beta decays," Phys. Rev. C 45, 1720 (1992). DOI: [10.1103/PhysRevC.45.1720](https://doi.org/10.1103/PhysRevC.45.1720)
- H. G. Kruse and B. H. Wildenthal, Bull. Am. Phys. Soc. 27, 533 (1982). Source of the proton interaction cited by Chou and Warburton.

## Files

No raw interaction file is included.

## Citation

For `CW5082`, cite Chou and Warburton, Phys. Rev. C 45, 1720 (1992), and note the Kruse-Wildenthal proton-sector input described there.
