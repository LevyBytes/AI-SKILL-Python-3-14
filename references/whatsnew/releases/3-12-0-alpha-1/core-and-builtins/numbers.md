# Python 3.12.0 alpha 1 / core and builtins / numbers

[gh-93516](https://github.com/python/cpython/issues/93516): Builds, on demand, a table linking bytecode offsets to line numbers so that line numbers compute faster during tracing.

[gh-88116](https://github.com/python/cpython/issues/88116): Resolves a case while pulling line numbers out of code objects whenever the encoded line numbers sit near `INT_MIN`. Pablo Galindo wrote the patch

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
