# usdb

`usdb` is one of the Brown-Richter updated USD Hamiltonians for the `sd` shell. The file uses a `Z=8, N=8` core, so nuclei are represented with proton and neutron particles above a `16O` inert core.

USDB uses the same model space as USDA and the older Wildenthal/USD interaction, but with its own refitted single-particle energies and two-body matrix elements.

## Model Space

Core in the KSHELL file:

```text
Z = 8, N = 8
```

Proton orbitals:

```text
0d5/2, 1s1/2, 0d3/2
```

Neutron orbitals:

```text
0d5/2, 1s1/2, 0d3/2
```

## Orbital Space

```text
USDB orbital space (KSHELL file convention)
Core: Z=8, N=8

            proton orbitals                           neutron orbitals
    major  orbital             SPE             major  orbital             SPE
          active model space                         active model space

  sd   0d3/2   [ 4]    2.112 MeV           sd   0d3/2   [ 4]    2.112 MeV
  sd   1s1/2   [ 2]   -3.208 MeV           sd   1s1/2   [ 2]   -3.208 MeV
  sd   0d5/2   [ 6]   -3.926 MeV           sd   0d5/2   [ 6]   -3.926 MeV

  ------------------------- closed-shell boundary -------------------------

  p    0p1/2   [ 2]  inert core            p    0p1/2   [ 2]  inert core
  p    0p3/2   [ 4]  inert core            p    0p3/2   [ 4]  inert core
  s    0s1/2   [ 2]  inert core            s    0s1/2   [ 2]  inert core
```

## Provenance

The local KSHELL file is named `usdb.snt` and has USDB single-particle energies and matrix elements, but its header text still says `USDA sd shell from sd.sp usda.int`. The file nevertheless differs from `usda.snt`. The USDA/USDB Hamiltonians were introduced in Brown and Richter, Phys. Rev. C 74, 034315 (2006), and the local header cites Richter, Mkhize, and Brown, Phys. Rev. C 78, 064302 (2008).

## Relevant Literature

- B. Alex Brown and W. A. Richter, "New \"USD\" Hamiltonians for the sd shell," Phys. Rev. C 74, 034315 (2006). Origin paper for the USDA and USDB Hamiltonians. DOI: [10.1103/PhysRevC.74.034315](https://doi.org/10.1103/PhysRevC.74.034315)
- W. A. Richter, S. Mkhize, and B. Alex Brown, "sd-shell observables for the USDA and USDB Hamiltonians," Phys. Rev. C 78, 064302 (2008). Literature reference cited by the local KSHELL `usdb.snt` header. DOI: [10.1103/PhysRevC.78.064302](https://doi.org/10.1103/PhysRevC.78.064302)
- B. A. Brown and B. H. Wildenthal, "Status of the Nuclear Shell Model," Annu. Rev. Nucl. Part. Sci. 38, 29-66 (1988). Background for the earlier USD/Wildenthal interaction. DOI: [10.1146/annurev.ns.38.120188.000333](https://doi.org/10.1146/annurev.ns.38.120188.000333)

## Files

- [files/kshell/usdb.snt](files/kshell/usdb.snt)

## Citation

B. Alex Brown and W. A. Richter, "New \"USD\" Hamiltonians for the sd shell," Phys. Rev. C 74, 034315 (2006). DOI: [10.1103/PhysRevC.74.034315](https://doi.org/10.1103/PhysRevC.74.034315)
