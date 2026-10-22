# collections: `somenamedtuple._asdict()`, `somenamedtuple._replace()`, `somenamedtuple._fields`

somenamedtuple._asdict()

Hand back a new [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) that pairs each field name with its matching value:

```pycon
>>> p = Point(x=11, y=22)
>>> p._asdict()
{'x': 11, 'y': 22}

```

Changed in version 3.1: Returns an `OrderedDict` instead of a regular [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict).

Changed in version 3.8: Now returns a plain [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) rather than an `OrderedDict`. Beginning with Python 3.7, ordinary dicts keep their order by guarantee. Should you still need what `OrderedDict` adds, the recommended fix is to coerce the output into whichever type you want: `OrderedDict(nt._asdict())`.

 somenamedtuple._replace(***kwargs*)

Hand back a fresh instance of the named tuple in which the named fields are swapped for new values:

```python
>>> p = Point(x=11, y=22)
>>> p._replace(x=33)
Point(x=33, y=22)

>>> for partnum, record in inventory.items():
...     inventory[partnum] = record._replace(price=newprices[partnum], timestamp=time.now())

```

The generic function [`copy.replace()`](https://docs.python.org/3.14/library/copy.html#copy.replace) supports named tuples as well.

Changed in version 3.13: Raise [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) instead of [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) for invalid keyword arguments.

 somenamedtuple._fields

Tuple of strings enumerating the field names. Handy for introspection and for spinning up new named tuple types out of existing ones.

```pycon
>>> p._fields            # view the field names
('x', 'y')

>>> Color = namedtuple('Color', 'red green blue')
>>> Pixel = namedtuple('Pixel', Point._fields + Color._fields)
>>> Pixel(11, 22, 128, 255, 0)
Pixel(x=11, y=22, red=128, green=255, blue=0)

```

[Subject index](INDEX.md) · [Previous](collections-namedtuple.md) · [Continue](somenamedtuple-field-defaults.md) · [Owning module, declaration or section: collections](collections-container-datatypes.md) · [Owning module, declaration or section: `namedtuple()` Factory Function for Tuples with Named Fields](collections-namedtuple.md)
