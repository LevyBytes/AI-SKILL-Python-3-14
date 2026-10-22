# Raw Memory Interface

### Raw Memory Interface

Each of the function sets below wraps the system allocator. Because these functions are thread-safe, there is no need for a [thread state](https://docs.python.org/3.14/glossary.html#term-thread-state) to be [attached](https://docs.python.org/3.14/glossary.html#term-attached-thread-state).

The functions the default raw memory allocator relies on are `malloc()`, `calloc()`, `realloc()` and `free()`; when zero bytes are asked for, it issues `malloc(1)` (or `calloc(1, 1)`).

Added in version 3.4.

 void *PyMem_RawMalloc(size_t n)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.13.*

Reserves *n* bytes, handing back a void* pointer aimed at the freshly allocated memory; on a failed request, `NULL` comes back instead.

Should you ask for zero bytes, you get back a separate non-`NULL` pointer where feasible, just as though `PyMem_RawMalloc(1)` had run in its place. No initialization of the memory occurs at all.

 void *PyMem_RawCalloc(size_t nelem, size_t elsize)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.13.*

Reserves *nelem* elements, each one *elsize* bytes wide, and yields a void* pointer aimed at that allocated memory, or `NULL` when the request cannot be met. Zeros fill the memory.

Should you ask for zero elements, or for elements whose size is zero bytes, you get back a separate non-`NULL` pointer where feasible, just as though `PyMem_RawCalloc(1, 1)` had run in its place.

Added in version 3.5.

 void *PyMem_RawRealloc(void *p, size_t n)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.13.*

Adjusts the block that *p* references so it spans *n* bytes. Up to the lesser of the prior and fresh sizes, whatever the block held remains intact.

Where *p* holds `NULL`, the call behaves just like `PyMem_RawMalloc(n)`; and when *n* instead comes out to zero, the block gets resized rather than released, with a non-`NULL` pointer returned.

Except when *p* is `NULL`, it has to be a value handed back by an earlier call to `PyMem_RawMalloc()`, `PyMem_RawRealloc()` or `PyMem_RawCalloc()`.

Should the request fail, `PyMem_RawRealloc()` hands back `NULL`, and *p* stays a valid pointer to the earlier memory area.

 void PyMem_RawFree(void *p)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.13.*

Releases the block that *p* references, where *p* must be a value an earlier `PyMem_RawMalloc()`, `PyMem_RawRealloc()` or `PyMem_RawCalloc()` call produced. Failing that, or if `PyMem_RawFree(p)` already ran earlier, behavior is undefined.

If *p* is `NULL`, no operation is performed.

[Subject index](INDEX.md) · [Previous source contract](allocator-domains.md) · [Following source contract](pymem-malloc-to-pymem-del.md)
