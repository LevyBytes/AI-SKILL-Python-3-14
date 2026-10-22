# enumerate

enumerate(*iterable*, *start=0*)

Produces an enumerate object. *iterable* has to be a sequence, an [iterator](https://docs.python.org/3.14/glossary.html#term-iterator), or any other object capable of iteration. Each call to the [`__next__()`](https://docs.python.org/3.14/library/stdtypes.html#iterator.__next__) method on the iterator that `enumerate()` hands back yields a tuple pairing a counter (beginning at *start*, whose default is 0) together with the value pulled from iterating across *iterable*.

```python
>>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
>>> list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
>>> list(enumerate(seasons, start=1))
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

```

Equivalent to:

```python
def enumerate(iterable, start=0):
    n = start
    for elem in iterable:
        yield n, elem
        n += 1

```

[Builtin task index](INDEX.md).
