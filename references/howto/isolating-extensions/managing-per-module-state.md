# Managing Per-Module State

### Managing Per-Module State

For per-module state, adopt [multi-phase extension module initialization](https://docs.python.org/3.14/c-api/extension-modules.html#multi-phase-initialization). Doing so declares that your module handles multiple interpreters properly.

Give `PyModuleDef.m_size` a positive value to ask for that count of bytes of storage local to the module. Typically you set this to the size of a module-specific `struct`, which can hold the whole of the module's C-level state. That, in particular, is where to place pointers to classes (exceptions included, but static types excluded) plus settings (for instance `csv`?s [`field_size_limit`](https://docs.python.org/3.14/library/csv.html#csv.field_size_limit)) that the C code relies on to operate.

Note

A further option is keeping state in the module's `__dict__`, but then you must guard against crashing when users alter `__dict__` from Python code. Typically that means error- and type-checking down in the C layer, which is simple to botch and tough to test thoroughly.

That said, when the C code doesn't require module state, keeping it solely in `__dict__` is a sound choice.

Should the module state carry `PyObject` pointers, the module object has to keep references to those objects and provide the module-level hooks `m_traverse`, `m_clear` and `m_free`. They operate much like the `tp_traverse`, `tp_clear` and `tp_free` of a class. Supplying them takes some effort and lengthens the code; that is the cost of modules that unload cleanly.

A sample module carrying per-module state is presently offered as [xxlimited](https://github.com/python/cpython/blob/master/Modules/xxlimited.c); the example module initialization appears near the end of the file.

[Subject index](INDEX.md) · [Previous source context](managing-global-state.md) · [Following source context](opt-out-limiting-to-one-module-object-per-process.md)
