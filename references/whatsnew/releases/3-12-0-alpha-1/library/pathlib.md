# Python 3.12.0 alpha 1 / library / pathlib

[gh-94909](https://github.com/python/cpython/issues/94909): Faulty joining of relative Windows paths that carry drives within the [`pathlib.PurePath`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath) initializer is corrected.

[gh-92675](https://github.com/python/cpython/issues/92675): Adjust `venv.ensure_directories()` so it takes [`pathlib.Path`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path) arguments as well as [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) paths. David Foster supplied the patch.

[gh-93156](https://github.com/python/cpython/issues/93156): Indexing the [`pathlib.PurePath.parents`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.parents) sequence of an absolute path with negative indices used to return wrong results.

[gh-90385](https://github.com/python/cpython/issues/90385): Add [`pathlib.Path.walk()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.walk) to serve as an alternative to [`os.walk()`](https://docs.python.org/3.14/library/os.html#os.walk).

[gh-92550](https://github.com/python/cpython/issues/92550): Repair [`pathlib.Path.rglob()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.rglob) when handed an empty pattern.

[gh-84131](https://github.com/python/cpython/issues/84131): The deprecated `link_to` method on [`pathlib.Path`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path) is gone. Switch to the 3.10 [`hardlink_to()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.hardlink_to) method, whose semantics line up with those of [`symlink_to()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.symlink_to).

[bpo-42777](https://bugs.python.org/issue?@action=redirect&bpo=42777): Provide an implementation of [`pathlib.Path.is_mount()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.is_mount) covering Windows paths.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
