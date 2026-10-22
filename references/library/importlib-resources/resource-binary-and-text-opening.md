# importlib.resources: `importlib.resources.open_binary()`, `importlib.resources.open_text()`

### Functional API

There's a collection of streamlined, backwards-compatible helpers on hand. With them, the usual operations fold down into one function call.

Across every one of the functions below:

- *anchor* is an `Anchor`, just as it is in `files()`. The difference from `files` is that here you cannot leave it out.

- *path_names* are the pieces making up a resource’s path name, taken relative to the anchor. As an illustration, to fetch the text of a resource called `info.txt`, write:

```python
importlib.resources.read_text(my_module, "info.txt")

```

As with [`Traversable.joinpath`](https://docs.python.org/3.14/library/importlib.resources.abc.html#importlib.resources.abc.Traversable), the separate pieces ought to rely on forward slashes (`/`) for their path separators. To illustrate, these two are equivalent:

```python
importlib.resources.read_binary(my_module, "pics/painting.png")
importlib.resources.read_binary(my_module, "pics", "painting.png")

```

To preserve backward compatibility, any text-reading function insists on an explicit *encoding* argument once you pass more than one *path_names*. As an illustration, to fetch the text of `info/chapter1.txt`, write:

```python
importlib.resources.read_text(my_module, "info", "chapter1.txt",
                              encoding='utf-8')

```

 importlib.resources.open_binary(*anchor*, **path_names*)

Open the named resource for binary reading.

Refer to the introduction for the particulars on *anchor* and *path_names*.

What this function returns is a [`BinaryIO`](https://docs.python.org/3.14/library/typing.html#typing.BinaryIO) object — in other words, a binary stream open for reading.

Roughly speaking, this function does the same as:

```python
files(anchor).joinpath(*path_names).open('rb')

```

Changed in version 3.13: Multiple *path_names* are accepted.

 importlib.resources.open_text(*anchor*, **path_names*, *encoding='utf-8'*, *errors='strict'*)

Open the named resource for text reading. Absent any other instruction, its contents are read as strict UTF-8.

Refer to the introduction for the particulars on *anchor* and *path_names*. Here *encoding* and *errors* carry the same sense they do in built-in [`open()`](https://docs.python.org/3.14/library/functions.html#open).

To preserve backward compatibility, you must spell out the *encoding* argument whenever more than one *path_names* is present. That restriction is set to disappear in Python 3.15.

What this function returns is a [`TextIO`](https://docs.python.org/3.14/library/typing.html#typing.TextIO) object — in other words, a text stream open for reading.

Roughly speaking, this function does the same as:

```python
files(anchor).joinpath(*path_names).open('r', encoding=encoding)

```

Changed in version 3.13: more than one *path_names* may now be supplied, while *encoding* and *errors* have to be passed as keyword arguments.

[Subject index](INDEX.md) · [Previous](resource-anchors-and-filesystem-context.md) · [Continue](resource-reading-and-existence.md) · [Owning module, declaration or section: importlib.resources](resource-anchors-and-filesystem-context.md)
