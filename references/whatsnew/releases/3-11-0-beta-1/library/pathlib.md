# Python 3.11.0 beta 1 / library / pathlib

[bpo-22276](https://bugs.python.org/issue?@action=redirect&bpo=22276): The [`Path`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path) methods [`glob()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.glob) and [`rglob()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.rglob) hand back only directories when *pattern* finishes with a pathname components separator (`/` or [`sep`](https://docs.python.org/3.14/library/os.html#os.sep)). Eisuke Kawashima authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
