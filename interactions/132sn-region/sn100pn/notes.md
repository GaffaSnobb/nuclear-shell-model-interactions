# Notes for sn100pn

## Core convention

The Brown et al. paper discusses `N <= 82` systems using a 132Sn closed-shell reference with neutron holes. The KSHELL file uses a `Z=50, N=50` core and places both proton and neutron particles in the 50-82 shell.

For 133Xe this means:

```text
Z = 54 -> 4 valence protons
N = 79 -> 29 valence neutrons
```

This is equivalent to the paper's `4 proton particles + 3 neutron holes` description, but the file itself uses particle-on-top bookkeeping.

## Open provenance question

The interaction physics is attributed to Brown et al. (2005). The exact `sn100pn` name appears to come from the NuShell@MSU interaction library, but a public source identifying who coined the file name has not yet been found.
