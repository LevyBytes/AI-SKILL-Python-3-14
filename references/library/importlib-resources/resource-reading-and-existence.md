# importlib.resources: `importlib.resources.read_binary()`, `importlib.resources.read_text()`, `importlib.resources.path()`, `importlib.resources.is_resource()`

importlib.resources.read_binary(*anchor*, **path_names*)

Read the named resource and hand back its contents as [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes).

Refer to the introduction for the particulars on *anchor* and *path_names*.

Roughly speaking, this function does the same as:

```python
files(anchor).joinpath(*path_names).read_bytes()

```

Changed in version 3.13: Multiple *path_names* are accepted.

 importlib.resources.read_text(*anchor*, **path_names*, *encoding='utf-8'*, *errors='strict'*)

Read the named resource and hand back its contents as [`str`](https://docs.python.org/3.14/library/stdtypes.html#str). Absent any other instruction, the contents are read as strict UTF-8.

Refer to the introduction for the particulars on *anchor* and *path_names*. Here *encoding* and *errors* carry the same sense they do in built-in [`open()`](https://docs.python.org/3.14/library/functions.html#open).

To preserve backward compatibility, you must spell out the *encoding* argument whenever more than one *path_names* is present. That restriction is set to disappear in Python 3.15.

Roughly speaking, this function does the same as:

```python
files(anchor).joinpath(*path_names).read_text(encoding=encoding)

```

Changed in version 3.13: several *path_names* are now permitted, and both *encoding* and *errors* must be handed over as keyword arguments.

 importlib.resources.path(*anchor*, **path_names*)

Supplies the path to the *resource* as a real file system path. The function returns a context manager meant for a [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement, and that context manager yields a [`pathlib.Path`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path) object.

Leaving the context manager tidies up whatever temporary files were made, for instance when the resource has to be pulled out of a zip file.

To illustrate, the [`stat()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.stat) method calls for a real file system path; you can apply it this way:

```python
with importlib.resources.path(anchor, "resource.txt") as fspath:
    result = fspath.stat()

```

Refer to the introduction for the particulars on *anchor* and *path_names*.

Roughly speaking, this function does the same as:

```python
as_file(files(anchor).joinpath(*path_names))

```

Changed in version 3.13: Multiple *path_names* are accepted.

 importlib.resources.is_resource(*anchor*, **path_names*)

Hand back `True` when the named resource is present, and `False` otherwise. Directories are not treated as resources by this function.

Refer to the introduction for the particulars on *anchor* and *path_names*.

Roughly speaking, this function does the same as:

```python
files(anchor).joinpath(*path_names).is_file()

```

Changed in version 3.13: Multiple *path_names* are accepted.

[Subject index](INDEX.md) · [Previous](resource-binary-and-text-opening.md) · [Continue](importlib-resources-contents.md) · [Owning module, declaration or section: importlib.resources](resource-anchors-and-filesystem-context.md) · [Owning module, declaration or section: Functional API](resource-binary-and-text-opening.md)
