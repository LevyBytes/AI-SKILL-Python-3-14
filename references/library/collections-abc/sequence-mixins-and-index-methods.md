# collections.abc / Detailed Descriptions: `collections.abc.Sequence`, `collections.abc.MutableSequence`, `collections.abc.ByteString`, `index()`

*class *collections.abc.Sequence

 *class *collections.abc.MutableSequence

 *class *collections.abc.ByteString

ABCs for read-only and mutable [sequences](https://docs.python.org/3.14/glossary.html#term-sequence).

Implementation note: A number of the mixin methods — among them [`__iter__()`](https://docs.python.org/3.14/library/stdtypes.html#container.__iter__), [`__reversed__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__reversed__), and [`index()`](https://docs.python.org/3.14/library/stdtypes.html#sequence.index) — invoke the underlying [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__) method over and over. As a result, when `__getitem__()` runs in constant time, those mixin methods perform linearly; but when the underlying method is itself linear (as happens with a linked list), the mixins become quadratic and will probably have to be overridden.

 index(*value*, *start=0*, *stop=None*)

Return first index of *value*.

Raises [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) if the value is not present.

Supporting the *start* and *stop* arguments is optional, but recommended.

Changed in version 3.5: Acceptance of the *stop* and *start* arguments was added to the [`index()`](https://docs.python.org/3.14/library/stdtypes.html#sequence.index) method.

Deprecated since version 3.12, will be removed in version 3.17: Deprecation now applies to the `ByteString` ABC.

To check at runtime whether `obj` realizes the [buffer protocol](https://docs.python.org/3.14/c-api/buffer.html#bufferobjects), call `isinstance(obj, collections.abc.Buffer)`. Within type annotations, reach for `Buffer`, or else a union naming outright whichever types your code handles (e.g., `bytes | bytearray | memoryview`).

The intent behind `ByteString` was originally that it would be an abstract class acting as a supertype over both [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) and [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray). Yet because the ABC was never given any methods, learning that an object was an instance of `ByteString` never genuinely revealed anything useful about that object. Additional widespread buffer types such as [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) likewise were never treated as subtypes of `ByteString` (neither at runtime nor by static type checkers).

See [**PEP 688**](https://peps.python.org/pep-0688/#current-options) for more details.

[Subject index](INDEX.md) · [Previous](collections-abc-generator-class.md) · [Continue](collections-abc-set-class-to-collections-abc-mutableset-class.md) · [Owning module, declaration or section: collections.abc](collections-abc-abstract-base-classes-for-containers.md) · [Owning module, declaration or section: Collections Abstract Base Classes ??? Detailed Descriptions](collections-abc-container-class.md)
