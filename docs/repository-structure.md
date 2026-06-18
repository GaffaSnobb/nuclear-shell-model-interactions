# Repository structure

Interactions are grouped primarily by the nuclear mass region or shell-model region they are used for. The inert core is recorded in each interaction's metadata instead of being the top-level grouping, because the core can be partly a bookkeeping convention.

The intended layout is:

```text
interactions/
  132sn-region/
    sn100pn/
      README.md
      metadata.yml
      notes.md
      files/
        kshell/
          sn100pn.snt
```

Only directories with actual content should be created. For example, if an interaction is only available in KSHELL format, create `files/kshell/` but do not create empty `nushellx/`, `oxbash/`, or `original/` directories.

Each interaction entry should contain:

- `README.md`: human-readable description, model space, provenance, and recommended citation.
- `metadata.yml`: structured facts such as region, core, valence space, source publication, DOI, and available file formats.
- `notes.md`: working notes, caveats, convention translations, and unresolved provenance questions.
- `files/kshell/`: KSHELL `.snt` files.

A top-level `index.md` gives a short table of all documented interactions.
