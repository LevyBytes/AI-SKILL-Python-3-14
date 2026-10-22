# What’s New In Python 3.5 / PEP 448 - Additional Unpacking Generalizations

### PEP 448 - Additional Unpacking Generalizations

[**PEP 448**](https://peps.python.org/pep-0448/) broadens where the `*` iterable unpacking operator and the `**` dictionary unpacking operator may appear. You can now apply any number of unpackings within [function calls](https://docs.python.org/3.14/reference/expressions.html#calls):

```python
>>> print(*[1], *[2], 3, *[4, 5])
1 2 3 4 5

>>> def fn(a, b, c, d):
...     print(a, b, c, d)
...

>>> fn(**{'a': 1, 'c': 3}, **{'b': 2, 'd': 4})
1 2 3 4

```

In the same way, displays for tuples, lists, sets, and dictionaries permit several unpackings (refer to [Expression lists](https://docs.python.org/3.14/reference/expressions.html#exprlists) and [Dictionary displays](https://docs.python.org/3.14/reference/expressions.html#dict)):

```python
>>> *range(4), 4
(0, 1, 2, 3, 4)

>>> [*range(4), 4]
[0, 1, 2, 3, 4]

>>> {*range(4), 4, *(5, 6, 7)}
{0, 1, 2, 3, 4, 5, 6, 7}

>>> {'x': 1, **{'y': 2}}
{'x': 1, 'y': 2}

```

See also

[**PEP 448**](https://peps.python.org/pep-0448/) – Additional Unpacking Generalizations

PEP authored by Joshua Landau; the implementation came from Neil Girdhar, Thomas Wouters, and Joshua Landau.

[Subject index](INDEX.md) · [Previous source section](pep-465-a-dedicated-infix-operator-for-matrix-multiplication.md) · [Next source section](pep-461-percent-formatting-support-for-bytes-and-bytearray.md) · [Release/subject declaration](summary-release-highlights.md)
