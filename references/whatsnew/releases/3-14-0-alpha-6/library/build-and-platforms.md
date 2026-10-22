# Python 3.14.0 alpha 6 / library / build and platforms

[gh-130940](https://github.com/python/cpython/issues/130940): `PyConfig.use_system_logger` had its behavior changed so it now defaults to on under iOS. Under macOS it stays off by default.

[gh-124096](https://github.com/python/cpython/issues/124096): On the Windows console, the REPL now switches on virtual terminal mode and turns on bracketed paste. (Where the terminal lacks bracketed paste support, switching it on has no effect.)

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
