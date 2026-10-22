# Garbage-Collection Protocol

### Garbage-Collection Protocol

Each instance of a heap type keeps a reference to its type. That guarantees the type outlives all its instances, but it can produce reference cycles that the garbage collector must break.

So as to head off memory leaks, instances of heap types must follow the garbage collection protocol. Concretely, heap types ought to:

- Carry the [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC) flag.

- Supply a traverse function through [`Py_tp_traverse`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_tp_traverse) that visits the type (for example with `Py_VISIT(Py_TYPE(self))`).

Consult the documentation for [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC) and [`tp_traverse`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_traverse) for further considerations.

The API used to define heap types developed piecemeal, which leaves it a bit clumsy to use as things stand. The sections that follow walk you through frequent pitfalls.

[Subject index](INDEX.md) · [Previous source context](defining-heap-types.md) · [Following source context](tp-traverse-in-python-3-8-and-lower.md)
