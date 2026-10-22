# What’s New In Python 3.8 / itertools — itertools

> (Contributed by Victor Stinner in [bpo-18748](https://bugs.python.org/issue?@action=redirect&bpo=18748).)

### itertools

An optional *initial* keyword argument has been added to the [`itertools.accumulate()`](https://docs.python.org/3.14/library/itertools.html#itertools.accumulate) function for naming a starting value:

```python
>>> from itertools import accumulate
>>> list(accumulate([10, 5, 30, 15], initial=1000))
[1000, 1010, 1015, 1045, 1060]

```

[Subject index](INDEX.md) · [Previous source section](io.md) · [Next source section](json-tool.md) · [Release/subject declaration](assignment-expressions.md)
