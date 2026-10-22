# Abstract Objects Layer

## Abstract Objects Layer

### Abstract Objects Layer

The routines described here operate on Python objects without caring about the specific type, or they span broad families of types (for instance, every numeric type, or every sequence type). Apply one to an object type it was not designed for, and a Python exception is raised.

These calls must not be applied to objects left in an unfinished state — for example, a list produced through [`PyList_New()`](https://docs.python.org/3.14/c-api/list.html#c.PyList_New) whose elements have yet to receive any non-`NULL` value.

- [Object Protocol](https://docs.python.org/3.14/c-api/object.html)
- [Call Protocol](https://docs.python.org/3.14/c-api/call.html)
  - [The *tp_call* Protocol](https://docs.python.org/3.14/c-api/call.html#the-tp-call-protocol)
  - [The Vectorcall Protocol](https://docs.python.org/3.14/c-api/call.html#the-vectorcall-protocol)
    - [Recursion Control](https://docs.python.org/3.14/c-api/call.html#recursion-control)
    - [Vectorcall Support API](https://docs.python.org/3.14/c-api/call.html#vectorcall-support-api)

  - [Object Calling API](https://docs.python.org/3.14/c-api/call.html#object-calling-api)
  - [Call Support API](https://docs.python.org/3.14/c-api/call.html#call-support-api)

- [Number Protocol](https://docs.python.org/3.14/c-api/number.html)
- [Sequence Protocol](https://docs.python.org/3.14/c-api/sequence.html)
- [Mapping Protocol](https://docs.python.org/3.14/c-api/mapping.html)
- [Iterator Protocol](https://docs.python.org/3.14/c-api/iter.html)
- [Buffer Protocol](https://docs.python.org/3.14/c-api/buffer.html)
  - [Buffer structure](https://docs.python.org/3.14/c-api/buffer.html#buffer-structure)
  - [Buffer request types](https://docs.python.org/3.14/c-api/buffer.html#buffer-request-types)
    - [request-independent fields](https://docs.python.org/3.14/c-api/buffer.html#request-independent-fields)
    - [readonly, format](https://docs.python.org/3.14/c-api/buffer.html#readonly-format)
    - [shape, strides, suboffsets](https://docs.python.org/3.14/c-api/buffer.html#shape-strides-suboffsets)
    - [contiguity requests](https://docs.python.org/3.14/c-api/buffer.html#contiguity-requests)
    - [compound requests](https://docs.python.org/3.14/c-api/buffer.html#compound-requests)

  - [Complex arrays](https://docs.python.org/3.14/c-api/buffer.html#complex-arrays)
    - [NumPy-style: shape and strides](https://docs.python.org/3.14/c-api/buffer.html#numpy-style-shape-and-strides)
    - [PIL-style: shape, strides and suboffsets](https://docs.python.org/3.14/c-api/buffer.html#pil-style-shape-strides-and-suboffsets)

  - [Buffer-related functions](https://docs.python.org/3.14/c-api/buffer.html#buffer-related-functions)

[Subject index](INDEX.md) · [Previous source contract](../orientation/overview.md) · [Following source contract](../allocating-objects-on-the-heap/pyobject-new-to-pytype-genericalloc.md)
