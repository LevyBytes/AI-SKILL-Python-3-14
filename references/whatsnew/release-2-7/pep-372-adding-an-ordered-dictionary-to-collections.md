# What’s New in Python 2.7 / PEP 372: Adding an Ordered Dictionary to collections — collections, configparser

### PEP 372: Adding an Ordered Dictionary to collections

Ordinary Python dictionaries walk through key/value pairs in an unspecified order. Through the years, several authors have built alternative implementations that recall the order in which the keys were first added. Drawing on the lessons of those implementations, 2.7 adds a new [`OrderedDict`](https://docs.python.org/3.14/library/collections.html#collections.OrderedDict) class to the [`collections`](https://docs.python.org/3.14/library/collections.html#module-collections) module.

The [`OrderedDict`](https://docs.python.org/3.14/library/collections.html#collections.OrderedDict) API exposes the identical interface as ordinary dictionaries, yet it walks through keys and values in an assured order tied to when each key was first added:

```python
>>> from collections import OrderedDict
>>> d = OrderedDict([('first', 1),
...                  ('second', 2),
...                  ('third', 3)])
>>> d.items()
[('first', 1), ('second', 2), ('third', 3)]

```

When a new entry replaces an entry that already exists, the original insertion slot stays the same:

```python
>>> d['second'] = 4
>>> d.items()
[('first', 1), ('second', 4), ('third', 3)]

```

Removing an entry and then adding it back will shift it to the end:

```python
>>> del d['second']
>>> d['second'] = 5
>>> d.items()
[('first', 1), ('third', 3), ('second', 5)]

```

The [`popitem()`](https://docs.python.org/3.14/library/collections.html#collections.OrderedDict.popitem) method carries an optional *last* argument whose default is `True`. When *last* is true, the key added most recently is returned and dropped; when it is false, the oldest key is chosen:

```python
>>> od = OrderedDict([(x,0) for x in range(20)])
>>> od.popitem()
(19, 0)
>>> od.popitem()
(18, 0)
>>> od.popitem(last=False)
(0, 0)
>>> od.popitem(last=False)
(1, 0)

```

When two ordered dictionaries are compared, both their keys and values are examined, and it is required that they share the same insertion order:

```python
>>> od1 = OrderedDict([('first', 1),
...                    ('second', 2),
...                    ('third', 3)])
>>> od2 = OrderedDict([('third', 3),
...                    ('first', 1),
...                    ('second', 2)])
>>> od1 == od2
False
>>> # Move 'third' key to the end
>>> del od2['third']; od2['third'] = 3
>>> od1 == od2
True

```

When an [`OrderedDict`](https://docs.python.org/3.14/library/collections.html#collections.OrderedDict) is compared against an ordinary dictionary, the insertion order is disregarded and only the keys and values are matched.

So how does the [`OrderedDict`](https://docs.python.org/3.14/library/collections.html#collections.OrderedDict) operate? It keeps a doubly linked list of keys, adding each new key onto the list as it gets inserted. A second dictionary maps each key to its matching list node, so that a deletion need not scan the whole linked list and thus stays *O*(1).

Several modules in the standard library now support the use of ordered dictionaries.

- The [`ConfigParser`](https://docs.python.org/3.14/library/configparser.html#module-configparser) module relies on them by default, which means configuration files can now be read, edited, and then written back out in their original order.

- The [`_asdict()`](https://docs.python.org/3.14/library/collections.html#collections.somenamedtuple._asdict) method on [`collections.namedtuple()`](https://docs.python.org/3.14/library/collections.html#collections.namedtuple) now hands back an ordered dictionary whose values follow the same order as the underlying tuple indices.

-

[Subject index](INDEX.md) · [Previous source section](python-3-1-features.md) · [Next source section](ordered-dictionaries-and-json-decoding.md) · [Release/subject declaration](the-future-for-python-2-x.md)
