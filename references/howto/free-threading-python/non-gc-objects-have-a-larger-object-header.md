# Non-GC objects have a larger object header

#### Non-GC objects have a larger object header

A distinct [`PyObject`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) layout is used by the free-threaded build. Where the standard build places the GC-related data ahead of the `PyObject` structure, here that GC data lives inside the ordinary object header. To illustrate, on the AMD64 platform `None` occupies 32 bytes under free threading against 16 bytes in the standard build. Objects tracked by the GC, like dicts and lists, come out identical in size across both builds, because the free-threaded build adds no extra room for the GC data in their case.

[Subject index](INDEX.md) · [Previous source context](all-interned-strings-are-immortal.md) · [Following source context](qsbr-can-delay-freeing-of-memory.md)
