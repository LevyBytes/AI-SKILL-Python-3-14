# Debugging C API extensions and CPython Internals with GDB

# Gdb Helpers

### Debugging C API extensions and CPython Internals with GDB

Here you will find how the Python GDB extension, `python-gdb.py`, pairs with the GDB debugger to debug CPython extensions along with the CPython interpreter itself.

For pinning down low-level trouble like crashes or deadlocks, a low-level debugger such as GDB helps you diagnose and fix the problem. Out of the box, GDB (and its various front-ends) carries no high-level knowledge tied to the CPython interpreter.

By loading the `python-gdb.py` extension, GDB gains CPython interpreter awareness. It assists in inspecting the stack of Python functions running at the moment. Hand it a Python object that a [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)* pointer stands for, and the extension reveals that object's type and value.

Anyone building CPython extensions or experimenting with the C-written portions of CPython can turn to this document to pick up how the `python-gdb.py` extension works alongside GDB.

Note

A grounding in the fundamentals of GDB and the CPython C API is taken for granted here. The guidance gathered draws on the [devguide](https://devguide.python.org) together with the [Python wiki](https://wiki.python.org/moin/DebuggingWithGdb).

[Subject index](INDEX.md) · [Following source context](prerequisites.md)
