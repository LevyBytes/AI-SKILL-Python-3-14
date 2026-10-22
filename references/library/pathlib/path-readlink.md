# pathlib: `Path.readlink()`

Path.readlink()

Return the path that the symbolic link points at (as [`os.readlink()`](https://docs.python.org/3.14/library/os.html#os.readlink) returns it):

```python
>>> p = Path('mylink')
>>> p.symlink_to('setup.py')
>>> p.readlink()
PosixPath('setup.py')

```

Added in version 3.9.

Changed in version 3.13: Raises `UnsupportedOperation` when [`os.readlink()`](https://docs.python.org/3.14/library/os.html#os.readlink) is unavailable. In earlier versions, [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError) was raised.

[Subject index](INDEX.md) · [Previous](path-expanduser-to-path-resolve.md) · [Continue](path-stat-to-path-is-mount.md) · [Owning module, declaration or section: pathlib](pathlib-object-oriented-filesystem-paths.md) · [Owning module, declaration or section: Expanding and resolving paths](path-expanduser-to-path-resolve.md)
