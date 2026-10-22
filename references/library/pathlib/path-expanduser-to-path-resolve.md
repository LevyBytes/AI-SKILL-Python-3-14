# pathlib: `Path.home()`, `Path.expanduser()`, `Path.cwd()`, `Path.absolute()`, `Path.resolve()`

### Expanding and resolving paths

 *classmethod *Path.home()

Build a new path object standing for the user's home directory (as [`os.path.expanduser()`](https://docs.python.org/3.14/library/os.path.html#os.path.expanduser) returns it with the `~` construct). When the home directory cannot be resolved, [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) is raised.

```python
>>> Path.home()
PosixPath('/home/antoine')

```

Added in version 3.5.

 Path.expanduser()

Build a new path with the `~` and `~user` constructs expanded, just as [`os.path.expanduser()`](https://docs.python.org/3.14/library/os.path.html#os.path.expanduser) returns them. When a home directory cannot be resolved, [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) is raised.

```python
>>> p = PosixPath('~/films/Monty Python')
>>> p.expanduser()
PosixPath('/home/eric/films/Monty Python')

```

Added in version 3.5.

 *classmethod *Path.cwd()

Build a new path object standing for the current directory (as [`os.getcwd()`](https://docs.python.org/3.14/library/os.html#os.getcwd) returns it):

```python
>>> Path.cwd()
PosixPath('/home/antoine/pathlib')

```

 Path.absolute()

Turn the path absolute, with no normalization and no resolving of symlinks. Hands back a new path object:

```python
>>> p = Path('tests')
>>> p
PosixPath('tests')
>>> p.absolute()
PosixPath('/home/antoine/pathlib/tests')

```

 Path.resolve(*strict=False*)

Turn the path absolute, resolving every symlink along the way. A new path object comes back:

```python
>>> p = Path()
>>> p
PosixPath('.')
>>> p.resolve()
PosixPath('/home/antoine/pathlib')

```

"`..`" components get stripped too (no other method does this):

```python
>>> p = Path('docs/../setup.py')
>>> p.resolve()
PosixPath('/home/antoine/pathlib/setup.py')

```

Should a path be absent or a symlink loop turn up while *strict* is `True`, [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) is raised. Where *strict* is `False`, the path gets resolved as far as it can, and whatever is left over is tacked on without any check that it exists.

Changed in version 3.6: The *strict* parameter was added (the pre-3.6 behavior is strict).

Changed in version 3.13: Symlink loops are now handled like any other error: [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) gets raised in strict mode, and nothing is raised in non-strict mode. In earlier versions, [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) was raised regardless of the *strict* value.

[Subject index](INDEX.md) · [Previous](path-as-uri.md) · [Continue](path-readlink.md) · [Owning module, declaration or section: pathlib](pathlib-object-oriented-filesystem-paths.md)
