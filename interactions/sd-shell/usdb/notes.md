# Notes for usdb

## Relation to W and USDA

USDB is a later Brown-Richter refit of the USD-family `sd`-shell Hamiltonian. It uses the same `16O` core and `sd` model space as `w.snt` and `usda.snt`, but has different single-particle energies and two-body matrix elements.

USDA and USDB are companion fits from the same Brown-Richter work. They should not be treated as two names for the same interaction.

## Header Caveat

The copied local file is named `usdb.snt`, but its first header line says:

```text
USDA sd shell from  sd.sp usda.int
```

This appears to be stale or copied header text. The file differs from `usda.snt`; for example the `0d3/2` SPE is `2.1117 MeV` in `usdb.snt`, compared with `1.9798 MeV` in `usda.snt`.

## Header Citation

The local file header cites:

```text
W. A. Richter, S. Mkhize, and B. Alex Brown
Phys. Rev. C 78, 064302 (2008)
```

The 2008 paper discusses observables for USDA and USDB. The Hamiltonians were introduced earlier in Brown and Richter, Phys. Rev. C 74, 034315 (2006).
