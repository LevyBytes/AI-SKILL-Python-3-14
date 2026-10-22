# enum.Enum: `Weekday.__init__()`, `__init_subclass__()`, `_missing_()`, `__new__()`, `__repr__()`

`Weekday.__init__()` would be called as `Weekday.__init__(self, 1, 'Mon')`

 __init_subclass__(*cls*, ***kwds*)

A *classmethod* whose purpose is the additional configuration of later subclasses. It does nothing by default.

 _missing_(*cls*, *value*)

A *classmethod* meant for resolving values that aren't present in *cls*. It does nothing by default, though you can override it to supply your own lookup logic:

```python
>>> from enum import auto, StrEnum
>>> class Build(StrEnum):
...     DEBUG = auto()
...     OPTIMIZED = auto()
...     @classmethod
...     def _missing_(cls, value):
...         value = value.lower()
...         for member in cls:
...             if member.value == value:
...                 return member
...         return None
...
>>> Build.DEBUG.value
'debug'
>>> Build('deBUG')
<Build.DEBUG: 'debug'>

```

Added in version 3.6.

 __new__(*cls*, **args*, ***kwds*)

It does not exist by default. When provided — whether inside the enum class definition or within a mixin class (for example `int`) — every value supplied in the member assignment gets forwarded; for example

```python
>>> from enum import Enum
>>> class MyIntEnum(int, Enum):
...     TWENTYSIX = '1a', 16

```

produces the call `int('1a', 16)` and a value of `26` for the member.

Note

If you author a custom `__new__`, avoid `super().__new__` – instead call the appropriate `__new__` directly.

 __repr__(*self*)

Yields the string employed by *repr()* calls. By default this returns the *Enum* name, the member name, and the value, but you may override it:

```python
>>> from enum import auto, Enum
>>> class OtherStyle(Enum):
...     ALTERNATE = auto()
...     OTHER = auto()
...     SOMETHING_ELSE = auto()
...     def __repr__(self):
...         cls_name = self.__class__.__name__
...         return f'{cls_name}.{self.name}'
...
>>> OtherStyle.ALTERNATE, str(OtherStyle.ALTERNATE), f"{OtherStyle.ALTERNATE}"
(OtherStyle.ALTERNATE, 'OtherStyle.ALTERNATE', 'OtherStyle.ALTERNATE')

```

[Subject index](INDEX.md) · [Previous](enum-enum-dir-to-enum-enum-init.md) · [Continue](enum-enum-str-to-enum-enum-add-value-alias.md) · [Owning module, declaration or section: enum](enum-support-for-enumerations.md) · [Owning module, declaration or section: enum.Enum](enum-enum-class.md) · [Owning module, declaration or section: Data types](enum-enumtype-class.md)
