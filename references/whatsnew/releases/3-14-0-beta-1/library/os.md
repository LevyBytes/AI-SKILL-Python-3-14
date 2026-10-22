# Python 3.14.0 beta 1 / library / os

[gh-81793](https://github.com/python/cpython/issues/81793): Repair [`os.link()`](https://docs.python.org/3.14/library/os.html#os.link) on those platforms (Linux among them) whose system `link()` function does not chase symlinks. Under Linux it now follows symlinks by default or whenever `follow_symlinks=True` is given. Under Windows it now errors out if `follow_symlinks=True` is supplied. Under macOS it now errors if `follow_symlinks=False` is given and the system `linkat()` function is unavailable at runtime.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
