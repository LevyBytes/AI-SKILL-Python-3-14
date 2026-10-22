# Python 3.12.0 beta 1 / library / zipfile

[gh-92184](https://github.com/python/cpython/issues/92184): While building zip archives through [`zipfile`](https://docs.python.org/3.14/library/zipfile.html#module-zipfile), a non-`None` value of `os.altsep` is now consistently honored as a path separator, even in cases where it differs from `/`. Carey Metcalfe wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
