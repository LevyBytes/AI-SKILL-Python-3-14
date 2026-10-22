# Python 3.12.0 alpha 6 / library / pathlib

[gh-101362](https://github.com/python/cpython/issues/101362): Make [`pathlib.Path`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path) construction faster by performing the path flavour compatibility check solely at the point pathlib is imported.

[gh-100809](https://github.com/python/cpython/issues/100809): Correct how drive-relative paths (such as ?C:? and ?C:foo?) are dealt with in [`pathlib.Path.absolute()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.absolute). The method now queries the OS API to fetch the right current working directory for that drive.

[gh-101362](https://github.com/python/cpython/issues/101362): Make [`pathlib.PurePath`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath) construction faster by treating arguments more consistently. Where a [`pathlib.Path`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path) argument is given, we take its string representation rather than stitching its parts together with [`os.path.join()`](https://docs.python.org/3.14/library/os.path.html#os.path.join).

[gh-101362](https://github.com/python/cpython/issues/101362): Make [`pathlib.PurePath`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath) construction faster by invoking [`os.path.join()`](https://docs.python.org/3.14/library/os.path.html#os.path.join) only once two or more arguments have been supplied.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
