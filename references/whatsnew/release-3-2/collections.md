# What's New In Python 3.2 / collections - collections

### collections

- The [`collections.Counter`](https://docs.python.org/3.14/library/collections.html#collections.Counter) class now offers two flavors of in-place subtraction: the long-standing *-=* operator for [saturating subtraction](https://en.wikipedia.org/wiki/Saturation_arithmetic) plus the fresh [`subtract()`](https://docs.python.org/3.14/library/collections.html#collections.Counter.subtract) method for ordinary subtraction. The first fits [multisets](https://en.wikipedia.org/wiki/Multiset), which carry only positive counts, while the second works better for scenarios that permit negative counts:

```python
>>> from collections import Counter
>>> tally = Counter(dogs=5, cats=3)
>>> tally -= Counter(dogs=2, cats=8)    # saturating subtraction
>>> tally
Counter({'dogs': 3})

```

```python
>>> tally = Counter(dogs=5, cats=3)
>>> tally.subtract(dogs=2, cats=8)      # regular subtraction
>>> tally
Counter({'dogs': 3, 'cats': -5})

```

(Contributed by Raymond Hettinger.)

- A new method [`move_to_end()`](https://docs.python.org/3.14/library/collections.html#collections.OrderedDict.move_to_end) belongs to the [`collections.OrderedDict`](https://docs.python.org/3.14/library/collections.html#collections.OrderedDict) class; it accepts an existing key and shifts it to either the first or the last slot in the ordered sequence.

By default an item moves to the final slot. That amounts to refreshing an entry via `od[k] = od.pop(k)`.

Having a quick move-to-end operation helps when resequencing entries. For instance, an ordered dictionary can record access order by aging entries running from the oldest up to the most recently used.

```python
>>> from collections import OrderedDict
>>> d = OrderedDict.fromkeys(['a', 'b', 'X', 'd', 'e'])
>>> list(d)
['a', 'b', 'X', 'd', 'e']
>>> d.move_to_end('X')
>>> list(d)
['a', 'b', 'd', 'e', 'X']

```

(Contributed by Raymond Hettinger.)

- Two fresh methods, [`count()`](https://docs.python.org/3.14/library/collections.html#collections.deque.count) and [`reverse()`](https://docs.python.org/3.14/library/collections.html#collections.deque.reverse), were added to the [`collections.deque`](https://docs.python.org/3.14/library/collections.html#collections.deque) class, rendering it a closer stand-in for [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) objects:

```python
>>> from collections import deque
>>> d = deque('simsalabim')
>>> d.count('s')
2
>>> d.reverse()
>>> d
deque(['m', 'i', 'b', 'a', 'l', 'a', 's', 'm', 'i', 's'])

```

(Contributed by Raymond Hettinger.)

[Subject index](INDEX.md) · [Previous source section](itertools.md) · [Next source section](threading.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)
