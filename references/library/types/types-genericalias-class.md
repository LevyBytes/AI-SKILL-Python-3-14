# types: `types.GenericAlias`

*class *types.GenericAlias(*t_origin*, *t_args*)

The type of [parameterized generics](https://docs.python.org/3.14/library/stdtypes.html#types-genericalias) like `list[int]`.

`t_origin` ought to be a non-parameterized generic class, `list`, `tuple` or `dict` for instance. `t_args` ought to be a [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple) (its length possibly 1) of the types that parameterize `t_origin`:

```python
>>> from types import GenericAlias

>>> list[int] == GenericAlias(list, (int,))
True
>>> dict[str, int] == GenericAlias(dict, (str, int))
True

```

Added in version 3.9.

Changed in version 3.9.2: This type can now be subclassed.

See also

[Generic Alias Types](https://docs.python.org/3.14/library/stdtypes.html#types-genericalias)

Thorough documentation covering instances of `types.GenericAlias`

[**PEP 585**](https://peps.python.org/pep-0585/) - Type Hinting Generics In Standard Collections

Bringing in the `types.GenericAlias` class

[Subject index](INDEX.md) · [Previous](types-ellipsistype-class.md) · [Continue](types-uniontype-class.md) · [Owning module, declaration or section: types](types-dynamic-type-creation-and-names-for-built-in-types.md) · [Owning module, declaration or section: Standard Interpreter Types](types-nonetype-class-to-types-asyncgeneratortype.md)
