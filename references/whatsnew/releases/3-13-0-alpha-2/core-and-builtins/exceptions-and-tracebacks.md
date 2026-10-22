# Python 3.13.0 alpha 2 / core and builtins / exceptions and tracebacks

[gh-79932](https://github.com/python/cpython/issues/79932): Throw an exception should [`frame.clear()`](https://docs.python.org/3.14/reference/datamodel.html#frame.clear) run against a suspended frame.

[gh-109181](https://github.com/python/cpython/issues/109181): Make `Traceback` object creation quicker by deferring the line number computation. Pablo Galindo wrote the patch

[gh-67224](https://github.com/python/cpython/issues/67224): Display source lines in tracebacks for the `-c` option when Python is run. Pablo Galindo wrote the patch

[gh-110892](https://github.com/python/cpython/issues/110892): Hand back `NULL` for `PyTrace_RETURN` events triggered by an exception

[gh-110805](https://github.com/python/cpython/issues/110805): Let the repl present source code along with full tracebacks. Pablo Galindo wrote the patch

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
