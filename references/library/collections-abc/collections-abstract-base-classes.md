# collections.abc - Collections Abstract Base Classes

### Collections Abstract Base Classes

The collections module offers the following [ABCs](https://docs.python.org/3.14/glossary.html#term-abstract-base-class):

| ABC | Inherits from | Abstract Methods | Mixin Methods |
| --- | --- | --- | --- |
| `Container` [1] |  | `__contains__` |  |
| `Hashable` [1] |  | `__hash__` |  |
| `Iterable` [1] [2] |  | `__iter__` |  |
| `Iterator` [1] | `Iterable` | `__next__` | `__iter__` |
| `Reversible` [1] | `Iterable` | `__reversed__` |  |
| `Generator` [1] | `Iterator` | `send`, `throw` | `close`, `__iter__`, `__next__` |
| `Sized` [1] |  | `__len__` |  |
| `Callable` [1] |  | `__call__` |  |
| `Collection` [1] | `Sized`, `Iterable`, `Container` | `__contains__`, `__iter__`, `__len__` |  |
| `Sequence` | `Reversible`, `Collection` | `__getitem__`, `__len__` | `__contains__`, `__iter__`, `__reversed__`, `index`, and `count` |
| `MutableSequence` | `Sequence` | `__getitem__`, `__setitem__`, `__delitem__`, `__len__`, `insert` | Inherited `Sequence` methods and `append`, `clear`, `reverse`, `extend`, `pop`, `remove`, and `__iadd__` |
| `ByteString` | `Sequence` | `__getitem__`, `__len__` | Inherited `Sequence` methods |
| `Set` | `Collection` | `__contains__`, `__iter__`, `__len__` | `__le__`, `__lt__`, `__eq__`, `__ne__`, `__gt__`, `__ge__`, `__and__`, `__or__`, `__sub__`, `__rsub__`, `__xor__`, `__rxor__` and `isdisjoint` |
| `MutableSet` | `Set` | `__contains__`, `__iter__`, `__len__`, `add`, `discard` | Inherited `Set` methods and `clear`, `pop`, `remove`, `__ior__`, `__iand__`, `__ixor__`, and `__isub__` |
| `Mapping` | `Collection` | `__getitem__`, `__iter__`, `__len__` | `__contains__`, `keys`, `items`, `values`, `get`, `__eq__`, and `__ne__` |
| `MutableMapping` | `Mapping` | `__getitem__`, `__setitem__`, `__delitem__`, `__iter__`, `__len__` | Inherited `Mapping` methods and `pop`, `popitem`, `clear`, `update`, and `setdefault` |
| `MappingView` | `Sized` |  | `__init__`, `__len__` and `__repr__` |
| `ItemsView` | `MappingView`, `Set` |  | `__contains__`, `__iter__` |
| `KeysView` | `MappingView`, `Set` |  | `__contains__`, `__iter__` |
| `ValuesView` | `MappingView`, `Collection` |  | `__contains__`, `__iter__` |
| `Awaitable` [1] |  | `__await__` |  |
| `Coroutine` [1] | `Awaitable` | `send`, `throw` | `close` |
| `AsyncIterable` [1] |  | `__aiter__` |  |
| `AsyncIterator` [1] | `AsyncIterable` | `__anext__` | `__aiter__` |
| `AsyncGenerator` [1] | `AsyncIterator` | `asend`, `athrow` | `aclose`, `__aiter__`, `__anext__` |
| `Buffer` [1] |  | `__buffer__` |  |

Footnotes

[Subject index](INDEX.md) · [Previous](collections-abc-abstract-base-classes-for-containers.md) · [Continue](collections-abc-container-class.md) · [Owning module, declaration or section: collections.abc](collections-abc-abstract-base-classes-for-containers.md)
