# Python 3.14.0 alpha 1 / library / zipfile

[gh-122905](https://github.com/python/cpython/issues/122905): [`zipfile.Path`](https://docs.python.org/3.14/library/zipfile.html#zipfile.Path) instances now clean up names taken from the zipfile.

[gh-123270](https://github.com/python/cpython/issues/123270): A more targeted fix is now applied for malformed payloads in [`zipfile.Path`](https://docs.python.org/3.14/library/zipfile.html#zipfile.Path) that trigger infinite loops ([gh-122905](https://github.com/python/cpython/issues/122905)), and it does so without harming contents that use legitimate characters.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
