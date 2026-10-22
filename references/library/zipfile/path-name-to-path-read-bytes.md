# zipfile: `Path.name`, `Path.open()`, `Path.iterdir()`, `Path.is_dir()`, `Path.is_file()`, `Path.is_symlink()`, `Path.exists()`, `Path.suffix`, `Path.stem`, `Path.suffixes`, `Path.read_text()`, `Path.read_bytes()`

The `Path` class performs no sanitizing of filenames held inside the ZIP archive. In contrast to the `ZipFile.extract()` and `ZipFile.extractall()` methods, validating or sanitizing filenames to head off path traversal vulnerabilities (such as absolute paths or paths bearing “..” components) rests with the caller. Where untrusted archives are involved, weigh resolving filenames through [`os.path.abspath()`](https://docs.python.org/3.14/library/os.path.html#os.path.abspath) and verifying them against the target directory with [`os.path.commonpath()`](https://docs.python.org/3.14/library/os.path.html#os.path.commonpath).

Path objects surface the following capabilities of [`pathlib.Path`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path) objects:

Path objects can be traversed by way of the `/` operator or `joinpath`.

 Path.name

The final path component.

 Path.open(*mode='r'*, ***, *pwd*, ****)

Invoke `ZipFile.open()` against the current path. Permits opening for read or write, text or binary, across the supported modes: ‘r’, ‘w’, ‘rb’, ‘wb’. Positional and keyword arguments get forwarded to [`io.TextIOWrapper`](https://docs.python.org/3.14/library/io.html#io.TextIOWrapper) when opened as text, and otherwise disregarded. `pwd` is the `pwd` parameter to `ZipFile.open()`.

Changed in version 3.9: Both text and binary modes for open gained support. The mode now defaults to text.

Changed in version 3.11.2: The `encoding` parameter may be handed over as a positional argument without triggering a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError). Just as it could in 3.9. Code that has to stay compatible with unpatched 3.10 and 3.11 releases must hand over every [`io.TextIOWrapper`](https://docs.python.org/3.14/library/io.html#io.TextIOWrapper) argument, `encoding` among them, as keywords.

 Path.iterdir()

Enumerate the children of the current directory.

 Path.is_dir()

Return `True` if the current context references a directory.

 Path.is_file()

Return `True` if the current context references a file.

 Path.is_symlink()

Return `True` if the current context references a symbolic link.

Added in version 3.12.

Changed in version 3.13: Formerly, `is_symlink` would always return `False` no matter what.

 Path.exists()

Return `True` when the current context points at a file or directory living inside the zip file.

 Path.suffix

The trailing dot-separated piece of the final component, where one exists. People commonly call this the file extension.

Added in version 3.11: Added `Path.suffix` property.

 Path.stem

The final path component, without its suffix.

Added in version 3.11: Added `Path.stem` property.

 Path.suffixes

A list of the path's suffixes, commonly called file extensions.

Added in version 3.11: Added `Path.suffixes` property.

 Path.read_text(***, ****)

Read the current file as unicode text. Positional and keyword arguments get forwarded to [`io.TextIOWrapper`](https://docs.python.org/3.14/library/io.html#io.TextIOWrapper) (save for `buffer`, which the context already implies).

Changed in version 3.11.2: The `encoding` parameter may be handed over as a positional argument without triggering a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError). Just as it could in 3.9. Code that has to stay compatible with unpatched 3.10 and 3.11 releases must hand over every [`io.TextIOWrapper`](https://docs.python.org/3.14/library/io.html#io.TextIOWrapper) argument, `encoding` among them, as keywords.

 Path.read_bytes()

Read the current file as bytes.

[Subject index](INDEX.md) · [Continue](path-joinpath.md) · [Owning module, declaration or section: zipfile](zipfile-badzipfile-to-zipfile-largezipfile.md) · [Owning module, declaration or section: zipfile.Path](zipfile-path-class.md) · [Owning module, declaration or section: Path objects](zipfile-path-class.md) · [Preceding source contract and version conditions](zipfile-path-class.md)
