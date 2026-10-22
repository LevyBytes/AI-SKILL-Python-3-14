# Static Types

### Static Types

Conventionally, the types written in C are *static*, meaning a static [`PyTypeObject`](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) structure is declared straight in the code and prepared with [`PyType_Ready()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Ready).

These types end up constrained when compared against types written in Python:

- A single base is the maximum for static types, that is, multiple inheritance is unavailable to them.

- Static type objects are immutable (although their instances need not be). Adding or altering the type object’s attributes from within Python cannot be done.

- Static type objects get shared between [sub-interpreters](https://docs.python.org/3.14/c-api/subinterpreters.html#sub-interpreter-support), and therefore must avoid holding any subinterpreter-specific state.

On top of that, because [`PyTypeObject`](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) appears within the [Limited API](https://docs.python.org/3.14/c-api/stable.html#limited-c-api) merely as an opaque struct, every extension module that employs static types has to be built against one particular Python minor version.

[Subject index](INDEX.md) · [Previous source contract](pyobject-callfinalizerfromdealloc-to-pytypeobject-tp-watched.md) · [Following source contract](heap-types.md)
