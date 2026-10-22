# collections / Counter objects: `elements()`, `most_common()`, `subtract()`, `total()`, `fromkeys()`

elements()

Hand back an iterator that repeats each element as often as its count dictates. The elements come out in the order they were first met. Should an element's count fall below one, `elements()` will skip over it.

```python
>>> c = Counter(a=4, b=2, c=0, d=-2)
>>> sorted(c.elements())
['a', 'a', 'a', 'a', 'b', 'b']

```

 most_common(*n=None*)

Hand back a list of the *n* most frequent elements paired with their counts, running from most frequent to least. When *n* is left out or set to `None`, `most_common()` hands back *all* elements held in the counter. Elements sharing the same count appear in the order they were first met:

```python
>>> Counter('abracadabra').most_common(3)
[('a', 5), ('b', 2), ('r', 2)]

```

 subtract(***kwargs*)

 subtract(*iterable*, */*, ***kwargs*)

 subtract(*mapping*, */*, ***kwargs*)

Counts are removed using an *iterable* or another *mapping* (or counter). It works like [`dict.update()`](https://docs.python.org/3.14/library/stdtypes.html#dict.update) except that it deducts counts rather than overwriting them. Either the inputs or the outputs can be zero or negative.

```python
>>> c = Counter(a=4, b=2, c=0, d=-2)
>>> d = Counter(a=1, b=2, c=3, d=4)
>>> c.subtract(d)
>>> c
Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})

```

Added in version 3.2.

 total()

Add up all of the counts.

```python
>>> c = Counter(a=10, b=5, c=0)
>>> c.total()
15

```

Added in version 3.10.

The standard dictionary methods are on hand for `Counter` objects, save for two that behave differently with counters.

 fromkeys(*iterable*)

For `Counter` objects, this class method has not been implemented.

[Subject index](INDEX.md) · [Previous](collections-counter-class-to-collections-counter-class.md) · [Continue](collections-counter-update-to-collections-counter-update.md) · [Owning module, declaration or section: collections](collections-container-datatypes.md) · [Owning module, declaration or section: collections.Counter; collections.Counter; collections.Counter](collections-counter-class-to-collections-counter-class.md) · [Owning module, declaration or section: `Counter` objects](collections-counter-class-to-collections-counter-class.md)
