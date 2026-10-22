# What's New In Python 3.13 / io — devmode, io, sys

### io

- When the [`IOBase`](https://docs.python.org/3.14/library/io.html#io.IOBase) finalizer runs, any exception thrown by [`close()`](https://docs.python.org/3.14/library/io.html#io.IOBase.close) is now reported through [`sys.unraisablehook`](https://docs.python.org/3.14/library/sys.html#sys.unraisablehook). Earlier behavior dropped such errors quietly unless you ran under [Python Development Mode](https://docs.python.org/3.14/library/devmode.html#devmode) or a [Python debug build](https://docs.python.org/3.14/using/configure.html#debug-build). (Contributed by Victor Stinner in [gh-62948](https://github.com/python/cpython/issues/62948).)

[Subject index](INDEX.md) · [Previous source section](importlib.md) · [Next source section](ipaddress.md) · [Release/subject declaration](summary-release-highlights.md)
