# Python 3.14.1 final / library / mmap

[gh-138204](https://github.com/python/cpython/issues/138204): On Linux, growing a shared anonymous [`memory maps`](https://docs.python.org/3.14/library/mmap.html#module-mmap) is now disallowed, since doing so produced a bus error.

[gh-116738](https://github.com/python/cpython/issues/116738): Render [`mmap`](https://docs.python.org/3.14/library/mmap.html#module-mmap) thread-safe under the [free threaded](https://docs.python.org/3.14/glossary.html#term-free-threading) build.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
