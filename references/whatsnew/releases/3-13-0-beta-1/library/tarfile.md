# Python 3.13.0 beta 1 / library / tarfile

[gh-116931](https://github.com/python/cpython/issues/116931): Adds a check for the *fileobj* parameter to [`tarfile.TarFile.addfile()`](https://docs.python.org/3.14/library/tarfile.html#tarfile.TarFile.addfile)

[gh-117691](https://github.com/python/cpython/issues/117691): Sharpens the warning text produced by [`tarfile`](https://docs.python.org/3.14/library/tarfile.html#module-tarfile) deprecation notices tied to PEP 706. Should no `filter` argument be passed to `extract()` or `extractall`, the deprecation warning now indicates the line in the caller's source where the function was invoked. Alex Waygood supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
