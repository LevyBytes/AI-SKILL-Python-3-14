# Python 3.14.0 release candidate 2 / library / urllib request

[gh-137059](https://github.com/python/cpython/issues/137059): Correct how [`urllib.request.url2pathname()`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.url2pathname) treats file URLs carrying a Windows drive letter inside the URL authority. This addresses a regression that appeared in earlier pre-releases of Python 3.14.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
