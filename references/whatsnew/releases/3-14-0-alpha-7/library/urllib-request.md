# Python 3.14.0 alpha 7 / library / urllib request

[gh-125866](https://github.com/python/cpython/issues/125866): The `nturl2path` module is now deprecated. Reach for [`urllib.request.url2pathname()`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.url2pathname) and [`pathname2url()`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.pathname2url) instead.

[gh-126367](https://github.com/python/cpython/issues/126367): Repaired a case where [`urllib.request.url2pathname()`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.url2pathname) threw [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) for a Windows URI bearing a colon character that did not follow a drive letter — such as the one preceding an NTFS alternate data stream.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
