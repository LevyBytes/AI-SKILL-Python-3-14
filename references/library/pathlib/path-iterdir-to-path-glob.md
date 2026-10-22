# pathlib: `Path.iterdir()`, `Path.glob()`

### Reading directories

 Path.iterdir()

While the path points at a directory, yield path objects for the directory's contents:

```python
>>> p = Path('docs')
>>> for child in p.iterdir(): child
...
PosixPath('docs/conf.py')
PosixPath('docs/_templates')
PosixPath('docs/make.bat')
PosixPath('docs/index.rst')
PosixPath('docs/_build')
PosixPath('docs/_static')
PosixPath('docs/Makefile')

```

The children come out in arbitrary order, and the special entries `'.'` and `'..'` are left out. Should a file be removed from or added to the directory after the iterator is created, whether a path object for that file shows up is unspecified.

When the path is not a directory or is otherwise inaccessible, [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) is raised.

 Path.glob(*pattern*, ***, *case_sensitive=None*, *recurse_symlinks=False*)

Glob the given relative *pattern* within the directory this path stands for, yielding every matching file (of whatever kind):

```python
>>> sorted(Path('.').glob('*.py'))
[PosixPath('pathlib.py'), PosixPath('setup.py'), PosixPath('test_pathlib.py')]
>>> sorted(Path('.').glob('*/*.py'))
[PosixPath('docs/conf.py')]
>>> sorted(Path('.').glob('**/*.py'))
[PosixPath('build/lib/pathlib.py'),
 PosixPath('docs/conf.py'),
 PosixPath('pathlib.py'),
 PosixPath('setup.py'),
 PosixPath('test_pathlib.py')]

```

Note

The paths come back in no particular order. When you need a specific order, sort the results.

See also

Pattern language documentation.

By default, or whenever the *case_sensitive* keyword-only argument is `None`, this method matches paths by platform-specific casing rules: case-sensitive on POSIX as a rule, and case-insensitive on Windows. Set *case_sensitive* to `True` or `False` to override that behaviour.

By default, or whenever the *recurse_symlinks* keyword-only argument is `False`, this method follows symlinks except while expanding "`**`" wildcards. Set *recurse_symlinks* to `True` so symlinks are always followed.

Note

Every [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) exception arising from the filesystem scan gets suppressed. That covers [`PermissionError`](https://docs.python.org/3.14/library/exceptions.html#PermissionError) when reaching directories without read permission.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `pathlib.Path.glob` with arguments `self`, `pattern`.

Changed in version 3.12: The *case_sensitive* parameter was added.

Changed in version 3.13: The *recurse_symlinks* parameter was added.

Changed in version 3.13: The *pattern* parameter accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

Changed in version 3.13: Every [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) exception arising from the filesystem scan gets suppressed. In earlier versions, such exceptions were suppressed in many cases, though not in all.

[Subject index](INDEX.md) · [Previous](path-write-bytes.md) · [Continue](path-rglob.md) · [Owning module, declaration or section: pathlib](pathlib-object-oriented-filesystem-paths.md)
