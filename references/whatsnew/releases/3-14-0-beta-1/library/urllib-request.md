# Python 3.14.0 beta 1 / library / urllib request

[gh-126838](https://github.com/python/cpython/issues/126838): A *resolve_host* keyword-only parameter has been added to [`urllib.request.url2pathname()`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.url2pathname), and handling of file URLs that include authorities is fixed.

[gh-125866](https://github.com/python/cpython/issues/125866): Provide an optional *add_scheme* argument on [`urllib.request.pathname2url()`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.pathname2url); supplying true yields a full URL. In the same way add an optional *require_scheme* argument to [`url2pathname()`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.url2pathname); supplying true makes it accept a full URL.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
