# w

`w` is the KSHELL copy of Wildenthal's USD interaction for the `sd` shell. The file uses a `Z=8, N=8` core, so nuclei are represented with proton and neutron particles above a `16O` inert core.

This is the older USD-family interaction that USDA and USDB were later refitted from.

## Orbital Space

```text
W orbital space (KSHELL file convention)
Core: Z=8, N=8

            proton orbitals                           neutron orbitals
    major  orbital             SPE             major  orbital             SPE
          active model space                         active model space

  sd   0d3/2   [ 4]    1.647 MeV           sd   0d3/2   [ 4]    1.647 MeV
  sd   1s1/2   [ 2]   -3.164 MeV           sd   1s1/2   [ 2]   -3.164 MeV
  sd   0d5/2   [ 6]   -3.948 MeV           sd   0d5/2   [ 6]   -3.948 MeV

  ------------------------- closed-shell boundary -------------------------

  p    0p1/2   [ 2]  inert core            p    0p1/2   [ 2]  inert core
  p    0p3/2   [ 4]  inert core            p    0p3/2   [ 4]  inert core
  s    0s1/2   [ 2]  inert core            s    0s1/2   [ 2]  inert core
```

## Provenance

The local KSHELL file header identifies this as Wildenthal's USD interaction for the `sd` shell and cites Brown and Wildenthal, Annu. Rev. Nucl. Part. Sci. 38, 29 (1988).

## Notes

`w.snt` is the older Wildenthal/USD `sd`-shell interaction. USDA and USDB use the same `16O` core and `sd`-shell model space, but are later Brown-Richter refits of the USD-family Hamiltonian.

The local file header says:

```text
Wildenthal's USD interaction for sd-shell
B. A. Brown and B. H. Wildenthal, Annu. Rev. Nucl. Part. Sci. 38, 29 (1988)
```

It also records default effective charges:

```text
eff_charge = 1.3, 0.5
```

The short name `w` appears to be a local interaction-library shorthand for the Wildenthal/USD interaction. The physical interaction should be cited through the USD/Wildenthal literature rather than through the short file name.

## Relevant Literature

- B. H. Wildenthal, "Empirical strengths of spin operators in nuclei," Prog. Part. Nucl. Phys. 11, 5-51 (1984). Early USD/Wildenthal `sd`-shell interaction context. DOI: [10.1016/0146-6410(84)90011-5](https://doi.org/10.1016/0146-6410(84)90011-5)
- B. A. Brown and B. H. Wildenthal, "Status of the Nuclear Shell Model," Annu. Rev. Nucl. Part. Sci. 38, 29-66 (1988). Literature reference cited by the local KSHELL `w.snt` header. DOI: [10.1146/annurev.ns.38.120188.000333](https://doi.org/10.1146/annurev.ns.38.120188.000333)
- B. Alex Brown and W. A. Richter, "New \"USD\" Hamiltonians for the sd shell," Phys. Rev. C 74, 034315 (2006). Introduces the later USDA and USDB refits from the USD-family interaction. DOI: [10.1103/PhysRevC.74.034315](https://doi.org/10.1103/PhysRevC.74.034315)

## Files

- [files/kshell/w.snt](files/kshell/w.snt)

## Citation

B. A. Brown and B. H. Wildenthal, "Status of the Nuclear Shell Model," Annu. Rev. Nucl. Part. Sci. 38, 29-66 (1988). DOI: [10.1146/annurev.ns.38.120188.000333](https://doi.org/10.1146/annurev.ns.38.120188.000333)
