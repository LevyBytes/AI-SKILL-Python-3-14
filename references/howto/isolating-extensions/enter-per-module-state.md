# Enter Per-Module State

### Enter Per-Module State

Rather than centering on per-interpreter state, the Python C API has been growing to give stronger support to the finer-grained *per-module* state. The implication is that C-level data ought to live on a *module object*. Every interpreter builds its own module object, so the data stays apart. To exercise the isolation, you can even load several module objects belonging to one extension within a single interpreter.

Per-module state offers a simple mental model for lifetime and resource ownership: the extension module sets itself up when a module object comes into existence, and tears down when that object is released. Seen this way, a module behaves like any other [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*; you have no ?on interpreter shutdown? hooks to remember — or to overlook.

Bear in mind that several flavors of ?globals? have legitimate uses: per-process, per-interpreter, per-thread or per-task state. When per-module state is your default, those remain available, yet you ought to regard them as the exception: should you require one, give it extra care and testing. (This guide leaves them out of scope.)

[Subject index](INDEX.md) · [Previous source context](background.md) · [Following source context](isolated-module-objects.md)
