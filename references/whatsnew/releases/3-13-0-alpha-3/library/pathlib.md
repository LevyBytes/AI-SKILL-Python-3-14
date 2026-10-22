# Python 3.13.0 alpha 3 / library / pathlib

[gh-113568](https://github.com/python/cpython/issues/113568): Raise audit events out of [`pathlib.Path`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path) instead of its private base class `PathBase`.

[gh-113225](https://github.com/python/cpython/issues/113225): Made [`pathlib.Path.glob()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.glob) faster by leaning on [`os.DirEntry.path`](https://docs.python.org/3.14/library/os.html#os.DirEntry.path) wherever feasible.

[gh-112405](https://github.com/python/cpython/issues/112405): Tune [`pathlib.PurePath.relative_to()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.relative_to) for speed. Alex Waygood wrote the patch.

[gh-112361](https://github.com/python/cpython/issues/112361): Make a few [`pathlib`](https://docs.python.org/3.14/library/pathlib.html#module-pathlib) methods quicker by discarding several temporary objects.

[gh-77621](https://github.com/python/cpython/issues/77621): Trim the import time of the [`pathlib`](https://docs.python.org/3.14/library/pathlib.html#module-pathlib) module a little by postponing several imports. Barney Gale wrote the patch.

[gh-113568](https://github.com/python/cpython/issues/113568): Emit deprecation warnings out of [`pathlib.PurePath`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath) instead of its private base class `PurePathBase`.

[gh-112727](https://github.com/python/cpython/issues/112727): Accelerate [`pathlib.Path.absolute()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.absolute). Barney Gale wrote the patch.

[gh-110109](https://github.com/python/cpython/issues/110109): Introduce a private `pathlib._PurePathBase` class — a base for [`pathlib.PurePath`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath) that leaves out some magic methods. It (along with `_PathBase`) could become public down the road.

[gh-103363](https://github.com/python/cpython/issues/103363): Introduce a *follow_symlinks* keyword-only argument on [`pathlib.Path.owner()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.owner) and [`group()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.group), with a default of `True`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
