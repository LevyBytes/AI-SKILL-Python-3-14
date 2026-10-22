# Customize pymalloc Arena Allocator

<a id="customize-pymalloc-arena-allocator"></a>

Customize pymalloc Arena Allocator: Added in version 3.4.

type PyObjectArenaAllocator

A structure that characterizes an arena allocator. It is made up of three fields:

| Field | Meaning |
| --- | --- |
| `void *ctx` | the caller's context, handed over as the first argument |
| `void* alloc(void *ctx, size_t size)` | reserve one arena spanning size bytes |
| `void free(void *ctx, void *ptr, size_t size)` | free an arena |

 void PyObject_GetArenaAllocator(PyObjectArenaAllocator *allocator)

Get the arena allocator.

 void PyObject_SetArenaAllocator(PyObjectArenaAllocator *allocator)

Set the arena allocator.

[Subject index](INDEX.md) · [Following source contract](the-mimalloc-allocator.md)
