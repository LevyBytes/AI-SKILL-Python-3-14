# bisect - Examples

### Examples

For numeric table lookups, the `bisect()` function comes in handy. The example here applies `bisect()` to map an exam score (for instance) onto a letter grade, driven by a set of ordered numeric breakpoints: anything from 90 upward is an 'A', 80 through 89 is a 'B', and onward in that vein:

```python
>>> def grade(score):
...     i = bisect([60, 70, 80, 90], score)
...     return "FDCBA"[i]
...
>>> [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
['F', 'A', 'C', 'C', 'B', 'A', 'A']

```

Lists of tuples work fine with the `bisect()` and `insort()` functions too. You can put the *key* argument to use pulling out the field that orders records within a table:

```python
>>> from collections import namedtuple
>>> from operator import attrgetter
>>> from bisect import bisect, insort
>>> from pprint import pprint

>>> Movie = namedtuple('Movie', ('name', 'released', 'director'))

>>> movies = [
...     Movie('Jaws', 1975, 'Spielberg'),
...     Movie('Titanic', 1997, 'Cameron'),
...     Movie('The Birds', 1963, 'Hitchcock'),
...     Movie('Aliens', 1986, 'Cameron')
... ]

>>> # Find the first movie released after 1960
>>> by_year = attrgetter('released')
>>> movies.sort(key=by_year)
>>> movies[bisect(movies, 1960, key=by_year)]
Movie(name='The Birds', released=1963, director='Hitchcock')

>>> # Insert a movie while maintaining sort order
>>> romance = Movie('Love Story', 1970, 'Hiller')
>>> insort(movies, romance, key=by_year)
>>> pprint(movies)
[Movie(name='The Birds', released=1963, director='Hitchcock'),
 Movie(name='Love Story', released=1970, director='Hiller'),
 Movie(name='Jaws', released=1975, director='Spielberg'),
 Movie(name='Aliens', released=1986, director='Cameron'),
 Movie(name='Titanic', released=1997, director='Cameron')]

```

When the key function is costly, you can sidestep repeated calls by searching a list of keys worked out beforehand to land on a record's index:

```python
>>> data = [('red', 5), ('blue', 1), ('yellow', 8), ('black', 0)]
>>> data.sort(key=lambda r: r[1])       # Or use operator.itemgetter(1).
>>> keys = [r[1] for r in data]         # Precompute a list of keys.
>>> data[bisect_left(keys, 0)]
('black', 0)
>>> data[bisect_left(keys, 1)]
('blue', 1)
>>> data[bisect_left(keys, 5)]
('red', 5)
>>> data[bisect_left(keys, 8)]
('yellow', 8)

```

[Subject index](INDEX.md) · [Previous](searching-sorted-lists.md) · [Continue](../builtins/builtins-built-in-objects.md) · [Owning module, declaration or section: bisect](bisect-bisect-left-to-bisect-insort.md)
