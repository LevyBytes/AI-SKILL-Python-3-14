# Python 3.14.3 final / library / argparse

[gh-112527](https://github.com/python/cpython/issues/112527): For required options, [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) help text is no longer appended with ` (default: None)`.

[gh-142346](https://github.com/python/cpython/issues/142346): Within [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse), usage formatting for mutually exclusive groups is corrected for the cases where positional arguments come first, or where other optional arguments come after or are interleaved.

[gh-142332](https://github.com/python/cpython/issues/142332): Correct usage formatting for positional arguments living inside mutually exclusive groups in [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse). in `argparse`.

[gh-75949](https://github.com/python/cpython/issues/75949): Keep the `|` separators intact in mutually exclusive [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) groups when the usage line has to wrap because of its length.

[gh-142267](https://github.com/python/cpython/issues/142267): Speed up [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) by caching the formatter that argument validation relies on.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
