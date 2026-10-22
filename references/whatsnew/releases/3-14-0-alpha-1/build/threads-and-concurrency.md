# Python 3.14.0 alpha 1 / build / threads and concurrency

[gh-124043](https://github.com/python/cpython/issues/124043): A build with [`--with-trace-refs`](https://docs.python.org/3.14/using/configure.html#cmdoption-with-trace-refs) is for the moment rejected whenever the GIL has been turned off.

[gh-120326](https://github.com/python/cpython/issues/120326): On Windows, repair the build failure triggered by pairing the `--disable-gil` and `--experimental-jit` options together.

[gh-118943](https://github.com/python/cpython/issues/118943): Close a potential race condition in parallel builds set up with `--enable-experimental-jit`, where an incompletely-generated header file could produce compilation errors.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
