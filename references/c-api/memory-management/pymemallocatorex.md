# type PyMemAllocatorEx

<a id="customize-memory-allocators"></a>

Customize Memory Allocators: Added in version 3.4.

type PyMemAllocatorEx

A structure that characterizes a memory block allocator. Its fields are these:

| Field | Meaning |
| --- | --- |
| `void *ctx` | user context passed as first argument |
| `void* malloc(void *ctx, size_t size)` | allocate a memory block |
| `void* calloc(void *ctx, size_t nelem, size_t elsize)` | allocate a memory block initialized with zeros |
| `void* realloc(void *ctx, void *ptr, size_t new_size)` | allocate or resize a memory block |
| `void free(void *ctx, void *ptr)` | free a memory block |

Changed in version 3.5: What had been the `PyMemAllocator` structure took the name `PyMemAllocatorEx`, and an additional `calloc` field joined it.

[Subject index](INDEX.md) · [Following source contract](pymemallocatordomain-to-pymem-getallocator.md)
