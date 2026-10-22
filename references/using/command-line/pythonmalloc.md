# PYTHONMALLOC

PYTHONMALLOC

Choose the Python memory allocators and/or set up debug hooks.

Choose the family of memory allocators Python uses:

- `default`: use the [default memory allocators](https://docs.python.org/3.14/c-api/memory.html#default-memory-allocators).

- `malloc`: use the `malloc()` function of the C library for all domains ([`PYMEM_DOMAIN_RAW`](https://docs.python.org/3.14/c-api/memory.html#c.PYMEM_DOMAIN_RAW), [`PYMEM_DOMAIN_MEM`](https://docs.python.org/3.14/c-api/memory.html#c.PYMEM_DOMAIN_MEM), [`PYMEM_DOMAIN_OBJ`](https://docs.python.org/3.14/c-api/memory.html#c.PYMEM_DOMAIN_OBJ)).

- `pymalloc`: use the [pymalloc allocator](https://docs.python.org/3.14/c-api/memory.html#pymalloc) for [`PYMEM_DOMAIN_MEM`](https://docs.python.org/3.14/c-api/memory.html#c.PYMEM_DOMAIN_MEM) and [`PYMEM_DOMAIN_OBJ`](https://docs.python.org/3.14/c-api/memory.html#c.PYMEM_DOMAIN_OBJ) domains and use the `malloc()` function for the [`PYMEM_DOMAIN_RAW`](https://docs.python.org/3.14/c-api/memory.html#c.PYMEM_DOMAIN_RAW) domain.

- `mimalloc`: use the [mimalloc allocator](https://docs.python.org/3.14/c-api/memory.html#mimalloc) for [`PYMEM_DOMAIN_MEM`](https://docs.python.org/3.14/c-api/memory.html#c.PYMEM_DOMAIN_MEM) and [`PYMEM_DOMAIN_OBJ`](https://docs.python.org/3.14/c-api/memory.html#c.PYMEM_DOMAIN_OBJ) domains and use the `malloc()` function for the [`PYMEM_DOMAIN_RAW`](https://docs.python.org/3.14/c-api/memory.html#c.PYMEM_DOMAIN_RAW) domain.

Install [debug hooks](https://docs.python.org/3.14/c-api/memory.html#pymem-debug-hooks):

- `debug`: install debug hooks on top of the [default memory allocators](https://docs.python.org/3.14/c-api/memory.html#default-memory-allocators).

- `malloc_debug`: same as `malloc` but also install debug hooks.

- `pymalloc_debug`: same as `pymalloc` but also install debug hooks.

- `mimalloc_debug`: same as `mimalloc` but also install debug hooks.

Note

Within the [free-threaded](https://docs.python.org/3.14/glossary.html#term-free-threading) build, support is absent for the `malloc`, `malloc_debug`, `pymalloc`, and `pymalloc_debug` values. The only ones taken are `default`, `debug`, `mimalloc`, and `mimalloc_debug`.

Added in version 3.6.

Changed in version 3.7: Added the `"default"` allocator.

[Subject index](INDEX.md) · [Previous source section](pythonasynciodebug.md) · [Following source section](pythonmallocstats.md)
