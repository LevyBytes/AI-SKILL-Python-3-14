# os.path: `os.path.abspath()`, `os.path.basename()`, `os.path.commonpath()`, `os.path.commonprefix()`, `os.path.dirname()`

### `os.path` - Common pathname manipulations

**Source code:** [Lib/genericpath.py](https://github.com/python/cpython/tree/3.14/Lib/genericpath.py), [Lib/posixpath.py](https://github.com/python/cpython/tree/3.14/Lib/posixpath.py) (for POSIX) and [Lib/ntpath.py](https://github.com/python/cpython/tree/3.14/Lib/ntpath.py) (for Windows).

---

A handful of handy routines that operate on pathnames live in this module. For reading from or writing to files, consult [`open()`](https://docs.python.org/3.14/library/functions.html#open); to interact with the filesystem itself, turn to the [`os`](https://docs.python.org/3.14/library/os.html#module-os) module. You may supply the path arguments as strings, as bytes, or as any object that implements the [`os.PathLike`](https://docs.python.org/3.14/library/os.html#os.PathLike) protocol.

Python, in contrast to a Unix shell, performs no *automatic* expansion of paths. When an application wants shell-style path expansion, it must call routines like `expanduser()` and `expandvars()` directly. (The [`glob`](https://docs.python.org/3.14/library/glob.html#module-glob) module is also worth a look here.)

See also

For high-level path objects, turn to the [`pathlib`](https://docs.python.org/3.14/library/pathlib.html#module-pathlib) module.

Note

Each of these routines takes parameters that are exclusively bytes or exclusively string objects. When a path or file name comes back, it shares the type of what was passed in.

Note

Because path name conventions vary from one operating system to the next, the standard library ships several flavors of this module. Whichever path module fits the operating system Python currently runs under is what `os.path` resolves to, which makes it appropriate for local paths. That said, should you need to work with a path that is *always* in one particular format, you can import and call the individual modules directly. The interface is identical across all of them:

- `posixpath` for UNIX-style paths

- `ntpath` for Windows paths

Changed in version 3.8: rather than raising an exception, `exists()`, `lexists()`, `isdir()`, `isfile()`, `islink()`, and `ismount()` from now on give back `False` for any path holding characters or bytes the OS level cannot represent.

 os.path.abspath(*path*)

Produce a normalized, absolutized form of the pathname *path*. For the majority of platforms, that amounts to invoking `normpath(join(os.getcwd(), path))`.

See also

`os.path.join()` and `os.path.normpath()`.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

 os.path.basename(*path*, */*)

Give back the base name of pathname *path*. It corresponds to the second member of the pair you get by handing *path* to the function `split()`. Be aware that what this function yields diverges from the Unix **basename** program: for `'/foo/bar/'`, where **basename** would give `'bar'`, the `basename()` function hands back an empty string (`''`).

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

 os.path.commonpath(*paths*)

Give back the longest common sub-path shared by every pathname in the iterable *paths*. A [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised when *paths* mixes absolute and relative pathnames, when its entries sit on different drives, or when *paths* is empty. In contrast to `commonprefix()`, what comes back here is a valid path.

Added in version 3.5.

Changed in version 3.6: Accepts a sequence of [path-like objects](https://docs.python.org/3.14/glossary.html#term-path-like-object).

Changed in version 3.13: where only sequences once worked, any iterable is now accepted.

 os.path.commonprefix(*list*, */*)

Give back the longest string prefix (compared character-by-character) common to every string in *list*. When *list* holds nothing, the empty string (`''`) comes back.

Warning

Because it operates one character at a time, this function can hand back invalid paths. When what you actually need is a **common path prefix**, the algorithm here is not safe for that purpose. Reach for `commonpath()` to locate a common path prefix instead.

```python
>>> os.path.commonprefix(['/usr/lib', '/usr/local/lib'])
'/usr/l'

>>> os.path.commonpath(['/usr/lib', '/usr/local/lib'])
'/usr'

```

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

 os.path.dirname(*path*, */*)

Give back the directory name of pathname *path*. It is the first member of the pair produced by handing *path* to the function `split()`.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

[Subject index](INDEX.md) · [Previous](os-path-common-pathname-manipulations.md) · [Continue](os-path-exists-to-os-path-isdir.md)
