# capsules C API: `PyCapsule_Destructor`, `PyCapsule_CheckExact()`, `PyCapsule_New()`, `PyCapsule_GetPointer()`, `PyCapsule_GetDestructor()`, `PyCapsule_GetContext()`, `PyCapsule_GetName()`, `PyCapsule_Import()`

type PyCapsule_Destructor

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

The type used for a capsule’s destructor callback. Its definition is:

```c
typedef void (*PyCapsule_Destructor)(PyObject *);

```

Consult `PyCapsule_New()` to learn how PyCapsule_Destructor callbacks behave.

 int PyCapsule_CheckExact([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p)

* Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

Yield true when the argument handed in is a `PyCapsule`. This call never fails.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyCapsule_New(void *pointer, const char *name, PyCapsule_Destructor destructor)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

Build a `PyCapsule` that wraps the *pointer*. The *pointer* argument is not allowed to be `NULL`.

Should the call fail, it sets an exception and gives back `NULL`.

The *name* string is permitted to be `NULL` or else a pointer to a valid C string. When it is non-`NULL`, that string has to remain alive longer than the capsule does. (Freeing it from within the *destructor*, however, is allowed.)

Provided the *destructor* argument is not `NULL`, it gets invoked with the capsule passed in as its argument at the moment the capsule is destroyed.

When the capsule is going to live as an attribute on a module, give the *name* in the form `modulename.attributename`. Doing so lets other modules pull in the capsule via `PyCapsule_Import()`.

 void *PyCapsule_GetPointer([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *capsule, const char *name)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Safe to call without external synchronization on distinct objects](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-distinct).*

Fetch the *pointer* held inside the capsule. Should it fail, an exception is set and `NULL` comes back.

The *name* parameter has to match the name kept in the capsule exactly. Where the capsule’s stored name is `NULL`, the *name* you supply must be `NULL` as well. To compare capsule names, Python falls back on the C function `strcmp()`.

 PyCapsule_Destructor PyCapsule_GetDestructor([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *capsule)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Safe to call without external synchronization on distinct objects](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-distinct).*

Give back the destructor presently held in the capsule. If it fails, an exception is set and the result is `NULL`.

A capsule is permitted to carry a `NULL` destructor, which leaves a `NULL` return value a bit ambiguous; lean on `PyCapsule_IsValid()` or [`PyErr_Occurred()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Occurred) to tell the cases apart.

 void *PyCapsule_GetContext([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *capsule)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Safe to call without external synchronization on distinct objects](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-distinct).*

Hand back whatever context is currently kept in the capsule. On a failure it sets an exception and yields `NULL`.

There is nothing wrong with a capsule holding a `NULL` context, though that renders a `NULL` return value somewhat unclear; reach for `PyCapsule_IsValid()` or [`PyErr_Occurred()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Occurred) to settle the matter.

 const char *PyCapsule_GetName([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *capsule)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Safe to call without external synchronization on distinct objects](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-distinct).*

Return the name presently held within the capsule. When it fails, an exception is set and `NULL` is returned.

It is entirely valid for a capsule to bear a `NULL` name, and that does make a `NULL` return value somewhat hard to read; turn to `PyCapsule_IsValid()` or [`PyErr_Occurred()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Occurred) to resolve the ambiguity.

 void *PyCapsule_Import(const char *name, int no_block)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Safe to call from multiple threads with external synchronization only](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-compatible).*

Bring in a pointer to a C object that sits in a module’s capsule attribute. Give the *name* parameter as the attribute’s complete path, like `module.attribute`. Whatever *name* the capsule stores has to match that string precisely.

The function breaks *name* apart at each `.` character and imports the leading element, then walks the rest by way of attribute lookups.

When it succeeds, the capsule’s internal *pointer* is returned. On a failure it sets an exception and gives back `NULL`.

Note

Where *name* refers to an attribute belonging to some submodule or subpackage, that submodule or subpackage has to have been imported beforehand through some other route (say, with [`PyImport_ImportModule()`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_ImportModule)) if the attribute lookups are to work.

Changed in version 3.3: *no_block* no longer does anything.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](capsules.md) · [Previous source contract](pycapsule-to-pycapsule-type.md) · [Following source contract](pycapsule-isvalid-to-pycapsule-setpointer.md)
