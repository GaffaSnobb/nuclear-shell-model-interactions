# SDPFSDG-MU

`SDPFSDG-MU` is a KSHELL-format interaction for a large `sd-pf-sdg` valence space above a `16O` core. The raw `.snt` file is not included in this repository.

The local file uses proton-neutron formalism with identical proton and neutron orbital lists. The active space contains the full `sd` shell, the full `pf` shell, and the `sdg` orbitals `0g9/2`, `0g7/2`, `1d5/2`, `1d3/2`, and `2s1/2`.

## Orbital Space

```text
SDPFSDG-MU orbital space (KSHELL file convention)
Core: Z=8, N=8

            proton orbitals                           neutron orbitals
    major  orbital             SPE             major  orbital             SPE
          active model space                         active model space

  sdg  0g7/2   [ 8]   15.982 MeV           sdg  0g7/2   [ 8]   15.982 MeV
  sdg  1d3/2   [ 4]   11.102 MeV           sdg  1d3/2   [ 4]   11.102 MeV
  sdg  2s1/2   [ 2]   10.453 MeV           sdg  2s1/2   [ 2]   10.453 MeV
  sdg  0g9/2   [10]   10.219 MeV           sdg  0g9/2   [10]   10.219 MeV
  sdg  1d5/2   [ 6]    6.619 MeV           sdg  1d5/2   [ 6]    6.619 MeV
  pf   0f5/2   [ 6]   10.022 MeV           pf   0f5/2   [ 6]   10.022 MeV
  pf   0f7/2   [ 8]    5.063 MeV           pf   0f7/2   [ 8]    5.063 MeV
  pf   1p1/2   [ 2]    1.903 MeV           pf   1p1/2   [ 2]    1.903 MeV
  pf   1p3/2   [ 4]    1.184 MeV           pf   1p3/2   [ 4]    1.184 MeV
  sd   0d3/2   [ 4]    1.647 MeV           sd   0d3/2   [ 4]    1.647 MeV
  sd   1s1/2   [ 2]   -3.164 MeV           sd   1s1/2   [ 2]   -3.164 MeV
  sd   0d5/2   [ 6]   -3.948 MeV           sd   0d5/2   [ 6]   -3.948 MeV

  ------------------------- closed-shell boundary -------------------------

  p    0p1/2   [ 2]  inert core            p    0p1/2   [ 2]  inert core
  p    0p3/2   [ 4]  inert core            p    0p3/2   [ 4]  inert core
  s    0s1/2   [ 2]  inert core            s    0s1/2   [ 2]  inert core
```

## Provenance

The local KSHELL header identifies the model-space source as:

```text
sdpfsdg_64.sps
sdpfsdg-shell
```

and the interaction source as:

```text
GCLSTsdpfsdgix5pn.int
p-n formalism
```

The official interaction name for this local file is `SDPFSDG-MU`; `GCLSTsdpfsdgix5pn.snt` is the local KSHELL filename. No paper title, DOI, author list, or public download URL is included in the local header. The exact provenance of the local filename is therefore not established here. The interaction is documented as an `sd-pf-sdg` file connected to the SDPFSDG-MU / monopole-based-universal interaction family by name, model-space content, and local KSHELL usage.

## Interaction Construction

Dahl et al., Phys. Rev. C 113, 024328 (2026), identifies `SDPFSDG-MU` as the effective interaction used for the full `sd-pf-sdg` valence shell. In that paper, `SDPFSDG-MU` is described as being built from:

- the USD interaction for the `sd`-shell part,
- the GXPF1B interaction for the `pf`-shell part,
- a variant of the VMU interaction, as used in SDPF-MU, for the remaining cross-shell and upper-shell parts,
- a few two-body matrix-element modifications made in the same way as in SDPF-MU.

The paper cites Yoshida, Utsuno, Shimizu, and Otsuka, Phys. Rev. C 97, 054321 (2018), as the SDPFSDG-MU interaction reference. It also notes that, for `50V`, the Fermi surface lies in the `pf` shell, making the `pf`-shell component especially important.

For the `50V` application, the `16O` core gives 15 valence protons and 19 valence neutrons. The calculation uses the full `sd-pf-sdg` valence shell with a `1 hbar omega` truncation: one nucleon may cross one major-shell gap (`sd` to `pf`, or `pf` to `sdg`) at a time, while multiple cross-shell excitations and jumps across two major-shell gaps are excluded. Within that truncation, the paper states that there are no further orbital-specific truncations, so the full set of `0 hbar omega` and `1 hbar omega` basis states is allowed.

The same paper emphasizes two practical consequences of the `sd-pf-sdg` space. First, the `1 hbar omega` space is needed for a consistent calculation of E1 strengths together with M1 strengths. Second, including the `sdg` shell helps reduce center-of-mass contamination compared with an `sd-pf` space alone, because the three-shell space covers the full `1 hbar omega` basis needed to separate physical and spurious components.

## Notes

The raw KSHELL interaction file is not included in this repository.

The file is large: the local copy has `18,227` lines and `18,170` two-body matrix-element rows. This README records the orbital space and public literature context, but not the raw TBMEs.

Local source checksum:

```text
fb86da67c555267502f25a5d38a3152d5573d44e  GCLSTsdpfsdgix5pn.snt
```

## Relevant Literature

- J. K. Dahl, A. C. Larsen, N. Shimizu, and Y. Utsuno, "Microscopic study of the low-energy enhancement in the gamma-decay strength of 50V," Phys. Rev. C 113, 024328 (2026). Application of SDPFSDG-MU to large-scale `sd-pf-sdg` calculations of dipole strength functions in `50V`. DOI: [10.1103/csx6-6g5k](https://doi.org/10.1103/csx6-6g5k)
- S. Yoshida, Y. Utsuno, N. Shimizu, and T. Otsuka, "Systematic shell-model study of beta-decay properties and Gamow-Teller strength distributions in A ~= 40 neutron-rich nuclei," Phys. Rev. C 97, 054321 (2018). Interaction reference cited by Dahl et al. for SDPFSDG-MU. DOI: [10.1103/PhysRevC.97.054321](https://doi.org/10.1103/PhysRevC.97.054321)
- Y. Utsuno, T. Otsuka, B. A. Brown, M. Honma, T. Mizusaki, and N. Shimizu, "Shape transitions in exotic Si and S isotopes and tensor-force-driven Jahn-Teller effect," Phys. Rev. C 86, 051301(R) (2012). Origin/reference paper for the related SDPF-MU interaction in the `sd-pf` space. DOI: [10.1103/PhysRevC.86.051301](https://doi.org/10.1103/PhysRevC.86.051301)
- T. Otsuka, T. Suzuki, M. Honma, Y. Utsuno, N. Tsunoda, K. Tsukiyama, and M. Hjorth-Jensen, "Novel Features of Nuclear Forces and Shell Evolution in Exotic Nuclei," Phys. Rev. Lett. 104, 012501 (2010). Reference for the monopole-based universal interaction used in SDPF-MU-style developments. DOI: [10.1103/PhysRevLett.104.012501](https://doi.org/10.1103/PhysRevLett.104.012501)
- M. Honma, T. Otsuka, B. A. Brown, and T. Mizusaki, "New effective interaction for pf-shell nuclei and its implications for the stability of the N = Z = 28 closed core," Phys. Rev. C 69, 034335 (2004). GXPF1/GXPF-family reference; Dahl et al. state that SDPFSDG-MU uses GXPF1B for the `pf`-shell part. DOI: [10.1103/PhysRevC.69.034335](https://doi.org/10.1103/PhysRevC.69.034335)
- B. A. Brown and B. H. Wildenthal, "Status of the Nuclear Shell Model," Annu. Rev. Nucl. Part. Sci. 38, 29-66 (1988). USD-family reference; Dahl et al. state that SDPFSDG-MU uses USD for the `sd`-shell part. DOI: [10.1146/annurev.ns.38.120188.000333](https://doi.org/10.1146/annurev.ns.38.120188.000333)
- Y. Utsuno, T. Otsuka, T. Mizusaki, and M. Honma, "Varying shell gap and deformation in N ~ 20 unstable nuclei studied by the Monte Carlo shell model," Phys. Rev. C 60, 054315 (1999). Origin/reference paper for the older SDPF-M interaction. DOI: [10.1103/PhysRevC.60.054315](https://doi.org/10.1103/PhysRevC.60.054315)

## Files

No raw interaction file is included.

## Citation

For calculations using this exact local file, record the official interaction name `SDPFSDG-MU`, the local filename, local checksum, and the fact that the raw interaction file is restricted. Until the exact file-label provenance is resolved, cite the relevant SDPFSDG-MU / VMU literature above rather than treating this README as an origin reference.
