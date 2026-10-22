# pathlib: `Path.touch()`, `Path.mkdir()`

### Creating files and directories

 Path.touch(*mode=0o666*, *exist_ok=True*)

Create a file at the given path. When *mode* is supplied, it gets combined with the process's `umask` value to settle the file mode and access flags. When the file is already there, the function succeeds if *exist_ok* is true (and its modification time gets bumped to the current time), otherwise [`FileExistsError`](https://docs.python.org/3.14/library/exceptions.html#FileExistsError) is raised.

See also

The `open()`, `write_text()` and `write_bytes()` methods see frequent use for creating files.

 Path.mkdir(*mode=0o777*, *parents=False*, *exist_ok=False*)

Create a new directory at the given path. When *mode* is supplied, it gets combined with the process's `umask` value to settle the file mode and access flags. When the path is already there, [`FileExistsError`](https://docs.python.org/3.14/library/exceptions.html#FileExistsError) is raised.

When *parents* is true, every missing parent of this path is created as needed; they get created with the default permissions, leaving *mode* out of the picture (echoing the POSIX `mkdir -p` command).

When *parents* is false (the default), a missing parent raises [`FileNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#FileNotFoundError).

When *exist_ok* is false (the default), [`FileExistsError`](https://docs.python.org/3.14/library/exceptions.html#FileExistsError) is raised should the target directory already exist.

[Subject index](INDEX.md) · [Previous](path-walk.md) · [Owning module, declaration or section: pathlib](pathlib-object-oriented-filesystem-paths.md) · [Required continuation of the source contract](path-symlink-to-to-path-hardlink-to.md)
