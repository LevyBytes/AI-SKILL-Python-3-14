# stdtypes / dict: `popitem()`, `reversed()`, `setdefault()`, `update()`, `values()`

popitem()

Drop a `(key, value)` pair from the dictionary and hand it back. The order in which pairs come out is LIFO.

The `popitem()` method comes in handy for destructively walking through a dictionary, a pattern common in set algorithms. Should the dictionary hold nothing, a call to `popitem()` raises a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError).

Changed in version 3.7: The LIFO ordering is now a guarantee. Earlier releases had `popitem()` hand back some arbitrary key/value pair.

 reversed(d)

Yield a reverse iterator that walks the dictionary's keys. It serves as shorthand for `reversed(d.keys())`.

Added in version 3.8.

 setdefault(*key*, *default=None*, */*)

Should *key* already be in the dictionary, hand back its value. If it is not, add *key* set to *default* and hand back *default*. The fallback for *default* is `None`.

 update(***kwargs*)

 update(*mapping*, */*, ***kwargs*)

 update(*iterable*, */*, ***kwargs*)

Refresh the dictionary using the key/value pairs drawn from *mapping* or *iterable* together with *kwargs*, replacing keys that already exist. Return `None`.

`update()` takes either a second object exposing a `keys()` method (whereupon [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__) is called for each key that method yields) or an iterable made of key/value pairs (given as tuples or as other length-two iterables). When keyword arguments come into play, the dictionary then absorbs those key/value pairs: `d.update(red=1, blue=2)`.

 values()

Hand back a fresh view onto the dictionary's values. Consult the documentation of view objects.

Comparing one `dict.values()` view against another for equality invariably yields `False`. The same holds true even when a `dict.values()` view is compared with itself:

```python
>>> d = {'a': 1}
>>> d.values() == d.values()
False

```

 d | other

Build a fresh dictionary whose keys and values combine those of *d* and *other*, both of which have to be dictionaries. Where *d* and *other* hold the same keys, the values from *other* win out.

Added in version 3.9.

 d |= other

Refresh the dictionary *d* with keys and values drawn from *other*, which can be a [mapping](https://docs.python.org/3.14/glossary.html#term-mapping) or else an [iterable](https://docs.python.org/3.14/glossary.html#term-iterable) of key/value pairs. Where *d* and *other* hold the same keys, the values from *other* win out.

Added in version 3.9.

Both dictionaries and dictionary views can be reversed.

```python
>>> d = {"one": 1, "two": 2, "three": 3, "four": 4}
>>> d
{'one': 1, 'two': 2, 'three': 3, 'four': 4}
>>> list(reversed(d))
['four', 'three', 'two', 'one']
>>> list(reversed(d.values()))
[4, 3, 2, 1]
>>> list(reversed(d.items()))
[('four', 4), ('three', 3), ('two', 2), ('one', 1)]

```

Changed in version 3.8: Dictionaries are now reversible.

See also

[`types.MappingProxyType`](https://docs.python.org/3.14/library/types.html#types.MappingProxyType) can be used to create a read-only view of a `dict`.

See also

For detailed information on thread-safety guarantees for `dict` objects, see [Thread safety for dict objects](https://docs.python.org/3.14/library/threadsafety.html#thread-safety-dict).

[Subject index](INDEX.md) · [Previous](dict-dict-dict-list-to-dict-dict-dict-pop.md) · [Continue](len-to-dictview-mapping.md) · [Owning module, declaration or section: dict; dict; dict](dict-class-to-dict-class.md) · [Owning module, declaration or section: Mapping Types - `dict`](dict-class-to-dict-class.md)
