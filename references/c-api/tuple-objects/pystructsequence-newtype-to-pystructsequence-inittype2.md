# tuple objects C API: `PyStructSequence_NewType()`, `PyStructSequence_InitType()`, `PyStructSequence_InitType2()`

### Struct Sequence Objects

Struct sequence objects serve as the C counterpart of [`namedtuple()`](https://docs.python.org/3.14/library/collections.html#collections.namedtuple) objects — that is, a sequence whose items are reachable through attributes as well. Building a struct sequence begins with creating a particular struct sequence type.

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) *PyStructSequence_NewType(PyStructSequence_Desc *desc)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Build a fresh struct sequence type out of the data held in *desc*, as detailed below. The resulting type's instances can be produced via `PyStructSequence_New()`.

Return `NULL` with an exception set on failure.

 void PyStructSequence_InitType([PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) *type, PyStructSequence_Desc *desc)

Initialize a struct sequence type *type* in place from *desc*.

 int PyStructSequence_InitType2([PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) *type, PyStructSequence_Desc *desc)

Like `PyStructSequence_InitType()`, but returns `0` on success and `-1` with an exception set on failure.

Added in version 3.4.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pytupleobject-to-pytuple-setitem.md) · [Previous source contract](pytuple-set-item-to-pytuple-resize.md) · [Following source contract](pystructsequence-desc-to-n-in-sequence.md)
