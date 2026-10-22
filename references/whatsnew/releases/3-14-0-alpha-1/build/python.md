# Python 3.14.0 alpha 1 / build / python

[gh-120291](https://github.com/python/cpython/issues/120291): Make the `python-config` shell script work under shells other than bash.

[gh-119729](https://github.com/python/cpython/issues/119729): Under POSIX, the pkg-config (`.pc`) filenames now carry the ABI flags, among them debug ("d") and free-threaded ("t"). As examples: * `python-3.14.pc` (default, non-debug build) * `python-3.14d.pc` (default, debug build) * `python-3.14t.pc` (free-threaded build)

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
