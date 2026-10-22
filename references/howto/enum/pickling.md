# Pickling

### Pickling

You can pickle enumerations and unpickle them again:

```python
>>> from test.test_enum import Fruit
>>> from pickle import dumps, loads
>>> Fruit.TOMATO is loads(dumps(Fruit.TOMATO))
True

```

The standard pickling caveats hold: any picklable enum has to live at a module's top level, because unpickling needs it to be importable out of that module.

Note

Under pickle protocol version 4, pickling enums tucked inside other classes is straightforward.

By supplying [`__reduce_ex__()`](https://docs.python.org/3.14/library/pickle.html#object.__reduce_ex__) on the enumeration class, you can adjust how its members are pickled/unpickled. By default it's by-value, but enums carrying intricate values might prefer by-name:

```python
>>> import enum
>>> class MyEnum(enum.Enum):
...     __reduce_ex__ = enum.pickle_by_enum_name

```

Note

Choosing by-name with flags is discouraged, because aliases without names won't unpickle.

[Subject index](INDEX.md) · [Previous source context](dataclass-support.md) · [Following source context](functional-enum-pickling-module-and-qualname.md)
