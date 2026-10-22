# 4.12.6. Dry run

### 4.12.6. Dry run

Setting the environment variable `PYLAUNCHER_DRYRUN` (to any value) makes the launcher print the command it would otherwise have run, while never actually starting Python. That can come in useful for tools wanting to use the launcher to detect Python and then launch it directly. Note that the command written to standard output is always encoded in UTF-8 and may not display correctly in the console.

[Subject index](INDEX.md) · [Previous source section](diagnostics.md) · [Following source section](install-on-demand.md)
