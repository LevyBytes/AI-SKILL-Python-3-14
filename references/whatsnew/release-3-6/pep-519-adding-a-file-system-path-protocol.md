# What's New In Python 3.6 / PEP 519: Adding a file system path protocol — os, os.path, pathlib

### PEP 519: Adding a file system path protocol

Traditionally a file system path was modeled as a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) or [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object. That history pushed authors of path-handling code to presume those objects could only ever be one of the two kinds (an [`int`](https://docs.python.org/3.14/library/functions.html#int) standing for a file descriptor is excluded since it is not a file path). Sadly such a presumption locks out other ways of representing file system paths, such as [`pathlib`](https://docs.python.org/3.14/library/pathlib.html#module-pathlib), from cooperating with existing code, Python's own standard library included.

The remedy is a new interface embodied by [`os.PathLike`](https://docs.python.org/3.14/library/os.html#os.PathLike). When an object supplies the [`__fspath__()`](https://docs.python.org/3.14/library/os.html#os.PathLike.__fspath__) method, it declares that it stands for a path. That object can then hand back a low-level rendering of its file system path as a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) or [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object. So an object counts as [path-like](https://docs.python.org/3.14/glossary.html#term-path-like-object) when it provides `os.PathLike`, or when it is a `str` or `bytes` object standing for a file system path. To pull a `str` and/or `bytes` rendering out of a path-like object explicitly, code can reach for [`os.fspath()`](https://docs.python.org/3.14/library/os.html#os.fspath), [`os.fsdecode()`](https://docs.python.org/3.14/library/os.html#os.fsdecode), or [`os.fsencode()`](https://docs.python.org/3.14/library/os.html#os.fsencode).

The built-in [`open()`](https://docs.python.org/3.14/library/functions.html#open) function now takes [`os.PathLike`](https://docs.python.org/3.14/library/os.html#os.PathLike) objects, and so do every pertinent function across the [`os`](https://docs.python.org/3.14/library/os.html#module-os) and [`os.path`](https://docs.python.org/3.14/library/os.path.html#module-os.path) modules, plus the bulk of the remaining functions and classes in the standard library. The [`os.DirEntry`](https://docs.python.org/3.14/library/os.html#os.DirEntry) class and the relevant [`pathlib`](https://docs.python.org/3.14/library/pathlib.html#module-pathlib) classes were likewise revised to provide `os.PathLike`.

The aspiration is that reworking the core path-handling functions will let third-party code embrace every [path-like objects](https://docs.python.org/3.14/glossary.html#term-path-like-object) automatically, with no edits or at most a tiny tweak (for instance a [`os.fspath()`](https://docs.python.org/3.14/library/os.html#os.fspath) call up front before the code touches a path-like object).

Below are a few illustrations of how this interface makes [`pathlib.Path`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path) slot more smoothly and seamlessly into existing code:

```python
>>> import pathlib
>>> with open(pathlib.Path("README")) as f:
...     contents = f.read()
...
>>> import os.path
>>> os.path.splitext(pathlib.Path("some_file.txt"))
('some_file', '.txt')
>>> os.path.join("/a/b", pathlib.Path("c"))
'/a/b/c'
>>> import os
>>> os.fspath(pathlib.Path("some_file.txt"))
'some_file.txt'

```

(Implemented by Brett Cannon, Ethan Furman, Dusty Phillips, and Jelle Zijlstra.)

See also

[**PEP 519**](https://peps.python.org/pep-0519/) — Adding a file system path protocol

PEP written by Brett Cannon and Koos Zevenhoven.

[Subject index](INDEX.md) · [Previous source section](pep-487-descriptor-protocol-enhancements.md) · [Next source section](pep-495-local-time-disambiguation.md) · [Release/subject declaration](summary-release-highlights.md)
