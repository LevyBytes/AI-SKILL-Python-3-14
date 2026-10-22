# Python 3.13.0 alpha 2 / c api / threads and concurrency

[gh-111569](https://github.com/python/cpython/issues/111569): The "Python Critical Sections" described by [**PEP 703**](https://peps.python.org/pep-0703/) are now implemented. They are macros that assist in swapping the GIL for per-object locks within the `--disable-gil` build of CPython, and they compile to no-ops whenever the standard build is used.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
