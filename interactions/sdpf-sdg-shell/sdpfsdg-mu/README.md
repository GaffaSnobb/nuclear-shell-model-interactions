# SDPFSDG-MU

`SDPFSDG-MU` is a restricted local KSHELL-format interaction for a large `sd-pf-sdg` valence space above a `16O` core. The raw `.snt` file is intentionally not included in this repository.

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

The official interaction name for this local file is `SDPFSDG-MU`; `GCLSTsdpfsdgix5pn.snt` is the restricted local KSHELL filename. No paper title, DOI, author list, or public download URL is included in the local header. The exact provenance of the local filename is therefore not established here. The interaction is documented as a restricted local `sd-pf-sdg` file connected to the SDPFSDG-MU / monopole-based-universal interaction family by name, model-space content, and local KSHELL usage.

## Notes

This entry intentionally does not include `files/kshell/GCLSTsdpfsdgix5pn.snt`. The filename is also listed in `.gitignore` to reduce the chance of accidental publication.

The file is large: the local copy has `18,227` lines and `18,170` two-body matrix-element rows. This README records the orbital space and public literature context, but not the raw TBMEs.

Local source checksum:

```text
fb86da67c555267502f25a5d38a3152d5573d44e  GCLSTsdpfsdgix5pn.snt
```

## Relevant Literature

- Y. Utsuno, T. Otsuka, B. A. Brown, M. Honma, T. Mizusaki, and N. Shimizu, "Shape transitions in exotic Si and S isotopes and tensor-force-driven Jahn-Teller effect," Phys. Rev. C 86, 051301(R) (2012). Origin/reference paper for the related SDPF-MU interaction in the `sd-pf` space. DOI: [10.1103/PhysRevC.86.051301](https://doi.org/10.1103/PhysRevC.86.051301)
- T. Otsuka, T. Suzuki, M. Honma, Y. Utsuno, N. Tsunoda, K. Tsukiyama, and M. Hjorth-Jensen, "Novel Features of Nuclear Forces and Shell Evolution in Exotic Nuclei," Phys. Rev. Lett. 104, 012501 (2010). Reference for the monopole-based universal interaction used in SDPF-MU-style developments. DOI: [10.1103/PhysRevLett.104.012501](https://doi.org/10.1103/PhysRevLett.104.012501)
- Y. Utsuno, T. Otsuka, T. Mizusaki, and M. Honma, "Varying shell gap and deformation in N ~ 20 unstable nuclei studied by the Monte Carlo shell model," Phys. Rev. C 60, 054315 (1999). Origin/reference paper for the older SDPF-M interaction. DOI: [10.1103/PhysRevC.60.054315](https://doi.org/10.1103/PhysRevC.60.054315)

## Files

No raw interaction file is included. The restricted local source is `/Applications/kshell/snt/GCLSTsdpfsdgix5pn.snt`.

## Citation

For calculations using this exact local file, record the official interaction name `SDPFSDG-MU`, the local filename, local checksum, and the fact that the raw interaction file is restricted. Until the exact file-label provenance is resolved, cite the relevant SDPFSDG-MU / VMU literature above rather than treating this README as an origin reference.
