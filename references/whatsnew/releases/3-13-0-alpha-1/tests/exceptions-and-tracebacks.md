# Python 3.13.0 alpha 1 / tests / exceptions and tracebacks

[gh-104736](https://github.com/python/cpython/issues/104736): Repaired test_gdb on Python compiled via LLVM clang 16 on Linux ppc64le (e.g. Fedora 38). Look for patterns within the gdb ?bt? command output to spot when gdb cannot recover the traceback. As one example, omit a test once `Backtrace stopped: frame did not save the PC` shows up. Victor Stinner authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
