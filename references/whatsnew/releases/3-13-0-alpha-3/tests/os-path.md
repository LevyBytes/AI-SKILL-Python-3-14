# Python 3.13.0 alpha 3 / tests / os path

[gh-44626](https://github.com/python/cpython/issues/44626): Stop [`os.path.isabs()`](https://docs.python.org/3.14/library/os.path.html#os.path.isabs) from wrongly answering `True` on Windows for a path led by precisely one (back)slash.

Stop `pathlib.PureWindowsPath.is_absolute()` from wrongly answering `False` on certain paths that open with two (back)slashes.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
