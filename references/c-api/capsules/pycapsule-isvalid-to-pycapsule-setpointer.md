# capsules C API: `PyCapsule_IsValid()`, `PyCapsule_SetContext()`, `PyCapsule_SetDestructor()`, `PyCapsule_SetName()`, `PyCapsule_SetPointer()`

int PyCapsule_IsValid([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *capsule, const char *name)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Safe to call without external synchronization on distinct objects](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-distinct).*

Works out whether *capsule* qualifies as a valid capsule. To be valid, a capsule must be non-`NULL`, clear `PyCapsule_CheckExact()`, hold a non-`NULL` pointer, and carry an internal name equal to the *name* parameter. (Refer to `PyCapsule_GetPointer()` for the way capsule names get compared.)

Put differently, once `PyCapsule_IsValid()` yields a true value, every accessor call — any function whose name begins with `PyCapsule_Get` — is assured of succeeding.

Give back a nonzero value when the object is valid and its name agrees with the one supplied; otherwise `0` is returned. This call cannot fail.

 int PyCapsule_SetContext([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *capsule, void *context)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Safe to call without external synchronization on distinct objects](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-distinct).*

Point the context pointer held in *capsule* at *context*.

A success yields `0`; a failure returns a nonzero value and sets an exception.

 int PyCapsule_SetDestructor([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *capsule, PyCapsule_Destructor destructor)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Safe to call without external synchronization on distinct objects](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-distinct).*

Assign *destructor* as the destructor kept in *capsule*.

It returns `0` when it succeeds, or a nonzero value with an exception set when it fails.

 int PyCapsule_SetName([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *capsule, const char *name)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Safe to call without external synchronization on distinct objects](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-distinct).*

Make *name* the name held in *capsule*. When it is non-`NULL`, the name has to stay alive beyond the capsule. Should the *name* previously kept in the capsule have been other than `NULL`, no effort is made to free it.

Success produces `0`, while failure produces a nonzero value along with a set exception.

 int PyCapsule_SetPointer([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *capsule, void *pointer)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Safe to call without external synchronization on distinct objects](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-distinct).*

Point the void pointer held in *capsule* at *pointer*. That pointer is not allowed to be `NULL`.

On success the result is `0`; on failure it is a nonzero value with an exception set.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](capsules.md) · [Owning structure and shared ABI conditions](pycapsule-destructor-to-pycapsule-import.md) · [Following source contract](../cell-objects/cell-objects.md)
