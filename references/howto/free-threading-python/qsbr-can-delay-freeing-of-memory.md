# QSBR can delay freeing of memory

#### QSBR can delay freeing of memory

To build lock-free data structures safely, a safe memory reclamation (SMR) approach called quiescent state-based reclamation (QSBR) comes into play. Concretely, the memory underlying structures that permit lock-free access goes through QSBR, which holds off on the free operation instead of releasing the memory at once. The list object and the dictionary keys object are two such structures. For specifics on how QSBR works under the hood, look at `InternalDocs/qsbr.md` within the CPython source tree. Calling [`gc.collect()`](https://docs.python.org/3.14/library/gc.html#gc.collect) ought to release every byte that QSBR is still holding. Keep in mind that even after QSBR hands the memory back, the allocator beneath it may hold onto it rather than returning it to the OS straight away, so the process's resident set size (RSS) may not shrink.

[Subject index](INDEX.md) · [Previous source context](non-gc-objects-have-a-larger-object-header.md) · [Following source context](mimalloc-allocator-vs-pymalloc.md)
