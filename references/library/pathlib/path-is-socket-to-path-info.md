# pathlib: `Path.is_socket()`, `Path.is_fifo()`, `Path.is_block_device()`, `Path.is_char_device()`, `Path.samefile()`, `Path.info`

Path.is_socket()

Return `True` when the path points at a Unix socket. You get `False` back when the path is invalid, inaccessible or missing, or when it points at something that is not a Unix socket. Reach for `Path.stat()` to tell those cases apart.

 Path.is_fifo()

Return `True` when the path points at a FIFO. You get `False` back when the path is invalid, inaccessible or missing, or when it points at something that is not a FIFO. Reach for `Path.stat()` to tell those cases apart.

 Path.is_block_device()

Return `True` when the path points at a block device. You get `False` back when the path is invalid, inaccessible or missing, or when it points at something that is not a block device. Reach for `Path.stat()` to tell those cases apart.

 Path.is_char_device()

Return `True` when the path points at a character device. You get `False` back when the path is invalid, inaccessible or missing, or when it points at something that is not a character device. Reach for `Path.stat()` to tell those cases apart.

 Path.samefile(*other_path*)

Return whether this path refers to the same file as *other_path*, which may be either a Path object or a string. Its semantics resemble [`os.path.samefile()`](https://docs.python.org/3.14/library/os.path.html#os.path.samefile) and [`os.path.samestat()`](https://docs.python.org/3.14/library/os.path.html#os.path.samestat).

An [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) may be raised should either file be inaccessible for some reason.

```python
>>> p = Path('spam')
>>> q = Path('eggs')
>>> p.samefile(q)
False
>>> p.samefile('spam')
True

```

Added in version 3.5.

 Path.info

A `PathInfo` object that supports querying file type information. This object exposes methods whose results are cached, which can cut the number of system calls needed while switching on file type. As an example:

```python
>>> p = Path('src')
>>> if p.info.is_symlink():
...     print('symlink')
... elif p.info.is_dir():
...     print('directory')
... elif p.info.exists():
...     print('something else')
... else:
...     print('not found')
...
directory

```

When the path came out of `Path.iterdir()`, this attribute gets seeded with some file-type information picked up while scanning the parent directory. Just accessing `Path.info` runs no filesystem queries at all.

For information that is current, your best bet is to call `Path.is_dir()`, `is_file()` and `is_symlink()` instead of this attribute's methods. The cache cannot be reset; what you can do instead is build a new path object with an empty info cache via `p = Path(p)`.

Added in version 3.14.

[Subject index](INDEX.md) · [Previous](path-stat-to-path-is-mount.md) · [Continue](path-open-to-path-write-text.md) · [Owning module, declaration or section: pathlib](pathlib-object-oriented-filesystem-paths.md) · [Owning module, declaration or section: Querying file type and status](path-stat-to-path-is-mount.md)
