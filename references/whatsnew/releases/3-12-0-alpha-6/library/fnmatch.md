# Python 3.12.0 alpha 6 / library / fnmatch

[gh-101360](https://github.com/python/cpython/issues/101360): Correct anchor matching within `pathlib.PureWindowsPath.match()`. Both path and pattern anchors now go through [`fnmatch`](https://docs.python.org/3.14/library/fnmatch.html#module-fnmatch), the same as any other path part. That makes patterns like `"*:/Users/*"` matchable.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
