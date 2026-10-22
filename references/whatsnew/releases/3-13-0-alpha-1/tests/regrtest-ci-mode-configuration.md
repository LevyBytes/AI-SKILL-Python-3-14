# Python 3.13.0 alpha 1 / tests / regrtest whenever fast ci or slow ci option play regrtest swaps

[gh-109566](https://github.com/python/cpython/issues/109566): regrtest: Whenever the `--fast-ci` or `--slow-ci` option is in play, regrtest now swaps the running process for a fresh one so that the `-u -W default -bb -E` options get added to Python. Victor Stinner authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
