# Python 3.13.0 beta 1 / build / build and platforms

[gh-118734](https://github.com/python/cpython/issues/118734): Repairs the Windows build when it runs directly (rather than via the `build.bat` script) and no value is given for `UseTIER2`.

[gh-115119](https://github.com/python/cpython/issues/115119): The `configure` option [`--with-system-libmpdec`](https://docs.python.org/3.14/using/configure.html#cmdoption-with-system-libmpdec) now defaults to `yes`. Python 3.15 will drop the bundled copy of `libmpdecimal`.

[gh-117845](https://github.com/python/cpython/issues/117845): Fixes building against newer libedit releases by having **configure** detect the readline hook signatures.

[gh-116622](https://github.com/python/cpython/issues/116622): A testbed project arrived for running the test suite on Android.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
