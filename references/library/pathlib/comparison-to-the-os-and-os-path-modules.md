# pathlib - Comparison to the `os` and `os.path` modules

### Comparison to the [`os`](https://docs.python.org/3.14/library/os.html#module-os) and [`os.path`](https://docs.python.org/3.14/library/os.path.html#module-os.path) modules

pathlib carries out path operations through `PurePath` and `Path` objects, which earns it the label *object-oriented*. The [`os`](https://docs.python.org/3.14/library/os.html#module-os) and [`os.path`](https://docs.python.org/3.14/library/os.path.html#module-os.path) modules, by contrast, hand you functions that operate on low-level `str` and `bytes` objects — a more *procedural* style. A number of users find the object-oriented form easier to read.

Plenty of functions across [`os`](https://docs.python.org/3.14/library/os.html#module-os) and [`os.path`](https://docs.python.org/3.14/library/os.path.html#module-os.path) accept `bytes` paths and [paths relative to directory descriptors](https://docs.python.org/3.14/library/os.html#dir-fd). pathlib offers neither of those capabilities.

Both Python's `str` and `bytes` types, together with chunks of the [`os`](https://docs.python.org/3.14/library/os.html#module-os) and [`os.path`](https://docs.python.org/3.14/library/os.path.html#module-os.path) modules, are coded in C and run very fast. pathlib, coded in pure Python, tends to lag, though hardly ever by enough to matter.

The way pathlib normalizes paths leans a touch more opinionated and consistent than [`os.path`](https://docs.python.org/3.14/library/os.path.html#module-os.path) does. To take one case, where [`os.path.abspath()`](https://docs.python.org/3.14/library/os.path.html#os.path.abspath) strips “`..`” segments out of a path — which can shift its meaning once symlinks enter the picture — `Path.absolute()` holds onto those segments for the sake of greater safety.

The way pathlib normalizes paths can make it a poor fit for certain applications:

1.

pathlib reduces `Path("my_folder/")` down to `Path("my_folder")`, and that shifts a path's meaning once it's fed to assorted operating system APIs and command-line utilities. In particular, with no trailing separator the path might resolve to either a file or a directory rather than strictly a directory.

2.

pathlib reduces `Path("./my_program")` down to `Path("my_program")`, and that shifts a path's meaning when it serves as an executable search path — in a shell, say, or while spawning a child process. In particular, with no separator in the path it may end up sought out along `PATH` rather than in the current directory.

Owing to these divergences, pathlib won't serve as a drop-in stand-in for [`os.path`](https://docs.python.org/3.14/library/os.path.html#module-os.path).

[Subject index](INDEX.md) · [Previous](comparison-to-the-glob-module.md) · [Continue](corresponding-tools.md) · [Owning module, declaration or section: pathlib](pathlib-object-oriented-filesystem-paths.md)
