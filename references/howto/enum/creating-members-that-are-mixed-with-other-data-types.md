# Creating members that are mixed with other data types

### Creating members that are mixed with other data types

If you subclass another data type — for instance [`int`](https://docs.python.org/3.14/library/functions.html#int) or [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) — together with an [`Enum`](https://docs.python.org/3.14/library/enum.html#enum.Enum), then everything after the `=` is forwarded to that data type’s constructor. For example:

```python
>>> class MyEnum(IntEnum):      # help(int) -> int(x, base=10) -> integer
...     example = '11', 16      # so x='11' and base=16
...
>>> MyEnum.example.value        # and hex(11) is...
17

```

[Subject index](INDEX.md) · [Previous source context](enum-member-type.md) · [Following source context](boolean-value-of-enum-classes-and-members.md)
