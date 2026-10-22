# Python 3.14.1 final / library / concurrent interpreters

[gh-112729](https://github.com/python/cpython/issues/112729): Prevents a crash from calling [`concurrent.interpreters.create()`](https://docs.python.org/3.14/library/concurrent.interpreters.html#concurrent.interpreters.create) while the process has run out of memory.

[gh-135729](https://github.com/python/cpython/issues/135729): Resolves an unraisable exception thrown during finalization when [`concurrent.interpreters`](https://docs.python.org/3.14/library/concurrent.interpreters.html#module-concurrent.interpreters) is exercised in the REPL.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
