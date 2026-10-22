# pathlib: `Path.symlink_to()`, `Path.hardlink_to()`

When *exist_ok* is true, [`FileExistsError`](https://docs.python.org/3.14/library/exceptions.html#FileExistsError) stays unraised unless the supplied path is already present on the file system while not being a directory (matching how the POSIX `mkdir -p` command behaves).

Changed in version 3.5: The *exist_ok* parameter was added.

 Path.symlink_to(*target*, *target_is_directory=False*)

Make this path a symbolic link pointing to *target*.

Under Windows, a symlink stands for either a file or a directory and won't shift to track the target on the fly. Where the target already exists, the symlink's type gets created so as to match it. Failing that, the symlink is created as a directory when *target_is_directory* is true, or otherwise as a file symlink (which is the default). Away from Windows, *target_is_directory* carries no weight.

```python
>>> p = Path('mylink')
>>> p.symlink_to('setup.py')
>>> p.resolve()
PosixPath('/home/antoine/pathlib/setup.py')
>>> p.stat().st_size
956
>>> p.lstat().st_size
8

```

Note

The order of arguments (link, target) is the reverse of [`os.symlink()`](https://docs.python.org/3.14/library/os.html#os.symlink)’s.

Changed in version 3.13: `UnsupportedOperation` gets raised should [`os.symlink()`](https://docs.python.org/3.14/library/os.html#os.symlink) be unavailable. Earlier releases raised [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError) here.

 Path.hardlink_to(*target*)

Make this path a hard link to the same file as *target*.

Note

The order of arguments (link, target) is the reverse of [`os.link()`](https://docs.python.org/3.14/library/os.html#os.link)’s.

Added in version 3.10.

Changed in version 3.13: `UnsupportedOperation` is now raised whenever [`os.link()`](https://docs.python.org/3.14/library/os.html#os.link) cannot be used. Prior releases raised [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError) in that situation.

[Subject index](INDEX.md) · [Continue](path-copy-to-path-rmdir.md) · [Owning module, declaration or section: pathlib](pathlib-object-oriented-filesystem-paths.md) · [Owning module, declaration or section: Creating files and directories](path-touch-to-path-mkdir.md) · [Owning module, declaration or section: Path.mkdir](path-touch-to-path-mkdir.md) · [Preceding source contract and version conditions](path-touch-to-path-mkdir.md)
