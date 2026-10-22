# Invocation from a class

### Invocation from a class

The logic behind a dotted lookup like `A.x` lives in `type.__getattribute__()`. Its steps mirror those of `object.__getattribute__()`, except that the search of the instance dictionary gives way to a traversal of the class’s [method resolution order](https://docs.python.org/3.14/glossary.html#term-method-resolution-order).

When a descriptor is located, it is called as `desc.__get__(None, A)`.

You can read the complete C implementation in `type_getattro()` and `_PyType_Lookup()` within [Objects/typeobject.c](https://github.com/python/cpython/tree/3.14/Objects/typeobject.c).

[Subject index](INDEX.md) · [Previous source context](invocation-from-an-instance.md) · [Following source context](invocation-from-super.md)
