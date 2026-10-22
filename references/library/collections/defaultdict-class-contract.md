# collections: `collections.defaultdict`

### `defaultdict` objects

 *class *collections.defaultdict(*default_factory=None*, */*, ***kwargs*)

 *class *collections.defaultdict(*default_factory*, *mapping*, */*, ***kwargs*)

 *class *collections.defaultdict(*default_factory*, *iterable*, */*, ***kwargs*)

Hand back a new dictionary-like object. `defaultdict` derives from the built-in [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) class. It supersedes a single method and introduces one writable instance variable. Everything else behaves exactly as the `dict` class does and is left undocumented here.

The opening argument supplies the starting value for the `default_factory` attribute, which falls back to `None`. Every other argument is handled just as though it had been handed to the [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) constructor, keyword arguments included.

`defaultdict`s are [generic](https://docs.python.org/3.14/library/typing.html#generics) over two types, denoting (in order) the types of the dictionary’s keys and values.

Beyond the standard [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) operations, `defaultdict` objects offer the following method:

[Subject index](INDEX.md) · [Previous](deque-recipes.md) · [Continue](collections-defaultdict-missing.md) · [Owning module, declaration or section: collections](collections-container-datatypes.md)
