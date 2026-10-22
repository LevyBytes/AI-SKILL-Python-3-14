# What’s New In Python 3.5 / collections — collections, collections.abc, pickle

### collections

The [`OrderedDict`](https://docs.python.org/3.14/library/collections.html#collections.OrderedDict) class has been reimplemented in C, yielding a speedup of 4 to 100 times. (Contributed by Eric Snow in [bpo-16991](https://bugs.python.org/issue?@action=redirect&bpo=16991).)

`OrderedDict.items()`, `OrderedDict.keys()`, and `OrderedDict.values()` views henceforth permit [`reversed()`](https://docs.python.org/3.14/library/functions.html#reversed) iteration. (Contributed by Serhiy Storchaka in [bpo-19505](https://bugs.python.org/issue?@action=redirect&bpo=19505).)

The [`deque`](https://docs.python.org/3.14/library/collections.html#collections.deque) class henceforth defines [`index()`](https://docs.python.org/3.14/library/collections.html#collections.deque.index), [`insert()`](https://docs.python.org/3.14/library/collections.html#collections.deque.insert), and [`copy()`](https://docs.python.org/3.14/library/collections.html#collections.deque.copy), while also honoring the `+` and `*` operators. As a result deques register as a [`MutableSequence`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.MutableSequence) and become more readily interchangeable with lists. (Contributed by Raymond Hettinger in [bpo-23704](https://bugs.python.org/issue?@action=redirect&bpo=23704).)

Docstrings emitted by [`namedtuple()`](https://docs.python.org/3.14/library/collections.html#collections.namedtuple) can henceforth be modified:

```python
Point = namedtuple('Point', ['x', 'y'])
Point.__doc__ += ': Cartesian coordinate'
Point.x.__doc__ = 'abscissa'
Point.y.__doc__ = 'ordinate'

```

(Contributed by Berker Peksag in [bpo-24064](https://bugs.python.org/issue?@action=redirect&bpo=24064).)

The [`UserString`](https://docs.python.org/3.14/library/collections.html#collections.UserString) class henceforth supplies the [`__getnewargs__()`](https://docs.python.org/3.14/library/pickle.html#object.__getnewargs__), [`__rmod__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__rmod__), [`casefold()`](https://docs.python.org/3.14/library/stdtypes.html#str.casefold), [`format_map()`](https://docs.python.org/3.14/library/stdtypes.html#str.format_map), [`isprintable()`](https://docs.python.org/3.14/library/stdtypes.html#str.isprintable), and [`maketrans()`](https://docs.python.org/3.14/library/stdtypes.html#str.maketrans) methods, matching the equivalent methods on [`str`](https://docs.python.org/3.14/library/stdtypes.html#str). (Contributed by Joe Jevnik in [bpo-22189](https://bugs.python.org/issue?@action=redirect&bpo=22189).)

[Subject index](INDEX.md) · [Previous source section](code.md) · [Next source section](collections-abc.md) · [Release/subject declaration](summary-release-highlights.md)
