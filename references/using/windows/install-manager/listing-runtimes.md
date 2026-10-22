# 4.1.4. Listing runtimes

### 4.1.4. Listing runtimes

```none
$> py list [-f=|--format=<FMT>] [-1|--one] [--online|-s=|--source=<URL>] [<TAG>...]

```

You can view the list of installed runtimes via `py list`. You may attach a filter consisting of one or more tags (with or without a company specifier), and each may carry a `<`, `<=`, `>=` or `>` prefix to limit it to a range.

Several formats are available, passed through the `--format=<FMT>` or `-f <FMT>` option. Among them: `table` (a readable tabular display), `csv` (table in comma-separated form), `json` (one JSON blob covering all), `jsonl` (a JSON blob for each result), `exe` (the executable path alone), `prefix` (the prefix path alone).

With the `--one` or `-1` option only one result appears. When the default runtime is among them, it becomes the one shown. Otherwise the "best" result appears ("best" is intentionally left loosely defined, but is generally the most recent version). What `py list --one <TAG>` shows will correspond to the runtime that `py -V:<TAG>` would launch.

The `--only-managed` option leaves out results that the Python install manager did not install. That helps when working out which runtimes can be updated or uninstalled via the `py` command.

The `--online` option is shorthand for giving `--source=<URL>` with the default source. Either of these options will query the online index for runtimes that are available to install. What `py list --online --one <TAG>` shows will correspond to the runtime that `py install <TAG>` would install.

```none
$> py list --online 3.14

```

To remain compatible with the old launcher, the `--list`, `--list-paths`, `-0` and `-0p` commands (for example `py -0p`) are kept. They accept no extra options and emit legacy formatted output.

[Subject index](INDEX.md) · [Previous source section](command-help.md) · [Following source section](installing-runtimes.md)
