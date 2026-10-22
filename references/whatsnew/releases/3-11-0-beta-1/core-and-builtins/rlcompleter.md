# Python 3.11.0 beta 1 / core and builtins / rlcompleter

[gh-92345](https://github.com/python/cpython/issues/92345): `pymain_run_python()` will now import `readline` and `rlcompleter` ahead of sys.path being extended with an interactive interpreter's current working directory. Interpreters running non-interactively see no change.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
