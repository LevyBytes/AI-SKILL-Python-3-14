# Python 3.14.0 alpha 5 / library / pathlib

[gh-125413](https://github.com/python/cpython/issues/125413): Introduce the [`pathlib.Path.info`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.info) attribute, which holds an object that implements the (also new) [`pathlib.types.PathInfo`](https://docs.python.org/3.14/library/pathlib.html#pathlib.types.PathInfo) protocol. That object lets you query the file type and caches [`stat()`](https://docs.python.org/3.14/library/os.html#os.stat) results internally. Path objects produced by [`iterdir()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.iterdir) arrive with file type information picked up while scanning the parent directory.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
