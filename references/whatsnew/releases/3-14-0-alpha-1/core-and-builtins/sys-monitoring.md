# Python 3.14.0 alpha 1 / core and builtins / sys monitoring

[gh-122821](https://github.com/python/cpython/issues/122821): Guarantee that branches inside [`while`](https://docs.python.org/3.14/reference/compound_stmts.html#while) statements carry consistent offsets for [`sys.monitoring`](https://docs.python.org/3.14/library/sys.monitoring.html#module-sys.monitoring). A `while` statement now compiles to a plain jump after the body instead of repeating the test.

[gh-116090](https://github.com/python/cpython/issues/116090): Correct a JIT-build problem that kept certain [`for`](https://docs.python.org/3.14/reference/compound_stmts.html#for) loops from firing [`RAISE`](https://docs.python.org/3.14/library/sys.monitoring.html#monitoring-event-RAISE) monitoring events as they should.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
