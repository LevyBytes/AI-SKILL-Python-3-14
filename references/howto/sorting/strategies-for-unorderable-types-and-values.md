# Strategies For Unorderable Types and Values

### Strategies For Unorderable Types and Values

Sorting can run into an assortment of type-related and value-related snags. The following tactics may come to the rescue:

- Turn input types that cannot be compared into strings before you sort them:

```pycon
>>> data = ['twelve', '11', 10]
>>> sorted(map(str, data))
['10', '11', 'twelve']

```

This step is required since the majority of comparisons spanning different types throw a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

- Strip out special values ahead of sorting:

```pycon
>>> from math import isnan
>>> from itertools import filterfalse
>>> data = [3.3, float('nan'), 1.1, 2.2]
>>> sorted(filterfalse(isnan, data))
[1.1, 2.2, 3.3]

```

You have to do this because the [IEEE-754 standard](https://en.wikipedia.org/wiki/IEEE_754) lays down that “Every NaN shall compare unordered with everything, including itself.”

In the same way, `None` can be pulled out of datasets too:

```pycon
>>> data = [3.3, None, 1.1, 2.2]
>>> sorted(x for x in data if x is not None)
[1.1, 2.2, 3.3]

```

This is called for because `None` cannot be compared against values of other types.

- Transform mapping types into sorted item lists prior to the sort:

```pycon
>>> data = [{'a': 1}, {'b': 2}]
>>> sorted(data, key=lambda d: sorted(d.items()))
[{'a': 1}, {'b': 2}]

```

This is required since comparing one dict against another throws a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

- Change set types into sorted lists ahead of sorting:

```pycon
>>> data = [{'a', 'b', 'c'}, {'b', 'c', 'd'}]
>>> sorted(map(sorted, data))
[['a', 'b', 'c'], ['b', 'c', 'd']]

```

This matters because the members held inside set types carry no fixed, predictable order. To illustrate, `list({'a', 'b'})` might yield either `['a', 'b']` or `['b', 'a']`.

[Subject index](INDEX.md) · [Previous source context](comparison-functions.md) · [Following source context](odds-and-ends.md)
