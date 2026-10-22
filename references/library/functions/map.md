# map

map(*function*, *iterable*, */*, **iterables*, *strict=False*)

Yield an iterator that runs *function* over each item of *iterable*, emitting the outcomes. When extra *iterables* arguments are supplied, *function* has to accept that count of arguments and gets applied to the items drawn from every iterable simultaneously. Given multiple iterables, the iterator halts once the shortest iterable runs out. When *strict* is `True` and one iterable runs out ahead of the rest, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) gets raised. For situations where the function inputs come pre-grouped into argument tuples, refer to [`itertools.starmap()`](https://docs.python.org/3.14/library/itertools.html#itertools.starmap).

Changed in version 3.14: Added the *strict* parameter.

[Builtin task index](INDEX.md).
