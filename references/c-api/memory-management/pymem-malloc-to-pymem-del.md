# Memory Interface

### Memory Interface

The function sets below, patterned on the ANSI C standard yet pinning down what happens when zero bytes are asked for, let you allocate and release memory drawn from the Python heap.

For the GIL-enabled build (the default build), the default memory allocator is the pymalloc memory allocator, while for the [free-threaded build](https://docs.python.org/3.14/glossary.html#term-free-threaded-build) the default is instead the mimalloc memory allocator.

Warning

When you call these functions, an [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) has to be present.

Changed in version 3.6: pymalloc, rather than the system `malloc()`, now serves as the default allocator.

Changed in version 3.13: Within the [free-threaded](https://docs.python.org/3.14/glossary.html#term-free-threading) build, mimalloc has become the default allocator.

 void *PyMem_Malloc(size_t n)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Reserves *n* bytes, handing back a void* pointer aimed at the freshly allocated memory; on a failed request, `NULL` comes back instead.

Should you ask for zero bytes, you get back a separate non-`NULL` pointer where feasible, just as though `PyMem_Malloc(1)` had run in its place. No initialization of the memory occurs at all.

 void *PyMem_Calloc(size_t nelem, size_t elsize)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.7.*

Reserves *nelem* elements, each one *elsize* bytes wide, and yields a void* pointer aimed at that allocated memory, or `NULL` when the request cannot be met. Zeros fill the memory.

Should you ask for zero elements, or for elements whose size is zero bytes, you get back a separate non-`NULL` pointer where feasible, just as though `PyMem_Calloc(1, 1)` had run in its place.

Added in version 3.5.

 void *PyMem_Realloc(void *p, size_t n)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Adjusts the block that *p* references so it spans *n* bytes. Up to the lesser of the prior and fresh sizes, whatever the block held remains intact.

Where *p* holds `NULL`, the call behaves just like `PyMem_Malloc(n)`; and when *n* instead comes out to zero, the block gets resized rather than released, with a non-`NULL` pointer returned.

Except when *p* is `NULL`, it has to be a value handed back by an earlier call to `PyMem_Malloc()`, `PyMem_Realloc()` or `PyMem_Calloc()`.

Should the request fail, `PyMem_Realloc()` hands back `NULL`, and *p* stays a valid pointer to the earlier memory area.

 void PyMem_Free(void *p)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Releases the block that *p* references, where *p* must be a value an earlier `PyMem_Malloc()`, `PyMem_Realloc()` or `PyMem_Calloc()` call produced. Failing that, or if `PyMem_Free(p)` already ran earlier, behavior is undefined.

If *p* is `NULL`, no operation is performed.

For convenience there are the type-oriented macros below. Note that *TYPE* stands for any C type.

 PyMem_New(TYPE, n)

Behaves like `PyMem_Malloc()`, except the amount reserved is `(n * sizeof(TYPE))` bytes. Hands back a pointer already cast to `TYPE*`. No initialization of that memory takes place at all.

 PyMem_Resize(p, TYPE, n)

Behaves like `PyMem_Realloc()`, except the block is brought to `(n * sizeof(TYPE))` bytes. Hands back a pointer already cast to `TYPE*`. Once it returns, *p* points to the new memory area, or holds `NULL` should the operation fail.

This is a C preprocessor macro; *p* is always reassigned. Keep a copy of the original *p* value so that you do not leak memory while dealing with errors.

 void PyMem_Del(void *p)

Same as `PyMem_Free()`.

[Subject index](INDEX.md) · [Previous source contract](pymem-rawmalloc-to-pymem-rawfree.md) · [Following source contract](deprecated-aliases.md)
