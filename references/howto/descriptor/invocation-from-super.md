# Invocation from super

### Invocation from super

The logic for super’s dotted lookup sits in the [`__getattribute__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattribute__) method belonging to the object that [`super()`](https://docs.python.org/3.14/library/functions.html#super) returns.

A dotted lookup like `super(A, obj).m` scans `obj.__class__.__mro__` for the base class `B` that comes right after `A`, then yields `B.__dict__['m'].__get__(obj, A)`. When `m` is not a descriptor, it comes back unchanged.

You can read the complete C implementation in `super_getattro()` within [Objects/typeobject.c](https://github.com/python/cpython/tree/3.14/Objects/typeobject.c). A pure Python equivalent appears in [Guido’s Tutorial](https://www.python.org/download/releases/2.2.3/descrintro/#cooperation).

[Subject index](INDEX.md) · [Following source continuation](descriptor-invocation-logic-summary.md) · [Previous source context](invocation-from-a-class.md) · [Following source context](descriptor-invocation-logic-summary.md)
