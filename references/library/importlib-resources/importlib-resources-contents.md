# importlib.resources: `importlib.resources.contents()`

importlib.resources.contents(*anchor*, **path_names*)

Hand back an iterable covering the named items inside the package or path. That iterable yields the names of resources (files, say) and non-resources (directories, say) as [`str`](https://docs.python.org/3.14/library/stdtypes.html#str). It does not descend into subdirectories.

Refer to the introduction for the particulars on *anchor* and *path_names*.

Roughly speaking, this function does the same as:

```python
for resource in files(anchor).joinpath(*path_names).iterdir():
    yield resource.name

```

Deprecated since version 3.11: Lean on `iterdir()` as shown above; it gives you tighter control over the results plus richer functionality.

[Subject index](INDEX.md) · [Previous](resource-reading-and-existence.md) · [Owning module, declaration or section: importlib.resources](resource-anchors-and-filesystem-context.md) · [Owning module, declaration or section: Functional API](resource-binary-and-text-opening.md)
