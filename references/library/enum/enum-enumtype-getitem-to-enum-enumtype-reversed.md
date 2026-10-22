# enum.EnumType: `__getitem__()`, `__iter__()`, `__len__()`, `__reversed__()`

__getitem__(*cls*, *name*)

Yields the Enum member within *cls* that matches *name*, or else raises a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError):

```python
>>> Color['BLUE']
<Color.BLUE: 3>

```

 __iter__(*cls*)

Yields every member of *cls* following definition order:

```python
>>> list(Color)
[<Color.RED: 1>, <Color.GREEN: 2>, <Color.BLUE: 3>]

```

 __len__(*cls*)

Yields how many members *cls* contains:

```python
>>> len(Color)
3

```

 __members__

Yields a mapping from each enum name to its member, aliases included

 __reversed__(*cls*)

Yields every member of *cls* following reverse definition order:

```python
>>> list(reversed(Color))
[<Color.BLUE: 3>, <Color.GREEN: 2>, <Color.RED: 1>]

```

[Subject index](INDEX.md) · [Previous](enum-enumtype-call-to-enum-enumtype-dir.md) · [Continue](enum-enum-class.md) · [Owning module, declaration or section: enum](enum-support-for-enumerations.md) · [Owning module, declaration or section: enum.EnumType](enum-enumtype-class.md) · [Owning module, declaration or section: Data types](enum-enumtype-class.md)
