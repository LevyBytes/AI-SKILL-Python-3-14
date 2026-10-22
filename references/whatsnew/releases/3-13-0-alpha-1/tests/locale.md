# Python 3.13.0 alpha 1 / tests / locale

[gh-101634](https://github.com/python/cpython/issues/101634): Whenever the Python test suite runs with the `-jN` option, should a worker stdout resist decoding from the locale encoding, report a failed testn so that the exitcode lands non-zero. Victor Stinner authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
