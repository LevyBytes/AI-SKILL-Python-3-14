# warnings — Repeated Warning Suppression Criteria

### Repeated Warning Suppression Criteria

When deciding whether a warning counts as a repeat, the filters that suppress repeated warnings use these criteria:

- `"default"`: the warning counts as a repeat only when (*message*, *category*, *module*, *lineno*) all match.

- `"module"`: the warning counts as a repeat when (*message*, *category*, *module*) match, with the line number disregarded.

- `"once"`: the warning counts as a repeat when (*message*, *category*) match, with both module and line number disregarded.

[Subject index](INDEX.md) · [Previous](the-warnings-filter.md) · [Continue](describing-warning-filters.md) · [Owning module, declaration or section: warnings](warnings-warning-control.md)
