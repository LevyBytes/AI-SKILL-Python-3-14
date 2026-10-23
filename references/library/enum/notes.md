# enum - Notes

### Notes

`IntEnum`, `StrEnum`, and `IntFlag`

>

Built to slot in cleanly wherever integer- or string-based values already appear, these three enum types carry a few additional restrictions because of that role:

- `__str__` reports the enum member’s value in place of its name

- `__format__`, since it relies on `__str__`, likewise surfaces the enum member’s value rather than its name

Should those restrictions not suit you, one option is to roll your own base class by mixing in the `int` or `str` type on your own:

```python
>>> from enum import Enum
>>> class MyIntEnum(int, Enum):
...     pass

```

alternatively, reassign the relevant [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str), and so on, right inside your enum:

```python
>>> from enum import Enum, IntEnum
>>> class MyIntEnum(IntEnum):
...     __str__ = Enum.__str__

```

[Subject index](INDEX.md) · [Previous](enum-show-flag-values-to-enum-bin.md) · [Owning module, declaration or section: enum](enum-support-for-enumerations.md)
