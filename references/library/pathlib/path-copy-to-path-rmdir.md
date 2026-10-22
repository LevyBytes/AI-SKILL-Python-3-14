# pathlib — Copying, moving and deleting

### Copying, moving and deleting

 Path.copy(*target*, ***, *follow_symlinks=True*, *preserve_metadata=False*)

Copy this file or directory tree across to the supplied *target*, then hand back a fresh `Path` instance aimed at *target*.

Where the source is a file, an existing file at the target gets replaced. Where the source is a symlink and *follow_symlinks* is true (its default), what's copied is the symlink's target. If not, the symlink itself is rebuilt at the destination.

With *preserve_metadata* false (its default), the only things guaranteed to come across are directory structures and file data. Flip *preserve_metadata* to true so that file and directory permissions, flags, last-access and modification times, plus extended attributes get copied wherever that's supported. On Windows this argument does nothing when copying files, since metadata there is always kept.

Note

Wherever the operating system and file system allow it, this method does a lightweight copy in which data blocks are duplicated only once they change. The term for this is copy-on-write.

Added in version 3.14.

 Path.copy_into(*target_dir*, ***, *follow_symlinks=True*, *preserve_metadata=False*)

Copy this file or directory tree into the supplied *target_dir*, which ought to be a directory that already exists. The remaining arguments behave exactly as they do for `Path.copy()`. A fresh `Path` instance aimed at the copy is handed back.

Added in version 3.14.

 Path.rename(*target*)

Rename this file or directory to the supplied *target*, then hand back a fresh `Path` instance aimed at *target*. On Unix, an existing *target* that happens to be a file is replaced without a word, provided the user has permission. On Windows, an existing *target* triggers [`FileExistsError`](https://docs.python.org/3.14/library/exceptions.html#FileExistsError). You may give *target* as a string or as another path object:

```python
>>> p = Path('foo')
>>> p.open('w').write('some text')
9
>>> target = Path('bar')
>>> p.rename(target)
PosixPath('bar')
>>> target.open().read()
'some text'

```

For the target path, either an absolute or a relative one will do. A relative path is read against the current working directory — *not* against the directory of the `Path` object.

Under the hood it builds on [`os.rename()`](https://docs.python.org/3.14/library/os.html#os.rename) and offers the very same guarantees.

Changed in version 3.8: Added return value, return the new `Path` instance.

 Path.replace(*target*)

Rename this file or directory to the supplied *target*, then hand back a fresh `Path` instance aimed at *target*. Should *target* refer to an existing file or empty directory, that gets replaced no matter what.

For the target path, either an absolute or a relative one is fine. A relative path is taken against the current working directory — *not* against the directory of the `Path` object.

Changed in version 3.8: Added return value, return the new `Path` instance.

 Path.move(*target*)

Move this file or directory tree across to the supplied *target*, then hand back a fresh `Path` instance aimed at *target*.

Where the *target* is absent, it gets created. Where this path and the *target* are both existing files, the target is overwritten. Where the two paths refer to the same file or directory, or the *target* is a directory that isn't empty, [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) is raised.

Where both paths live on the same filesystem, the move runs via [`os.replace()`](https://docs.python.org/3.14/library/os.html#os.replace). Otherwise this path is first copied (keeping metadata and symlinks) and then removed.

Added in version 3.14.

 Path.move_into(*target_dir*)

Move this file or directory tree into the supplied *target_dir*, which ought to be a directory that already exists. A fresh `Path` instance aimed at the moved path is handed back.

Added in version 3.14.

 Path.unlink(*missing_ok=False*)

Remove this file or symbolic link. Where the path refers to a directory, reach for `Path.rmdir()` instead.

With *missing_ok* false (its default), [`FileNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#FileNotFoundError) is raised when the path is absent.

With *missing_ok* true, any [`FileNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#FileNotFoundError) exception is swallowed (matching how the POSIX `rm -f` command behaves).

Changed in version 3.8: The *missing_ok* parameter was added.

 Path.rmdir()

Remove this directory. The directory must be empty.

[Subject index](INDEX.md) · [Previous](path-symlink-to-to-path-hardlink-to.md) · [Continue](path-owner-to-path-lchmod.md) · [Owning module, declaration or section: pathlib](pathlib-object-oriented-filesystem-paths.md)
