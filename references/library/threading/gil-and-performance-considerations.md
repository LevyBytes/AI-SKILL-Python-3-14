# threading — GIL and performance considerations

### GIL and performance considerations

The [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) module sidesteps the [global interpreter lock](https://docs.python.org/3.14/glossary.html#term-global-interpreter-lock) (GIL) by spawning distinct processes; the threading module, by contrast, stays inside one process, so every thread shares a common memory space. Because only one thread runs Python bytecode at any instant, though, the GIL caps how much faster threading makes CPU-bound work. Even so, threads stay valuable for reaching concurrency across plenty of situations.

Starting with Python 3.13, [free-threaded](https://docs.python.org/3.14/glossary.html#term-free-threading) builds are able to turn the GIL off, which permits threads to truly run in parallel, though this capability is not enabled out of the box (refer to [**PEP 703**](https://peps.python.org/pep-0703/)).

[Subject index](INDEX.md) · [Previous](introduction.md) · [Continue](threading-active-count-to-threading-enumerate.md) · [Owning module, declaration or section: threading](threading-thread-based-parallelism.md)
