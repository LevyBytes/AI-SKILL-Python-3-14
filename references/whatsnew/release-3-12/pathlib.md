# What’s New In Python 3.12 / pathlib — os, os.path, pathlib

### pathlib

- Add the ability to subclass [`pathlib.PurePath`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath) and [`pathlib.Path`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path), as well as their Posix- and Windows-specific flavors. A subclass may override the [`pathlib.PurePath.with_segments()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.with_segments) method to carry data across path instances.

- Add [`pathlib.Path.walk()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.walk) to traverse directory trees and yield each file or directory name found inside them, much like [`os.walk()`](https://docs.python.org/3.14/library/os.html#os.walk). (Contributed by Stanislav Zmiev in [gh-90385](https://github.com/python/cpython/issues/90385).)

- Add an optional *walk_up* parameter to [`pathlib.PurePath.relative_to()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.relative_to) so `..` entries can appear in the outcome; this lines up better with [`os.path.relpath()`](https://docs.python.org/3.14/library/os.path.html#os.path.relpath). (Contributed by Domenico Ragusa in [gh-84538](https://github.com/python/cpython/issues/84538).)

- Add [`pathlib.Path.is_junction()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.is_junction) acting as a proxy onto [`os.path.isjunction()`](https://docs.python.org/3.14/library/os.path.html#os.path.isjunction). (Contributed by Charles Machalow in [gh-99547](https://github.com/python/cpython/issues/99547).)

- Add an optional *case_sensitive* parameter to [`pathlib.Path.glob()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.glob), [`pathlib.Path.rglob()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.rglob) and [`pathlib.PurePath.match()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.match) to set the path’s case sensitivity, giving finer command over how matching proceeds.

[Subject index](INDEX.md) · [Previous source section](os-path.md) · [Next source section](platform.md) · [Release/subject declaration](summary-release-highlights.md)
