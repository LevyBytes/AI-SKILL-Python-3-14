# pickle - Comparison with `marshal`

### Relationship to other Python modules

### Comparison with `marshal`

Python ships a lower-level serialization module named [`marshal`](https://docs.python.org/3.14/library/marshal.html#module-marshal), yet as a rule `pickle` should be your preferred means of serializing Python objects. `marshal` is around chiefly to support Python's `.pyc` files.

In several important respects the `pickle` module is unlike [`marshal`](https://docs.python.org/3.14/library/marshal.html#module-marshal):

- [`marshal`](https://docs.python.org/3.14/library/marshal.html#module-marshal) cannot serialize user-defined classes or their instances. `pickle`, by contrast, saves and restores class instances seamlessly, though the class definition has to be importable and reside in the same module it did when the object was pickled.

- There is no guarantee that the [`marshal`](https://docs.python.org/3.14/library/marshal.html#module-marshal) serialization format stays portable from one Python version to the next. Since its main purpose in life is supporting `.pyc` files, the Python implementers keep the freedom to alter the serialization format in non-backwards-compatible ways whenever the need comes up. The `pickle` serialization format, by contrast, comes with a guarantee of backwards compatibility from one Python release to the next, so long as you pick a compatible pickle protocol and your pickling and unpickling code handles the Python 2 versus Python 3 type differences whenever your data crosses that one-of-a-kind breaking-change language boundary.

[Subject index](INDEX.md) · [Continue](comparison-with-json.md) · [Owning module, declaration or section: pickle](pickle-python-object-serialization.md)
