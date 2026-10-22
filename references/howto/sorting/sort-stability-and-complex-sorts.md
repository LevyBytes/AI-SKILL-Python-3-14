# Sort Stability and Complex Sorts

### Sort Stability and Complex Sorts

Sorting is promised to be [stable](https://en.wikipedia.org/wiki/Sorting_algorithm#Stability). In practice this means that whenever several records share an identical key, the order they began in is kept intact.

```pycon
>>> data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
>>> sorted(data, key=itemgetter(0))
[('blue', 1), ('blue', 2), ('red', 1), ('red', 2)]

```

Observe that the pair of *blue* entries hold onto the sequence they started in, which assures that `('blue', 1)` always comes ahead of `('blue', 2)`.

That handy guarantee makes it possible to assemble elaborate orderings through a sequence of separate sort passes. Say you want the student records arranged by descending *grade* and then ascending *age*: run the *age* pass first, and afterward sort once more on *grade*:

```pycon
>>> s = sorted(student_objects, key=attrgetter('age'))     # sort on secondary key
>>> sorted(s, key=attrgetter('grade'), reverse=True)       # now sort on primary key, descending
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

```

You can factor this out into a wrapper function that accepts a list plus tuples of field-and-direction, ordering the data over several successive passes.

```pycon
>>> def multisort(xs, specs):
...     for key, reverse in reversed(specs):
...         xs.sort(key=attrgetter(key), reverse=reverse)
...     return xs

>>> multisort(list(student_objects), (('grade', True), ('age', False)))
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

```

Python's [Timsort](https://en.wikipedia.org/wiki/Timsort) algorithm handles repeated sorts efficiently, since it is able to exploit whatever ordering a dataset already happens to contain.

[Subject index](INDEX.md) · [Previous source context](ascending-and-descending.md) · [Following source context](decorate-sort-undecorate.md)
