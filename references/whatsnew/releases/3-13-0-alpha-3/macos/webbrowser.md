# Python 3.13.0 alpha 3 / macos / webbrowser

[gh-87277](https://github.com/python/cpython/issues/87277): webbrowser: Skip the hunt for X11 browsers under macOS. They see little use there, and probing them can launch XQuartz even when nothing else needs it.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
