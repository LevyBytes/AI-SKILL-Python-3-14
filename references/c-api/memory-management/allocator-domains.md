# Allocator Domains

### Allocator Domains

Every allocating function falls under one of three distinct "domains" (see also `PyMemAllocatorDomain`). These domains stand for separate allocation strategies, each tuned to a different aim. Exactly how a given domain obtains memory, or which internal functions it invokes, counts as an implementation detail, though for debugging a streamlined table appears at Default Memory Allocators. To allocate and free a block of memory, the APIs you use have to come from one and the same domain. As an example, memory obtained with `PyMem_Malloc()` has to be released through `PyMem_Free()`.

The three allocation domains are:

- Raw domain: meant for allocating memory toward general-purpose memory buffers in cases where the allocation *must* reach the system allocator, or where the allocator has to function without an [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state). Memory comes straight from the system. See Raw Memory Interface.

- "Mem" domain: meant for allocating memory toward Python buffers and general-purpose memory buffers in cases where an [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) has to be present for the allocation. Memory comes out of the Python private heap. See Memory Interface.

- Object domain: meant for allocating memory toward Python objects. Memory comes out of the Python private heap. See Object allocators.

Note

For the [free-threaded](https://docs.python.org/3.14/glossary.html#term-free-threading) build, the rule is that the "object" domain serves only Python objects, and that every Python object is allocated through that domain. That is a change from earlier Python versions, in which the same convention was merely recommended rather than strictly enforced.

So, for instance, buffers (objects that are not Python objects) belong with `PyMem_Malloc()`, `PyMem_RawMalloc()`, or `malloc()`, and never with `PyObject_Malloc()`.

See [Memory Allocation APIs](https://docs.python.org/3.14/howto/free-threading-extensions.html#free-threaded-memory-allocation).

[Subject index](INDEX.md) · [Previous source contract](overview.md) · [Following source contract](pymem-rawmalloc-to-pymem-rawfree.md)
