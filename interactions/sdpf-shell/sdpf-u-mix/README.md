# SDPF-U-MIX

`SDPF-U-MIX` extends SDPF-U-SI to mix neutron configurations across the N=20 shell gap. It targets neutron-rich nuclei around the N=20 and N=28 islands of inversion. The construction is described in the Appendix of [Caurier, Nowacki, and Poves (2014)](https://doi.org/10.1103/PhysRevC.90.014302).

## Orbital Space

```text
SDPF-U-MIX orbital space (published calculation space)
Core: Z=8, N=8 (16O)

            proton orbitals                    neutron orbitals
    major  orbital       capacity      major  orbital       capacity
          active model space                 active model space

                                       pf   0f5/2          [ 6]
                                       pf   1p1/2          [ 2]
                                       pf   1p3/2          [ 4]
                                       pf   0f7/2          [ 8]
  sd   0d3/2             [ 4]          sd   0d3/2          [ 4]
  sd   1s1/2             [ 2]          sd   1s1/2          [ 2]
  sd   0d5/2             [ 6]          sd   0d5/2          [ 6]

  -------------------- closed-shell boundary --------------------

  p    0p1/2   [ 2]  inert core        p    0p1/2   [ 2]  inert core
  p    0p3/2   [ 4]  inert core        p    0p3/2   [ 4]  inert core
  s    0s1/2   [ 2]  inert core        s    0s1/2   [ 2]  inert core
```

The diagram records the published space, not a parsed interaction file; vertical order is schematic, not an SPE scale. Brackets give orbital capacities. No SPE values are inferred from another interaction.

## Provenance

The parent uses USD in the sd sector and a KB3 variant in the pf sector. SDPF-U-MIX adds scaled Lee-Kahana-Scott cross-shell matrix elements, retunes SPEs and monopoles, and reduces sd-shell isovector pairing to avoid double counting. The first excited 0+ in 30Mg helps constrain the tuning. See Sec. I and the Appendix of [Caurier et al. (2014)](https://doi.org/10.1103/PhysRevC.90.014302).

An earlier application used SDPF-U-MIX to describe the intruder 0+ state in 34Si: [Rotaru et al. (2012)](https://doi.org/10.1103/PhysRevLett.109.092503).

## Notes

The published calculations allow neutron sd-to-pf excitations; proton pf excitations are omitted. The Appendix cautions against applying this treatment to Ar and Ca near N=20 without proton excitations. Do not equate shell-space capacity with validated applicability.

SDPF-U-MIX is distinct from [SDPF-MU](../sdpf-mu/README.md), [SDPFSDG-MU](../../sdpf-sdg-shell/sdpfsdg-mu/README.md), and [gs8](../../sdpf-sdg-shell/gs8/README.md); similarly named interactions are not interchangeable files.

## Relevant Literature

- E. Caurier, F. Nowacki, and A. Poves, "Merging of the islands of inversion at N = 20 and N = 28," Phys. Rev. C 90, 014302 (2014). Interaction construction: Sec. I and Appendix; calculation space: Secs. II and VII. DOI: [10.1103/PhysRevC.90.014302](https://doi.org/10.1103/PhysRevC.90.014302). [Open PDF](https://harvest.aps.org/v2/journals/articles/10.1103/PhysRevC.90.014302/fulltext).
- F. Nowacki and A. Poves, "New effective interaction for 0 hbar omega shell-model calculations in the sd-pf valence space," Phys. Rev. C 79, 014310 (2009). Parent SDPF-U interaction. DOI: [10.1103/PhysRevC.79.014310](https://doi.org/10.1103/PhysRevC.79.014310).
- F. Rotaru et al., "Unveiling the Intruder Deformed 0+_2 State in 34Si," Phys. Rev. Lett. 109, 092503 (2012). Early SDPF-U-MIX application. DOI: [10.1103/PhysRevLett.109.092503](https://doi.org/10.1103/PhysRevLett.109.092503). [Preprint](https://arxiv.org/abs/1206.6572).

## Files

No matching KSHELL interaction file was found in the local interaction collection. This entry documents the published interaction; no raw file is included.

## Citation

Cite Caurier, Nowacki, and Poves (2014) for the SDPF-U-MIX construction and Nowacki and Poves (2009) for SDPF-U. Record the exact file version, conversion source, and calculation truncation when using an interaction file.
