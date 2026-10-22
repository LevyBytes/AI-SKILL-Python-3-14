# Python 3.14.6 final / library / exceptions and tracebacks

[gh-112821](https://github.com/python/cpython/issues/112821): Within the REPL, autocompletion could end up executing arbitrary code inside a descriptor’s getter. Should that getter throw an exception, autocompletion would then fail to surface any options across the whole object. Autocompletion now behaves correctly for such objects.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
