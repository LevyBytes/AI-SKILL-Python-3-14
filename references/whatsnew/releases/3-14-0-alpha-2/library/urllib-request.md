# Python 3.14.0 alpha 2 / library / urllib request

[gh-84850](https://github.com/python/cpython/issues/84850): Drop the `URLopener` together with `FancyURLopener` classes out of [`urllib.request`](https://docs.python.org/3.14/library/urllib.request.html#module-urllib.request). Since Python 3.3 they had been emitting [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning).

[gh-126212](https://github.com/python/cpython/issues/126212): Correct a problem where [`urllib.request.pathname2url()`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.pathname2url) along with [`url2pathname()`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.url2pathname) stripped slashes out of Windows DOS drive paths together with URLs.

[gh-126205](https://github.com/python/cpython/issues/126205): Correct a problem where [`urllib.request.pathname2url()`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.pathname2url) produced URLs starting with four slashes (instead of two) for a supplied Windows UNC path.

[gh-126766](https://github.com/python/cpython/issues/126766): Correct the case where [`urllib.request.url2pathname()`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.url2pathname) neglected to strip two leading slashes that brought in an empty authority section.

[gh-120423](https://github.com/python/cpython/issues/120423): Correct the case where [`urllib.request.pathname2url()`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.pathname2url) handled Windows paths containing embedded forward slashes incorrectly.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
