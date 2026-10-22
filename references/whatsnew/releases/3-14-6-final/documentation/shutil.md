# Python 3.14.6 final / documentation / shutil

[gh-109503](https://github.com/python/cpython/issues/109503): Repair the documentation covering [`shutil.move()`](https://docs.python.org/3.14/library/shutil.html#shutil.move) regarding its use of [`os.rename()`](https://docs.python.org/3.14/library/os.html#os.rename), given that a nonatomic move may occur even where the files share one filesystem. Fang Li authored the change

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
