# Python 3.12.0 beta 1 / build / imports and modules

[gh-103532](https://github.com/python/cpython/issues/103532): Neither the `_tkinter` module nor anything else still defines or relies on the `TKINTER_PROTECT_LOADTK` macro. That macro had only ever been defined when compiling against Tk 8.4.13 or earlier, yet anything older than Tk 8.5.12 stopped being supported back in [gh-91152](https://github.com/python/cpython/issues/91152).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
