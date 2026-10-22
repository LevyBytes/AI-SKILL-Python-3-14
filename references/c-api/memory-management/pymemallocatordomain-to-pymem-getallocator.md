# memory management C API: Allocator domains and allocator inspection

type PyMemAllocatorDomain

Enum used to identify an allocator domain. Domains:

 PYMEM_DOMAIN_RAW

Functions:

- `PyMem_RawMalloc()`

- `PyMem_RawRealloc()`

- `PyMem_RawCalloc()`

- `PyMem_RawFree()`

 PYMEM_DOMAIN_MEM

Functions:

- `PyMem_Malloc()`,

- `PyMem_Realloc()`

- `PyMem_Calloc()`

- `PyMem_Free()`

 PYMEM_DOMAIN_OBJ

Functions:

- `PyObject_Malloc()`

- `PyObject_Realloc()`

- `PyObject_Calloc()`

- `PyObject_Free()`

 void PyMem_GetAllocator(PyMemAllocatorDomain domain, PyMemAllocatorEx *allocator)

Get the memory block allocator of the specified domain.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pymemallocatorex.md) · [Following source contract](pymem-setallocator-to-pymem-setupdebughooks.md)
