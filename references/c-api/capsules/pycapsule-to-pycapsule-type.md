# capsules C API: `PyCapsule`, `PyCapsule_Type`

type PyCapsule

A subtype of [`PyObject`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject), this stands for an opaque value and comes in handy for C extension modules that must carry such a value (in the form of a `void*` pointer) across Python code to reach other C code. A common use is exposing a C function pointer declared in one module to other modules, letting the ordinary import machinery reach C APIs that live in dynamically loaded modules.

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyCapsule_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

The type object that goes with capsule objects. At the Python level it is one and the same as [`types.CapsuleType`](https://docs.python.org/3.14/library/types.html#types.CapsuleType).

[Subject index](INDEX.md) · [Owning C API section and shared conditions](capsules.md) · [Following source contract](pycapsule-destructor-to-pycapsule-import.md)
