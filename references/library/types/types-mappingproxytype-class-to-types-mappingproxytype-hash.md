# types: `types.MappingProxyType`, `iter()`, `len()`, `copy()`, `get()`, `items()`, `keys()`, `values()`, `reversed()`, `hash()`

*class *types.MappingProxyType(*mapping*)

A read-only proxy onto a mapping. It exposes a live view of the mapping’s entries, so that any change to the mapping shows through in the view.

A `MappingProxyType` is [generic](https://docs.python.org/3.14/library/typing.html#generics) over two types, which stand for (in order) the types of the keys and the values of the underlying mapping.

Added in version 3.3.

Changed in version 3.9: Revised to handle the fresh union (`|`) operator out of [**PEP 584**](https://peps.python.org/pep-0584/); it merely hands the work off to the underlying mapping.

 key in proxy

Return `True` when the underlying mapping holds a key *key*, otherwise `False`.

 proxy[key]

Return the underlying mapping’s item whose key is *key*. Raises a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) when *key* is absent from the underlying mapping.

 iter(proxy)

Return an iterator across the underlying mapping’s keys. This is shorthand for `iter(proxy.keys())`.

 len(proxy)

Return how many items the underlying mapping holds.

 copy()

Return a shallow copy of the underlying mapping.

 get(*key*[, *default*])

Return the value tied to *key* when *key* is present in the underlying mapping, otherwise *default*. When *default* is omitted, it falls back to `None`, so this method never raises a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError).

 items()

Return a fresh view of the underlying mapping’s items (`(key, value)` pairs).

 keys()

Return a fresh view of the underlying mapping’s keys.

 values()

Return a fresh view of the underlying mapping’s values.

 reversed(proxy)

Return a reverse iterator across the underlying mapping’s keys.

Added in version 3.9.

 hash(proxy)

Return a hash for the underlying mapping.

Added in version 3.12.

[Subject index](INDEX.md) · [Previous](types-frametype-to-types-memberdescriptortype.md) · [Continue](types-capsuletype-class.md) · [Owning module, declaration or section: types](types-dynamic-type-creation-and-names-for-built-in-types.md) · [Owning module, declaration or section: Standard Interpreter Types](types-nonetype-class-to-types-asyncgeneratortype.md)
