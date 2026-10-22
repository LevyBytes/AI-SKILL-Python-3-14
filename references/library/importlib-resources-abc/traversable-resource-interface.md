# importlib.resources.abc: `importlib.resources.abc.Traversable`, `read_bytes()`, `read_text()`

*class *importlib.resources.abc.Traversable

An object carrying a portion of the [`pathlib.Path`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path) methods, the ones fit for walking directories and opening files.

To get a file-system representation of the object, reach for [`importlib.resources.as_file()`](https://docs.python.org/3.14/library/importlib.resources.html#importlib.resources.as_file).

 name

Abstract. This object's base name, stripped of any parent references.

 *abstractmethod *iterdir()

Yield Traversable objects in self.

 *abstractmethod *is_dir()

Return `True` if self is a directory.

 *abstractmethod *is_file()

Return `True` if self is a file.

 *abstractmethod *joinpath(**pathsegments*)

Traverse directories according to *pathsegments* and return the result as `Traversable`.

Any single *pathsegments* argument is free to hold several names joined by forward slashes (`/`, `posixpath.sep` ). To illustrate, these two are equivalent:

```python
files.joinpath('subdir', 'subsuddir', 'file.txt')
files.joinpath('subdir/subsuddir/file.txt')

```

Be aware that certain `Traversable` implementations may lag behind the newest protocol revision. To stay compatible with those, hand each `joinpath` call just one argument that carries no path separators. For instance:

```python
files.joinpath('subdir').joinpath('subsubdir').joinpath('file.txt')

```

Changed in version 3.11: `joinpath` now takes several *pathsegments*, and within those segments forward slashes count as path separators. Up to that point, only one *child* argument could be supplied.

 *abstractmethod *__truediv__(*child*)

Return Traversable child in self. Equivalent to `joinpath(child)`.

 *abstractmethod *open(*mode='r'*, **args*, ***kwargs*)

For *mode*, pass ‘r’ or ‘rb’ to open in text or binary. The call returns a handle you can read from (the same as [`pathlib.Path.open`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.open)).

Opening in text mode lets you supply encoding parameters of the sort [`io.TextIOWrapper`](https://docs.python.org/3.14/library/io.html#io.TextIOWrapper) takes.

 read_bytes()

Read contents of self as bytes.

 read_text(*encoding=None*)

Read contents of self as text.

[Subject index](INDEX.md) · [Previous](importlib-resources-abc-abstract-base-classes-for-resources.md) · [Continue](importlib-resources-abc-traversableresources-class.md) · [Owning module, declaration or section: importlib.resources.abc](importlib-resources-abc-resourcereader-class.md)
