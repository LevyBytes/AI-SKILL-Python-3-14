# Object Implementation Support

## Object Implementation Support

### Object Implementation Support

The functions, types, and macros you draw on while defining new object types are laid out in this chapter.

- [Allocating objects on the heap](https://docs.python.org/3.14/c-api/allocation.html)
  - [Soft-deprecated aliases](https://docs.python.org/3.14/c-api/allocation.html#soft-deprecated-aliases)

- [Object Life Cycle](https://docs.python.org/3.14/c-api/lifecycle.html)
  - [Life Events](https://docs.python.org/3.14/c-api/lifecycle.html#life-events)
  - [Cyclic Isolate Destruction](https://docs.python.org/3.14/c-api/lifecycle.html#cyclic-isolate-destruction)
  - [Functions](https://docs.python.org/3.14/c-api/lifecycle.html#functions)

- [Common Object Structures](https://docs.python.org/3.14/c-api/structures.html)
  - [Base object types and macros](https://docs.python.org/3.14/c-api/structures.html#base-object-types-and-macros)
  - [Implementing functions and methods](https://docs.python.org/3.14/c-api/structures.html#implementing-functions-and-methods)
  - [Accessing attributes of extension types](https://docs.python.org/3.14/c-api/structures.html#accessing-attributes-of-extension-types)
    - [Member flags](https://docs.python.org/3.14/c-api/structures.html#member-flags)
    - [Member types](https://docs.python.org/3.14/c-api/structures.html#member-types)
    - [Defining Getters and Setters](https://docs.python.org/3.14/c-api/structures.html#defining-getters-and-setters)

- [Type Object Structures](https://docs.python.org/3.14/c-api/typeobj.html)
  - [Quick Reference](https://docs.python.org/3.14/c-api/typeobj.html#quick-reference)
    - [“tp slots”](https://docs.python.org/3.14/c-api/typeobj.html#tp-slots)
    - [sub-slots](https://docs.python.org/3.14/c-api/typeobj.html#sub-slots)
    - [slot typedefs](https://docs.python.org/3.14/c-api/typeobj.html#slot-typedefs)

  - [PyTypeObject Definition](https://docs.python.org/3.14/c-api/typeobj.html#pytypeobject-definition)
  - [PyObject Slots](https://docs.python.org/3.14/c-api/typeobj.html#pyobject-slots)
  - [PyVarObject Slots](https://docs.python.org/3.14/c-api/typeobj.html#pyvarobject-slots)
  - [PyTypeObject Slots](https://docs.python.org/3.14/c-api/typeobj.html#pytypeobject-slots)
  - [Static Types](https://docs.python.org/3.14/c-api/typeobj.html#static-types)
  - [Heap Types](https://docs.python.org/3.14/c-api/typeobj.html#heap-types)
  - [Number Object Structures](https://docs.python.org/3.14/c-api/typeobj.html#number-object-structures)
  - [Mapping Object Structures](https://docs.python.org/3.14/c-api/typeobj.html#mapping-object-structures)
  - [Sequence Object Structures](https://docs.python.org/3.14/c-api/typeobj.html#sequence-object-structures)
  - [Buffer Object Structures](https://docs.python.org/3.14/c-api/typeobj.html#buffer-object-structures)
  - [Async Object Structures](https://docs.python.org/3.14/c-api/typeobj.html#async-object-structures)
  - [Slot Type typedefs](https://docs.python.org/3.14/c-api/typeobj.html#slot-type-typedefs)
  - [Examples](https://docs.python.org/3.14/c-api/typeobj.html#examples)

- [Supporting Cyclic Garbage Collection](https://docs.python.org/3.14/c-api/gcsupport.html)
  - [Controlling the Garbage Collector State](https://docs.python.org/3.14/c-api/gcsupport.html#controlling-the-garbage-collector-state)
  - [Querying Garbage Collector State](https://docs.python.org/3.14/c-api/gcsupport.html#querying-garbage-collector-state)

[Subject index](INDEX.md) · [Previous source contract](../orientation/overview.md) · [Following source contract](../support-for-perf-maps/pyunstable-perfmapstate-init-to-pyunstable-perfmapstate-fini.md)
