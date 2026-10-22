# Dictionary view objects

### Dictionary view objects

What `dict.keys()`, `dict.values()` and `dict.items()` hand back are *view objects*. They expose a live view onto the dictionary's entries, so any change to the dictionary shows up in the view.

You can iterate dictionary views to obtain their underlying data, and they accommodate membership tests too:

 len(dictview)

Hand back how many entries the dictionary holds.

 iter(dictview)

Yield an iterator that walks the dictionary's keys, values or items (each item shown as a `(key, value)` tuple).

The keys and values come up in insertion order during iteration. That makes it possible to assemble `(value, key)` pairs through [`zip()`](https://docs.python.org/3.14/library/functions.html#zip): `pairs = zip(d.values(), d.keys())`. The very same list can also be built with `pairs = [(v, k) for (k, v) in d.items()]`.

Should you iterate views while inserting or removing dictionary entries, a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) may result or some entries may be skipped during iteration.

Changed in version 3.7: Insertion order for dictionaries is now a guarantee.

 x in dictview

Yield `True` when *x* sits among the underlying dictionary's keys, values or items (for items, *x* ought to be a `(key, value)` tuple).

 reversed(dictview)

Yield a reverse iterator that walks the dictionary's keys, values or items. The view is traversed in the reverse of insertion order.

Changed in version 3.8: Dictionary views are now reversible.

 dictview.mapping

Hand back a [`types.MappingProxyType`](https://docs.python.org/3.14/library/types.html#types.MappingProxyType) that encloses the original dictionary the view points at.

Added in version 3.10.

Keys views behave like sets because their entries are both unique and [hashable](https://docs.python.org/3.14/glossary.html#term-hashable). Items views gain set-like operations as well, given that the (key, value) pairs are unique and the keys are hashable. Provided every value in an items view is hashable too, that items view can interoperate with other sets. (Values views do not count as set-like, since their entries are typically not unique.) On set-like views, the full set of operations declared by the abstract base class [`collections.abc.Set`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Set) is at your disposal (for example, `==`, `<`, or `^`). When set operators are applied, set-like views will take any iterable as the other operand, whereas sets themselves only accept sets as input.

An example of dictionary view usage:

```python
>>> dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
>>> keys = dishes.keys()
>>> values = dishes.values()

>>> # iteration
>>> n = 0
>>> for val in values:
...     n += val
...
>>> print(n)
504

>>> # keys and values are iterated over in the same order (insertion order)
>>> list(keys)
['eggs', 'sausage', 'bacon', 'spam']
>>> list(values)
[2, 1, 1, 500]

>>> # view objects are dynamic and reflect dict changes
>>> del dishes['eggs']
>>> del dishes['sausage']
>>> list(keys)
['bacon', 'spam']

>>> # set operations
>>> keys & {'eggs', 'bacon', 'salad'}
{'bacon'}
>>> keys ^ {'sausage', 'juice'} == {'juice', 'sausage', 'bacon', 'spam'}
True
>>> keys | ['juice', 'juice', 'juice'] == {'bacon', 'spam', 'juice'}
True

>>> # get back a read-only proxy for the original dictionary
>>> values.mapping
mappingproxy({'bacon': 1, 'spam': 500})
>>> values.mapping['spam']
500

```

[Subject index](INDEX.md) · [Previous](dict-dict-dict-popitem-to-dict-dict-dict-values.md) · [Continue](contextmanager-enter-to-contextmanager-exit.md)
