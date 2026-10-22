# Sorting Basics

### Sorting Basics

Producing a plain ascending order takes almost no effort: simply invoke the [`sorted()`](https://docs.python.org/3.14/library/functions.html#sorted) function, which hands back a fresh ordered list:

```pycon
>>> sorted([5, 2, 3, 1, 4])
[1, 2, 3, 4, 5]

```

An alternative is the [`list.sort()`](https://docs.python.org/3.14/library/stdtypes.html#list.sort) method, which rearranges the list directly in place (and hands back `None`, so as not to mislead you). It tends to be a bit clumsier than [`sorted()`](https://docs.python.org/3.14/library/functions.html#sorted) - though when you have no further use for the unsorted version, it is marginally faster.

```pycon
>>> a = [5, 2, 3, 1, 4]
>>> a.sort()
>>> a
[1, 2, 3, 4, 5]

```

A further distinction: the [`list.sort()`](https://docs.python.org/3.14/library/stdtypes.html#list.sort) method exists exclusively on lists, whereas the [`sorted()`](https://docs.python.org/3.14/library/functions.html#sorted) function happily takes any iterable.

```pycon
>>> sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})
[1, 2, 3, 4, 5]

```

[Subject index](INDEX.md) · [Previous source context](sorting-techniques.md) · [Following source context](key-functions.md)
