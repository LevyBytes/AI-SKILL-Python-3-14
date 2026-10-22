# Changing Static Types to Heap Types

### Changing Static Types to Heap Types

You can turn static types into heap types, but keep in mind that the heap type API was never meant for a ?lossless? conversion away from static types — that is, producing a type that behaves precisely like a given static type. Consequently, while restating the class definition through a fresh API, you will probably alter a handful of details by accident (such as pickleability or inherited slots). Always verify the details that matter to you.

Keep an eye out for the next two points especially (though understand that this list is not exhaustive):

- In contrast with static types, heap type objects default to being mutable. Apply the [`Py_TPFLAGS_IMMUTABLETYPE`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_IMMUTABLETYPE) flag to block mutability.

- Heap types take on [`tp_new`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_new) by default, so instantiating them from Python code may become feasible. The [`Py_TPFLAGS_DISALLOW_INSTANTIATION`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_DISALLOW_INSTANTIATION) flag lets you stop this.

[Subject index](INDEX.md) · [Previous source context](heap-types.md) · [Following source context](defining-heap-types.md)
