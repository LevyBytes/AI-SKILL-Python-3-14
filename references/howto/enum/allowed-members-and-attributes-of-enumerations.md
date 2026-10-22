# Allowed members and attributes of enumerations

### Allowed members and attributes of enumerations

The bulk of the examples so far rely on integers as enumeration values. Integers are compact and convenient (and the Functional API supplies them by default), though nothing forces them. For most use-cases nobody cares what an enumeration's actual value is. But when the value *does* matter, enumerations are free to hold any values at all.

Being Python classes, enumerations can carry methods and special methods like any class. Given this enumeration:

```python
>>> class Mood(Enum):
...     FUNKY = 1
...     HAPPY = 3
...
...     def describe(self):
...         # self is the member here
...         return self.name, self.value
...
...     def __str__(self):
...         return 'my custom str! {0}'.format(self.value)
...
...     @classmethod
...     def favorite_mood(cls):
...         # cls here is the enumeration
...         return cls.HAPPY
...

```

Then:

```python
>>> Mood.favorite_mood()
<Mood.HAPPY: 3>
>>> Mood.HAPPY.describe()
('HAPPY', 3)
>>> str(Mood.FUNKY)
'my custom str! 1'

```

Here is what's permitted: any name both opening and closing with one underscore is claimed by enum and off-limits; every other attribute declared inside an enumeration turns into a member of it, save for special methods ([`__str__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__str__), [`__add__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__add__), and the like), descriptors (methods count as descriptors too), and any variable names enumerated in [`_ignore_`](https://docs.python.org/3.14/library/enum.html#enum.Enum._ignore_).

Note: should your enumeration declare [`__new__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__new__) and/or [`__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__), whatever value(s) you assign the enum member get forwarded to those methods. Refer to Planet for a worked case.

Note

When defined, the [`__new__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__new__) method serves while the Enum members are being created; afterward Enum swaps in its own `__new__()`, which handles looking up members that already exist once the class is built. See When to use __new__() vs. __init__() for further detail.

[Subject index](INDEX.md) · [Previous source context](comparisons.md) · [Following source context](restricted-enum-subclassing.md)
