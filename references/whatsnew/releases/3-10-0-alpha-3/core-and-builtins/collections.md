# Python 3.10.0 alpha 3 / core and builtins / collections

[bpo-42536](https://bugs.python.org/issue?@action=redirect&bpo=42536): A number of built-in and standard library types now guarantee that their internal result tuples are always watched by the [garbage collector](https://docs.python.org/3.14/glossary.html#term-garbage-collection):

  - [`collections.OrderedDict.items()`](https://docs.python.org/3.14/library/collections.html#collections.OrderedDict)

  - [`dict.items()`](https://docs.python.org/3.14/library/stdtypes.html#dict.items)

  - [`enumerate()`](https://docs.python.org/3.14/library/functions.html#enumerate)

  - [`functools.reduce()`](https://docs.python.org/3.14/library/functools.html#functools.reduce)

  - [`itertools.combinations()`](https://docs.python.org/3.14/library/itertools.html#itertools.combinations)

  - [`itertools.combinations_with_replacement()`](https://docs.python.org/3.14/library/itertools.html#itertools.combinations_with_replacement)

  - [`itertools.permutations()`](https://docs.python.org/3.14/library/itertools.html#itertools.permutations)

  - [`itertools.product()`](https://docs.python.org/3.14/library/itertools.html#itertools.product)

  - [`itertools.zip_longest()`](https://docs.python.org/3.14/library/itertools.html#itertools.zip_longest)

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
