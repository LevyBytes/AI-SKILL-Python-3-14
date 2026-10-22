# tracemalloc: Trace address spaces and allocation records

domain

Address space of a memory block (`int`). Read-only property.

tracemalloc reserves domain `0` for the memory allocations Python makes. Other domains are available to C extensions for tracing different resources.

 size

Size of the memory block in bytes (`int`).

 traceback

The traceback for where the memory block was allocated, a `Traceback` instance.

[Subject index](INDEX.md) · [Previous](tracemalloc-trace-class.md) · [Continue](tracemalloc-traceback-class.md) · [Owning module, declaration or section: tracemalloc](tracemalloc-trace-memory-allocations.md) · [Owning module, declaration or section: tracemalloc.Trace](tracemalloc-trace-class.md) · [Owning module, declaration or section: Trace](tracemalloc-trace-class.md)
