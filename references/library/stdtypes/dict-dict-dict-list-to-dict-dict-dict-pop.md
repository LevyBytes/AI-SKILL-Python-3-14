# stdtypes / dict: `list()`, `len()`, `iter()`, `clear()`, `copy()`, `fromkeys()`, `get()`, `items()`, `keys()`, `pop()`

list(d)

Hand back a list holding every key that the dictionary *d* uses.

 len(d)

Hand back how many items sit in the dictionary *d*.

 d[key]

Hand back the entry of *d* keyed by *key*. A [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) is raised should *key* be absent from the map.

When a dict subclass supplies a [`__missing__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__missing__) method and *key* is absent, the `d[key]` operation hands that method the key *key* as its argument. Whatever the `__missing__(key)` call then returns or raises becomes what the `d[key]` operation returns or raises. The `__missing__()` method is triggered by no other operation or method. With `__missing__()` left undefined, [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) is raised. Note that `__missing__()` has to be a method and may not be an instance variable:

```python
>>> class Counter(dict):
...     def __missing__(self, key):
...         return 0
...
>>> c = Counter()
>>> c['red']
0
>>> c['red'] += 1
>>> c['red']
1

```

The snippet above reproduces a portion of how [`collections.Counter`](https://docs.python.org/3.14/library/collections.html#collections.Counter) is built. [`collections.defaultdict`](https://docs.python.org/3.14/library/collections.html#collections.defaultdict) relies on a `__missing__()` method that differs from this one.

 d[key] = value

Assign *value* to `d[key]`.

 del d[key]

Delete `d[key]` out of *d*. A [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) is raised should *key* be absent from the map.

 key in d

Yield `True` when *d* holds a key *key*, and `False` otherwise.

 key not in d

The same as `not key in d`.

 iter(d)

Yield an iterator that walks the dictionary's keys. It serves as shorthand for `iter(d.keys())`.

 clear()

Clear every item out of the dictionary.

 copy()

Hand back a shallow copy of the dictionary.

 *classmethod *fromkeys(*iterable*, *value=None*, */*)

Build a fresh dictionary whose keys come from *iterable*, with each value set to *value*.

As a class method, `fromkeys()` produces a fresh dictionary. *value* falls back to `None`. Since every value points to one shared instance, it usually makes little sense for *value* to be a mutable object like an empty list. Should you need separate values, reach for a [dict comprehension](https://docs.python.org/3.14/reference/expressions.html#dict) instead.

 get(*key*, *default=None*, */*)

Hand back the value tied to *key* when *key* lives in the dictionary, otherwise hand back *default*. With no *default* supplied, it falls back to `None`, which means this method will never raise a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError).

 items()

Hand back a fresh view onto the dictionary's items (`(key, value)` pairs). Consult the documentation of view objects.

 keys()

Hand back a fresh view onto the dictionary's keys. Consult the documentation of view objects.

 pop(*key*, */*)

 pop(*key*, *default*, */*)

When *key* is present in the dictionary, drop it and hand back its value; otherwise hand back *default*. Should *default* be omitted and *key* be missing from the dictionary, a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) is raised.

[Subject index](INDEX.md) · [Previous](mapping-types-and-dict-construction.md) · [Continue](dict-dict-dict-popitem-to-dict-dict-dict-values.md) · [Owning module, declaration or section: dict; dict; dict](dict-class-to-dict-class.md) · [Owning module, declaration or section: Mapping Types — `dict`](dict-class-to-dict-class.md)
