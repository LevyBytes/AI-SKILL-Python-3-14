# Python 3.14.0 alpha 4 / library / faulthandler

[gh-128400](https://github.com/python/cpython/issues/128400): To head off races, [`faulthandler`](https://docs.python.org/3.14/library/faulthandler.html#module-faulthandler) now reports only the current thread under the [free threaded](https://docs.python.org/3.14/glossary.html#term-free-threading) build.

[gh-128400](https://github.com/python/cpython/issues/128400): Resolved a crash that occurred when [`faulthandler.dump_traceback()`](https://docs.python.org/3.14/library/faulthandler.html#faulthandler.dump_traceback) ran while other threads stayed active under the [free threaded](https://docs.python.org/3.14/glossary.html#term-free-threading) build.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
