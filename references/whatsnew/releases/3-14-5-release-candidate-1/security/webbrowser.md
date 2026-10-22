# Python 3.14.5 release candidate 1 / security / webbrowser

[gh-148169](https://github.com/python/cpython/issues/148169): In [`webbrowser`](https://docs.python.org/3.14/library/webbrowser.html#module-webbrowser), a loophole let any URL beginning with `%action` slip past the dash-prefix safety screen.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
