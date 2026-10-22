# Memory Allocation APIs

### Memory Allocation APIs

The memory-management portion of Python's C API splits its functions across three separate [allocation domains](https://docs.python.org/3.14/c-api/memory.html#id1): “raw”, “mem”, and “object”. To keep things thread-safe, the free-threaded build insists that the object domain be reserved exclusively for Python objects and that every Python object pass through it. Earlier Python releases treated this merely as a recommendation rather than something strictly enforced.

Note

Hunt through your extension for every [`PyObject_Malloc()`](https://docs.python.org/3.14/c-api/memory.html#c.PyObject_Malloc) call and confirm that the resulting memory genuinely holds Python objects. When you simply need a buffer, switch over to [`PyMem_Malloc()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_Malloc) rather than `PyObject_Malloc()`.

[Subject index](INDEX.md) · [Previous source context](borrowed-references.md) · [Following source context](thread-state-and-gil-apis.md)
