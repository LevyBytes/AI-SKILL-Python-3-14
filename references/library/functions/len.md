# Built-in Functions

len(*object*, */*)

Yield the length (the count of items) belonging to an object. The argument can be a sequence (for instance a string, bytes, tuple, list, or range) or a collection (for instance a dictionary, set, or frozen set).

**CPython implementation detail:** `len` raises [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) for lengths exceeding [`sys.maxsize`](https://docs.python.org/3.14/library/sys.html#sys.maxsize), for instance [`range(2 ** 100)`](https://docs.python.org/3.14/library/stdtypes.html#range).

[Subject index](INDEX.md) · [Previous](iter.md) · [Continue](list-class.md) · [Owning module, declaration or section: Built-in Functions](INDEX.md)
