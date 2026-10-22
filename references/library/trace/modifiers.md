# trace — Modifiers

### Modifiers

 -f, --file=&lt;file&gt;

The name of a file in which to tally counts across multiple tracing runs. Pair it with the `--count` option.

 -C, --coverdir=&lt;dir&gt;

The directory the report files land in. For `package.module`, the coverage report ends up in the file `*dir*/*package*/*module*.cover`.

 -m, --missing

While building annotated listings, flag any line that never ran using `>>>>>>`.

 -s, --summary

With `--count` or `--report` in play, print a short summary to stdout covering every file handled.

 -R, --no-report

Skip producing annotated listings. That comes in handy when you plan several `--count` runs and want just one batch of annotated listings generated at the very end.

 -g, --timing

Stamp every line with how much time has passed since the program began. This applies only during tracing.

[Subject index](INDEX.md) · [Previous](main-options.md) · [Continue](filters.md) · [Owning module, declaration or section: trace](coverage-py.md)
