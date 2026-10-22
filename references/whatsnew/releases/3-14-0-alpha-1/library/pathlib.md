# Python 3.14.0 alpha 1 / library / pathlib

[gh-119113](https://github.com/python/cpython/issues/119113): Resolve the bug where [`pathlib.PurePath.with_suffix()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.with_suffix) failed to raise [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) when handed `None` as the suffix.

[gh-119518](https://github.com/python/cpython/issues/119518): Accelerates normalization for [`pathlib.PurePath`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath) and [`Path`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path) objects by skipping the interning of string parts.

[gh-73991](https://github.com/python/cpython/issues/73991): Adds [`pathlib.Path.copy_into()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.copy_into) plus [`move_into()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.move_into), which copy and relocate files and directories into directories that already *exist*.

[gh-73991](https://github.com/python/cpython/issues/73991): Introduce [`pathlib.Path.move()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.move) for relocating a file or an entire directory tree.

[gh-74033](https://github.com/python/cpython/issues/74033): Passing keyword arguments into [`pathlib.Path`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path) is no longer supported.

[gh-101357](https://github.com/python/cpython/issues/101357): Rather than catching only a handful of the more frequent errors, [`pathlib.Path.exists()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.exists) and the `is_*()` methods now swallow every [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError). This brings the behaviour in line with [`os.path.exists()`](https://docs.python.org/3.14/library/os.path.html#os.path.exists), [`os.path.isdir()`](https://docs.python.org/3.14/library/os.path.html#os.path.isdir), and so on. To fetch file status while letting exceptions propagate, turn to [`pathlib.Path.stat()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.stat).

[gh-78707](https://github.com/python/cpython/issues/78707): Supplying extra positional arguments to [`pathlib.PurePath.relative_to()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.relative_to) and [`is_relative_to()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.is_relative_to) is no longer allowed.

[gh-73991](https://github.com/python/cpython/issues/73991): Introduce [`pathlib.Path.copy()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.copy), which duplicates a file or directory into another location.

[gh-82805](https://github.com/python/cpython/issues/82805): Handle single-dot file extensions within [`pathlib.PurePath.suffix`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.suffix) plus its related attributes and methods. As an illustration, the [`suffixes`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.suffixes) of `PurePath('foo.bar.')` now come out as `['.bar', '.']` instead of `[]`. That aligns extension splitting with [`os.path.splitext()`](https://docs.python.org/3.14/library/os.path.html#os.path.splitext).

[gh-125069](https://github.com/python/cpython/issues/125069): Repair a problem where supplying a [`pathlib.PurePath`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath) object as an initializer argument to a second `PurePath` object carrying a different [`parser`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.parser) caused the arguments passed to the former object's initializer to be joined using the latter object's parser.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
