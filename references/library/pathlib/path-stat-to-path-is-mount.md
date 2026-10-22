# pathlib: `Path.stat()`, `Path.lstat()`, `Path.exists()`, `Path.is_file()`, `Path.is_dir()`, `Path.is_symlink()`, `Path.is_junction()`, `Path.is_mount()`

### Querying file type and status

Changed in version 3.8: For paths holding characters that cannot be represented at the OS level, `exists()`, `is_dir()`, `is_file()`, `is_mount()`, `is_symlink()`, `is_block_device()`, `is_char_device()`, `is_fifo()`, `is_socket()` now return `False` rather than raising an exception.

Changed in version 3.14: The methods listed above now return `False` rather than letting any [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) exception from the operating system through. In earlier versions, certain kinds of `OSError` exception were raised while others were suppressed. The new behaviour lines up with [`os.path.exists()`](https://docs.python.org/3.14/library/os.path.html#os.path.exists), [`os.path.isdir()`](https://docs.python.org/3.14/library/os.path.html#os.path.isdir), and so on. Reach for `stat()` to obtain the file status without suppressing exceptions.

 Path.stat(***, *follow_symlinks=True*)

Return an [`os.stat_result`](https://docs.python.org/3.14/library/os.html#os.stat_result) object carrying information about this path, much like [`os.stat()`](https://docs.python.org/3.14/library/os.html#os.stat). The result gets looked up on every call of this method.

Ordinarily this method follows symlinks; to stat a symlink itself, add the argument `follow_symlinks=False`, or turn to `lstat()`.

```python
>>> p = Path('setup.py')
>>> p.stat().st_size
956
>>> p.stat().st_mtime
1327883547.852554

```

Changed in version 3.10: The *follow_symlinks* parameter was added.

 Path.lstat()

Like `Path.stat()`, except that when the path points at a symbolic link, it returns the symbolic link's information instead of the target's.

 Path.exists(***, *follow_symlinks=True*)

Return `True` when the path points at an existing file or directory. You get `False` back when the path is invalid, inaccessible or missing. Reach for `Path.stat()` to tell those cases apart.

Ordinarily this method follows symlinks; to check whether a symlink exists, add the argument `follow_symlinks=False`.

```python
>>> Path('.').exists()
True
>>> Path('setup.py').exists()
True
>>> Path('/etc').exists()
True
>>> Path('nonexistentfile').exists()
False

```

Changed in version 3.12: The *follow_symlinks* parameter was added.

 Path.is_file(***, *follow_symlinks=True*)

Return `True` when the path points at a regular file. You get `False` back when the path is invalid, inaccessible or missing, or when it points at something that is not a regular file. Reach for `Path.stat()` to tell those cases apart.

Ordinarily this method follows symlinks; to leave symlinks out, add the argument `follow_symlinks=False`.

Changed in version 3.13: The *follow_symlinks* parameter was added.

 Path.is_dir(***, *follow_symlinks=True*)

Return `True` when the path points at a directory. You get `False` back when the path is invalid, inaccessible or missing, or when it points at something that is not a directory. Reach for `Path.stat()` to tell those cases apart.

Ordinarily this method follows symlinks; to leave out symlinks to directories, add the argument `follow_symlinks=False`.

Changed in version 3.13: The *follow_symlinks* parameter was added.

 Path.is_symlink()

Return `True` when the path points at a symbolic link, even a broken one. You get `False` back when the path is invalid, inaccessible or missing, or when it points at something that is not a symbolic link. Reach for `Path.stat()` to tell those cases apart.

 Path.is_junction()

Return `True` when the path points at a junction, and `False` for every other type of file. For now junctions exist only on Windows.

Added in version 3.12.

 Path.is_mount()

Return `True` when the path is a *mount point*: a spot in a file system where some other file system has been mounted. On POSIX, the function tests whether *path*'s parent, `path/..`, sits on a different device than *path*, or whether `path/..` and *path* refer to the same i-node on the same device — this ought to spot mount points across all Unix and POSIX variants. On Windows, what counts as a mount point is a drive letter root (e.g. `c:\`), a UNC share (`\\server\share`, for instance), or a directory where a filesystem is mounted.

Added in version 3.7.

Changed in version 3.12: Windows support was added.

[Subject index](INDEX.md) · [Previous](path-readlink.md) · [Continue](path-is-socket-to-path-info.md) · [Owning module, declaration or section: pathlib](pathlib-object-oriented-filesystem-paths.md)
