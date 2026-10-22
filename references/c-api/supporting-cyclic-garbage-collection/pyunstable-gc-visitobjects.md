# Querying Garbage Collector State

### Querying Garbage Collector State

For asking after information about the garbage collector, the C-API exposes the interface below.

 void PyUnstable_GC_VisitObjects(gcvisitobjects_t callback, void *arg)

 *This is [Unstable API](https://docs.python.org/3.14/c-api/stable.html#unstable-c-api). It may change without warning in minor releases.*

Apply the given *callback* to every live GC-capable object. The *arg* you supply is forwarded into each call of *callback*.

Warning

Should the callback allocate or free objects, whether they end up visited is left undefined.

While this runs, garbage collection stays off. Forcing a collection from within the callback can produce undefined behaviour — for instance visiting the same objects more than once, or skipping some entirely.

Added in version 3.12.

 typedef int (*gcvisitobjects_t)([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *object, void *arg)

The type of the visitor function destined for `PyUnstable_GC_VisitObjects()`. Its *arg* matches the *arg* given to `PyUnstable_GC_VisitObjects`. Hand back `1` to keep iterating or `0` to halt. Any other return value is reserved for the time being, so returning something else has undefined behavior.

Added in version 3.12.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](py-tpflags-have-gc-to-pyobject-gc-newvar.md) · [Previous source contract](pygc-collect-to-pygc-isenabled.md) · [Following source contract](../generator-objects/generator-objects.md)
