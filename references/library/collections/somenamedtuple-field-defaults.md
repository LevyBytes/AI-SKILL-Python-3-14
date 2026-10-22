# collections: `somenamedtuple._field_defaults`

somenamedtuple._field_defaults

Dictionary that pairs field names with their default values.

```pycon
>>> Account = namedtuple('Account', ['type', 'balance'], defaults=[0])
>>> Account._field_defaults
{'balance': 0}
>>> Account('premium')
Account(type='premium', balance=0)

```

When the name of the field you want sits in a string, fetch it through the [`getattr()`](https://docs.python.org/3.14/library/functions.html#getattr) function:

```python
>>> getattr(p, 'x')
11

```

Turning a dictionary into a named tuple is done with the double-star-operator (as covered in [Unpacking Argument Lists](https://docs.python.org/3.14/tutorial/controlflow.html#tut-unpacking-arguments)):

```python
>>> d = {'x': 11, 'y': 22}
>>> Point(**d)
Point(x=11, y=22)

```

Because a named tuple is an ordinary Python class, extending or tweaking its behavior through a subclass is simple. Below is how you might tack on a computed field together with a fixed-width print format:

```pycon
>>> class Point(namedtuple('Point', ['x', 'y'])):
...     __slots__ = ()
...     @property
...     def hypot(self):
...         return (self.x ** 2 + self.y ** 2) ** 0.5
...     def __str__(self):
...         return 'Point: x=%6.3f  y=%6.3f  hypot=%6.3f' % (self.x, self.y, self.hypot)

>>> for p in Point(3, 4), Point(14, 5/7):
...     print(p)
Point: x= 3.000  y= 4.000  hypot= 5.000
Point: x=14.000  y= 0.714  hypot=14.018

```

In the subclass above, `__slots__` is assigned an empty tuple. Doing so holds memory usage down by stopping instance dictionaries from being created.

For tacking on new, stored fields, subclassing is the wrong tool. Just build a brand-new named tuple type out of the `_fields` attribute instead:

```python
>>> Point3D = namedtuple('Point3D', Point._fields + ('z',))

```

To tailor docstrings, assign directly to the `__doc__` fields:

```python
>>> Book = namedtuple('Book', ['id', 'title', 'authors'])
>>> Book.__doc__ += ': Hardcover book in active collection'
>>> Book.id.__doc__ = '13-digit ISBN'
>>> Book.title.__doc__ = 'Title of first printing'
>>> Book.authors.__doc__ = 'List of authors sorted by last name'

```

Changed in version 3.5: Property docstrings became writeable.

See also

- Consult [`typing.NamedTuple`](https://docs.python.org/3.14/library/typing.html#typing.NamedTuple) when you want to attach type hints to named tuples. On top of that it offers a graceful syntax built around the [`class`](https://docs.python.org/3.14/reference/compound_stmts.html#class) keyword:

```python
class Component(NamedTuple):
    part_number: int
    weight: float
    description: Optional[str] = None

```

- Consult [`types.SimpleNamespace()`](https://docs.python.org/3.14/library/types.html#types.SimpleNamespace) when you want a mutable namespace backed by a dictionary underneath rather than by a tuple.

- The [`dataclasses`](https://docs.python.org/3.14/library/dataclasses.html#module-dataclasses) module supplies a decorator plus helper functions that attach auto-generated special methods to classes you define yourself.

[Subject index](INDEX.md) · [Previous](somenamedtuple-asdict-to-somenamedtuple-fields.md) · [Continue](ordered-dictionary-class-contract.md) · [Owning module, declaration or section: collections](collections-container-datatypes.md) · [Owning module, declaration or section: `namedtuple()` Factory Function for Tuples with Named Fields](collections-namedtuple.md)
