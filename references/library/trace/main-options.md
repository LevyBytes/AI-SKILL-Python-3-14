# trace - Main options

### Main options

You have to give at least one of the options below whenever you call `trace`. The `--listfuncs` option cannot be combined with the `--trace` and `--count` options. Supplying `--listfuncs` rules out both `--count` and `--trace`, and the reverse holds too.

 -c, --count

Once the program finishes, emit a batch of annotated listing files recording how often each statement ran. Consult `--coverdir`, `--file`, and `--no-report` further down as well.

 -t, --trace

Echo each line at the moment it runs.

 -l, --listfuncs

List which functions ran while the program executed.

 -r, --report

Build an annotated list out of a prior run that had used the `--count` and `--file` option. No code is run in the process.

 -T, --trackcalls

Show the call relationships that surface as the program runs.

[Subject index](INDEX.md) · [Previous](command-line-usage.md) · [Continue](modifiers.md) · [Owning module, declaration or section: trace](coverage-py.md)
