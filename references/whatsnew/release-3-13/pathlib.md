# What's New In Python 3.13 / pathlib — os.path, pathlib

### pathlib

- A new [`UnsupportedOperation`](https://docs.python.org/3.14/library/pathlib.html#pathlib.UnsupportedOperation) now surfaces, in place of [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError), whenever a path operation has no support. (Contributed by Barney Gale in [gh-89812](https://github.com/python/cpython/issues/89812).)

- A new constructor, [`Path.from_uri()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.from_uri), builds [`Path`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path) objects out of ?file? URIs (`file:///`). (Contributed by Barney Gale in [gh-107465](https://github.com/python/cpython/issues/107465).)

- A new [`PurePath.full_match()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.full_match) matches paths against shell-style wildcards, the recursive wildcard ?`**`? included. (Contributed by Barney Gale in [gh-73435](https://github.com/python/cpython/issues/73435).)

- A new [`PurePath.parser`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.parser) class attribute records which [`os.path`](https://docs.python.org/3.14/library/os.path.html#module-os.path) implementation drives low-level path parsing and joining. Its value is `posixpath` or `ntpath`.

- A *recurse_symlinks* keyword-only argument now joins [`Path.glob()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.glob) plus [`rglob()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.rglob). (Contributed by Barney Gale in [gh-77609](https://github.com/python/cpython/issues/77609).)

- When the supplied pattern closes with ?`**`?, [`Path.glob()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.glob) and [`rglob()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.rglob) now hand back both files and directories. Formerly the result held only directories. (Contributed by Barney Gale in [gh-70303](https://github.com/python/cpython/issues/70303).)

- A *follow_symlinks* keyword-only argument is now accepted by [`Path.is_file`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.is_file), [`Path.is_dir`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.is_dir), [`Path.owner()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.owner), and [`Path.group()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.group). (Contributed by Barney Gale in [gh-105793](https://github.com/python/cpython/issues/105793) and Kamil Turek in [gh-107962](https://github.com/python/cpython/issues/107962).)

### pathlib

- Drop the option to treat [`Path`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path) objects as context managers. The capability was deprecated and has done nothing as of Python 3.9. (Contributed by Barney Gale in [gh-83863](https://github.com/python/cpython/issues/83863).)

[Subject index](INDEX.md) · [Previous source section](os-path.md) · [Next source section](pdb.md) · [Release/subject declaration](summary-release-highlights.md) · [Previous source section](optparse.md) · [Next source section](re.md)
