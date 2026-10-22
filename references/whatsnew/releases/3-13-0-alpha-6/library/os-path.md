# Python 3.13.0 alpha 6 / library / os path

[gh-114847](https://github.com/python/cpython/issues/114847): Make [`os.path.realpath()`](https://docs.python.org/3.14/library/os.path.html#os.path.realpath) faster on platforms other than Windows.

[gh-117114](https://github.com/python/cpython/issues/117114): Offer [`os.path.isdevdrive()`](https://docs.python.org/3.14/library/os.path.html#os.path.isdevdrive) across every platform. Where Dev Drives are unavailable, it simply returns `False`.

[gh-117648](https://github.com/python/cpython/issues/117648): Make [`os.path.join()`](https://docs.python.org/3.14/library/os.path.html#os.path.join) together with [`os.path.expanduser()`](https://docs.python.org/3.14/library/os.path.html#os.path.expanduser) run faster.

[gh-117584](https://github.com/python/cpython/issues/117584): Have [`posixpath.relpath`](https://docs.python.org/3.14/library/os.path.html#os.path.relpath) throw [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) when handed something that is not a path.

[gh-117349](https://github.com/python/cpython/issues/117349): Tune several [`os.path`](https://docs.python.org/3.14/library/os.path.html#module-os.path) functions for speed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
