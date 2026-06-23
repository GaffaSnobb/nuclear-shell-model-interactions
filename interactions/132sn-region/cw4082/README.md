# CW4082

`CW4082` is the Chou-Warburton tuned interaction enlarged to include the proton `0g9/2` orbit below the `Z=50` shell closure. It uses a `Z=40, N=82` bookkeeping core in the source paper. This entry is documentation-only; no raw KSHELL interaction file is included.

## Orbital Space

```text
CW4082 orbital space
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

Chou and Warburton created `CW4082` by expanding the tuned `CW5082` interaction to include the proton `0g9/2` orbit.

The source paper states that:

- the `0g9/2` orbit was added because of its possible strong influence on first-forbidden beta-decay observables,
- the added `0g9/2` TBMEs were generated with the H7B bare G-matrix potential plus Coulomb,
- calculations in the `4082` spaces used an inert full proton `0g9/2` orbit plus one particle-hole excitation out of that orbit.

Warburton and Towner later identify `CW4082` as the shell-model interaction used in their A ~= 132 axial-charge study.

## Notes

`CW4082` is the closest named interaction in this trail to the Warburton-Towner axial-charge paper. It still does not look like the plain `/Applications/kshell/snt/sn100.snt` file, which uses a `Z=50, N=50` KSHELL convention with both proton and neutron particles in the `50-82` shell.

## Relevant Literature

- W.-T. Chou and E. K. Warburton, "Construction of shell-model interactions for Z=50, N=82 nuclei: Predictions for A=133-134 beta decays," Phys. Rev. C 45, 1720 (1992). DOI: [10.1103/PhysRevC.45.1720](https://doi.org/10.1103/PhysRevC.45.1720)
- E. K. Warburton and I. S. Towner, "Renormalization of the axial charge at A ~= 132," Phys. Lett. B 294, 1-6 (1992). Uses `CW4082` for the A ~= 132 beta-decay study. DOI: [10.1016/0370-2693(92)91629-N](https://doi.org/10.1016/0370-2693(92)91629-N)
- A. Hosaka, K.-I. Kubo, and H. Toki, Nucl. Phys. A 244, 76 (1985). H7B source cited by Chou and Warburton for the added `0g9/2` TBMEs.

## Files

No raw interaction file is included.

## Citation

For `CW4082`, cite Chou and Warburton, Phys. Rev. C 45, 1720 (1992). If using it in the axial-charge context, also cite Warburton and Towner, Phys. Lett. B 294, 1 (1992).
