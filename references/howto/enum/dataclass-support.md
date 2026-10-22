# Dataclass support

### Dataclass support

Where the base is a [`dataclass`](https://docs.python.org/3.14/library/dataclasses.html#dataclasses.dataclass), the [`__repr__()`](https://docs.python.org/3.14/library/enum.html#enum.Enum.__repr__) drops the name of the inherited class. As an example:

```python
>>> from dataclasses import dataclass, field
>>> @dataclass
... class CreatureDataMixin:
...     size: str
...     legs: int
...     tail: bool = field(repr=False, default=True)
...
>>> class Creature(CreatureDataMixin, Enum):
...     BEETLE = 'small', 6
...     DOG = 'medium', 4
...
>>> Creature.DOG
<Creature.DOG: size='medium', legs=4>

```

Pass the [`dataclass()`](https://docs.python.org/3.14/library/dataclasses.html#dataclasses.dataclass) argument `repr=False` if you want the standard [`repr()`](https://docs.python.org/3.14/library/functions.html#repr).

Changed in version 3.12: The value area now lists only the dataclass fields, leaving out the dataclass' name.

Note

Applying the [`dataclass()`](https://docs.python.org/3.14/library/dataclasses.html#dataclasses.dataclass) decorator to [`Enum`](https://docs.python.org/3.14/library/enum.html#enum.Enum) along with its subclasses isn't supported. No errors will surface, but at runtime it yields thoroughly bizarre outcomes, like members comparing equal to one another:

```python
>>> @dataclass               # don't do this: it does not make any sense
... class Color(Enum):
...    RED = 1
...    BLUE = 2
...
>>> Color.RED is Color.BLUE
False
>>> Color.RED == Color.BLUE  # problem is here: they should not be equal
True

```

[Subject index](INDEX.md) · [Previous source context](restricted-enum-subclassing.md) · [Following source context](pickling.md)
