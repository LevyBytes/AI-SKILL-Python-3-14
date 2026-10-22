# Restricted Enum subclassing

### Restricted Enum subclassing

Each new [`Enum`](https://docs.python.org/3.14/library/enum.html#enum.Enum) class is allowed one base enum class, at most one concrete data type, and however many [`object`](https://docs.python.org/3.14/library/functions.html#object)-based mixin classes you require. These base classes go in this order:

```python
class EnumName([mix-in, ...,] [data-type,] base-enum):
    pass

```

Furthermore, you can subclass an enumeration only when it declares no members. Hence this is not permitted:

```python
>>> class MoreColor(Color):
...     PINK = 17
...
Traceback (most recent call last):
...
TypeError: <enum 'MoreColor'> cannot extend <enum 'Color'>

```

Whereas this is fine:

```python
>>> class Foo(Enum):
...     def some_behavior(self):
...         pass
...
>>> class Bar(Foo):
...     HAPPY = 1
...     SAD = 2
...

```

Were subclassing of member-bearing enums permitted, it would break several crucial invariants governing types and their instances. Even so, letting a family of enumerations share some shared behavior is reasonable. (Refer to OrderedEnum for an example.)

[Subject index](INDEX.md) · [Previous source context](allowed-members-and-attributes-of-enumerations.md) · [Following source context](dataclass-support.md)
