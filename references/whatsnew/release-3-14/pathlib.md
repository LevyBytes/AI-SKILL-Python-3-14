# What's new in Python 3.14 / pathlib — os, pathlib

### pathlib

- Add methods to [`pathlib.Path`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path) for recursively copying or relocating files and directories:

  - [`copy()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.copy) copies a file or directory tree to a destination.

  - [`copy_into()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.copy_into) copies *into* a destination directory.

  - [`move()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.move) moves a file or directory tree to a destination.

  - [`move_into()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.move_into) moves *into* a destination directory.

(Contributed by Barney Gale in [gh-73991](https://github.com/python/cpython/issues/73991).)

- Add the [`info`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.info) attribute, holding an object that implements the freshly added [`pathlib.types.PathInfo`](https://docs.python.org/3.14/library/pathlib.html#pathlib.types.PathInfo) protocol. That object lets you query the file type while caching [`stat()`](https://docs.python.org/3.14/library/os.html#os.stat) results internally. Path objects produced by [`iterdir()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.iterdir) start out carrying file-type information drawn from scanning the parent directory. (Contributed by Barney Gale in [gh-125413](https://github.com/python/cpython/issues/125413).)

### pathlib

- [`Path.read_bytes`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.read_bytes) now opens files in unbuffered mode, making a full read between 9% and 17% faster. (Contributed by Cody Maloney in [gh-120754](https://github.com/python/cpython/issues/120754).)

### pathlib

- You can no longer hand extra keyword arguments to [`Path`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path). Earlier releases simply discarded anything like that. (Contributed by Barney Gale in [gh-74033](https://github.com/python/cpython/issues/74033).)

- Extra positional arguments are no longer accepted by [`PurePath.relative_to()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.relative_to) or [`is_relative_to()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.is_relative_to). Earlier releases would append anything like that onto *other*. (Contributed by Barney Gale in [gh-78707](https://github.com/python/cpython/issues/78707).)

[Subject index](INDEX.md) · [Previous source section](os-path.md) · [Next source section](pdb.md) · [Release/subject declaration](summary-release-highlights.md) · [Previous source section](io.md) · [Previous source section](itertools.md) · [Next source section](pkgutil.md)
