# What's New In Python 3.0 / Views And Iterators Instead Of Lists - itertools

### Views And Iterators Instead Of Lists

A handful of familiar APIs have stopped handing back lists:

- The [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) methods [`dict.keys()`](https://docs.python.org/3.14/library/stdtypes.html#dict.keys), [`dict.items()`](https://docs.python.org/3.14/library/stdtypes.html#dict.items) and [`dict.values()`](https://docs.python.org/3.14/library/stdtypes.html#dict.values) now hand back ?views? rather than lists. To give one case, the following has stopped working: `k = d.keys(); k.sort()`. Reach for `k = sorted(d)` instead (which also runs under Python 2.5 and is every bit as efficient).

- On top of that, the methods `dict.iterkeys()`, `dict.iteritems()` and `dict.itervalues()` have been dropped.

- The functions [`map()`](https://docs.python.org/3.14/library/functions.html#map) and [`filter()`](https://docs.python.org/3.14/library/functions.html#filter) now yield iterators. When you genuinely require a list and every input sequence shares the same length, the fast remedy is to wrap `map()` with [`list()`](https://docs.python.org/3.14/library/stdtypes.html#list), as in `list(map(...))`; a stronger remedy, though, is frequently a list comprehension (above all when the source code reaches for [`lambda`](https://docs.python.org/3.14/reference/expressions.html#lambda)), or reshaping the code so no list is required whatsoever. A thorny case is `map()` called purely for the function's side effects; here the right rewrite is an ordinary [`for`](https://docs.python.org/3.14/reference/compound_stmts.html#for) loop (because building a list would simply waste effort).

When the input sequences differ in length, [`map()`](https://docs.python.org/3.14/library/functions.html#map) halts once the shortest sequence runs out. To match `map()` from Python 2.x exactly, additionally wrap the sequences with [`itertools.zip_longest()`](https://docs.python.org/3.14/library/itertools.html#itertools.zip_longest), so that `map(func, *sequences)` turns into `list(map(func, itertools.zip_longest(*sequences)))`.

- The behavior [`range()`](https://docs.python.org/3.14/library/stdtypes.html#range) shows today mirrors the former `xrange()`, with the added benefit of handling values of arbitrary size. That older name is gone now.

- The function [`zip()`](https://docs.python.org/3.14/library/functions.html#zip) hands back an iterator now.

[Subject index](INDEX.md) · [Previous source section](print-is-a-function.md) · [Next source section](ordering-comparisons.md) · [Release/subject declaration](common-stumbling-blocks.md)
