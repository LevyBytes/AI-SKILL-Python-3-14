# Python 3.14.0 beta 1 / library / webbrowser

[gh-113539](https://github.com/python/cpython/issues/113539): [`webbrowser`](https://docs.python.org/3.14/library/webbrowser.html#module-webbrowser): A name listed in the `BROWSER` environment variable may now point to a web browser that is already registered, rather than forcing a fresh browser command every time.

That means `BROWSER` can be set to one of the browsers macOS supports.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
