# Notes for w

## Relation to USDA and USDB

`w.snt` is the older Wildenthal/USD `sd`-shell interaction. USDA and USDB use the same `16O` core and `sd`-shell model space, but are later Brown-Richter refits of the USD-family Hamiltonian.

## Header Facts

The local file header says:

```text
Wildenthal's USD interaction for sd-shell
B. A. Brown and B. H. Wildenthal, Annu. Rev. Nucl. Part. Sci. 38, 29 (1988)
```

It also records default effective charges:

```text
eff_charge = 1.3, 0.5
```

## Caveats

The short name `w` appears to be a local interaction-library shorthand for the Wildenthal/USD interaction. The physical interaction should be cited through the USD/Wildenthal literature rather than through the short file name.
