# Object allocators

### Object allocators

The function sets below, patterned on the ANSI C standard yet pinning down what happens when zero bytes are asked for, let you allocate and release memory drawn from the Python heap.

Note

When the allocating functions of this domain are intercepted by the techniques laid out in the Customize Memory Allocators section, nothing promises that the memory these allocators return can be cast successfully into a Python object.

By default the object allocator relies on the pymalloc memory allocator. For the [free-threaded](https://docs.python.org/3.14/glossary.html#term-free-threading) build, though, the mimalloc memory allocator takes that default role.

Warning

When you call these functions, an [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) has to be present.

 void *PyObject_Malloc(size_t n)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Reserves *n* bytes, handing back a void* pointer aimed at the freshly allocated memory; on a failed request, `NULL` comes back instead.

Should you ask for zero bytes, you get back a separate non-`NULL` pointer where feasible, just as though `PyObject_Malloc(1)` had run in its place. No initialization of the memory occurs at all.

 void *PyObject_Calloc(size_t nelem, size_t elsize)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.7.*

Reserves *nelem* elements, each one *elsize* bytes wide, and yields a void* pointer aimed at that allocated memory, or `NULL` when the request cannot be met. Zeros fill the memory.

Should you ask for zero elements, or for elements whose size is zero bytes, you get back a separate non-`NULL` pointer where feasible, just as though `PyObject_Calloc(1, 1)` had run in its place.

Added in version 3.5.

 void *PyObject_Realloc(void *p, size_t n)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Adjusts the block that *p* references so it spans *n* bytes. Up to the lesser of the prior and fresh sizes, whatever the block held remains intact.

Where *p* holds `NULL`, the call behaves just like `PyObject_Malloc(n)`; and when *n* instead comes out to zero, the block gets resized rather than released, with a non-`NULL` pointer returned.

Except when *p* is `NULL`, it has to be a value handed back by an earlier call to `PyObject_Malloc()`, `PyObject_Realloc()` or `PyObject_Calloc()`.

Should the request fail, `PyObject_Realloc()` hands back `NULL`, and *p* stays a valid pointer to the earlier memory area.

 void PyObject_Free(void *p)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Releases the block that *p* references, where *p* must be a value an earlier `PyObject_Malloc()`, `PyObject_Realloc()` or `PyObject_Calloc()` call produced. Failing that, or if `PyObject_Free(p)` already ran earlier, behavior is undefined.

If *p* is `NULL`, no operation is performed.

Never invoke this directly to release an object's memory; reach for the type's [`tp_free`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_free) slot instead.

Steer clear of using this on memory that [`PyObject_GC_New`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyObject_GC_New) or [`PyObject_GC_NewVar`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyObject_GC_NewVar) allocated; turn to [`PyObject_GC_Del()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyObject_GC_Del) instead.

See also

- For memory that types supporting garbage collection have allocated, [`PyObject_GC_Del()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyObject_GC_Del) plays the same role this function does.

- `PyObject_Malloc()`

- `PyObject_Realloc()`

- `PyObject_Calloc()`

- [`PyObject_New`](https://docs.python.org/3.14/c-api/allocation.html#c.PyObject_New)

- [`PyObject_NewVar`](https://docs.python.org/3.14/c-api/allocation.html#c.PyObject_NewVar)

-

[Subject index](INDEX.md) · [Previous source contract](deprecated-aliases.md) · [Following source contract](pytype-genericalloc.md)
