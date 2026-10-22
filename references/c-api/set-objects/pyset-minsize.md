# PySet_MINSIZE

### Deprecated API

 PySet_MINSIZE

A [soft deprecated](https://docs.python.org/3.14/glossary.html#term-soft-deprecated) constant that gives the size of an internal preallocated table within `PySetObject` instances.

It is recorded here purely for completeness, since nothing guarantees that a particular CPython version relies on preallocated tables of a fixed size. Within code that stays away from unstable set internals, `PySet_MINSIZE` may be swapped for a small constant such as `8`.

To obtain the size of a set, reach for `PySet_Size()` instead.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](set-objects.md) · [Previous source contract](pyset-contains-to-pyset-clear.md) · [Following source contract](../slice-objects/pyslice-type-to-pyslice-unpack.md)
