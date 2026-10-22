# functools: `functools.cmp_to_key()`

functools.cmp_to_key(*func*)

Convert an old-style comparison function into a [key function](https://docs.python.org/3.14/glossary.html#term-key-function). It works alongside utilities that take key functions (for instance [`sorted()`](https://docs.python.org/3.14/library/functions.html#sorted), [`min()`](https://docs.python.org/3.14/library/functions.html#min), [`max()`](https://docs.python.org/3.14/library/functions.html#max), [`heapq.nlargest()`](https://docs.python.org/3.14/library/heapq.html#heapq.nlargest), [`heapq.nsmallest()`](https://docs.python.org/3.14/library/heapq.html#heapq.nsmallest), [`itertools.groupby()`](https://docs.python.org/3.14/library/itertools.html#itertools.groupby)). Its main role is as a migration aid for code being ported from Python 2, which permitted comparison functions.

A comparison function is any callable taking two arguments that compares them and returns: something negative to signal less-than, zero to signal equality, or something positive to signal greater-than. By contrast, a key function accepts a single argument and produces a different value, which then serves as the sort key.

Example:

```python
sorted(iterable, key=cmp_to_key(locale.strcoll))  # locale-aware sort order

```

For worked sorting examples plus a short sorting walkthrough, refer to [Sorting Techniques](https://docs.python.org/3.14/howto/sorting.html#sortinghowto).

Added in version 3.2.

[Subject index](INDEX.md) · [Previous](cached-factorial-and-dataset-examples.md) · [Continue](cache-vowel-pep-and-fibonacci-examples.md) · [Owning module, declaration or section: functools](cached-factorial-and-dataset-examples.md)
