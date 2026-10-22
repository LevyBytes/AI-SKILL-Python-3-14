# Data Types That Support Iterators

### Data Types That Support Iterators

We've already observed how lists and tuples support iterators. Indeed, every Python sequence type, strings included, will automatically support building an iterator.

Invoking [`iter()`](https://docs.python.org/3.14/library/functions.html#iter) on a dictionary yields an iterator that will cycle through the dictionary's keys:

```python
>>> m = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
...      'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
>>> for key in m:
...     print(key, m[key])
Jan 1
Feb 2
Mar 3
Apr 4
May 5
Jun 6
Jul 7
Aug 8
Sep 9
Oct 10
Nov 11
Dec 12

```

Be aware that as of Python 3.7, the order in which dictionaries iterate is guaranteed to match the insertion order. In prior releases, this behaviour wasn't specified and might differ across implementations.

Calling [`iter()`](https://docs.python.org/3.14/library/functions.html#iter) on a dictionary always cycles through the keys, but dictionaries provide methods returning other iterators. Should you wish to iterate over values or key/value pairs, you can call the [`values()`](https://docs.python.org/3.14/library/stdtypes.html#dict.values) or [`items()`](https://docs.python.org/3.14/library/stdtypes.html#dict.items) methods explicitly to obtain a suitable iterator.

The [`dict()`](https://docs.python.org/3.14/library/stdtypes.html#dict) constructor is able to take an iterator that yields a finite stream of `(key, value)` tuples:

```python
>>> L = [('Italy', 'Rome'), ('France', 'Paris'), ('US', 'Washington DC')]
>>> dict(iter(L))
{'Italy': 'Rome', 'France': 'Paris', 'US': 'Washington DC'}

```

Files support iteration too, by invoking the [`readline()`](https://docs.python.org/3.14/library/io.html#io.TextIOBase.readline) method until the file has no remaining lines. This lets you read each line of a file as follows:

```python
for line in file:
    # do something for each line
    ...

```

Sets can draw their contents from an iterable and permit you to iterate over the set's elements:

```python
>>> S = {2, 3, 5, 7, 11, 13}
>>> for i in S:
...     print(i)
2
3
5
7
11
13

```

[Subject index](INDEX.md) · [Previous source context](iterators.md) · [Following source context](generator-expression-and-comprehension-filtering.md)
