# filter

filter(*function*, *iterable*, */*)

Build an iterator out of the elements of *iterable* where *function* evaluates to true. *iterable* can be a sequence, a container that supports iteration, or an iterator. When *function* is `None`, the identity function applies, meaning every element of *iterable* that is false gets dropped.

Observe that `filter(function, iterable)` matches the generator expression `(item for item in iterable if function(item))` when function is not `None`, and matches `(item for item in iterable if item)` when function is `None`.

Consult [`itertools.filterfalse()`](https://docs.python.org/3.14/library/itertools.html#itertools.filterfalse) for the complementary function that yields the elements of *iterable* where *function* is false.

[Builtin task index](INDEX.md).
