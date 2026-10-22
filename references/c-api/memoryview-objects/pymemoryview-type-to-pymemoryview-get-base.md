# MemoryView objects

# Memoryview, Method

## Overview

Covers: MemoryView objects; Instance Method Objects.

## MemoryView objects

### MemoryView objects

A [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) object surfaces the C-level [buffer interface](https://docs.python.org/3.14/c-api/buffer.html#bufferobjects) in the shape of a Python object, after which you can hand it around just as you would any other object.

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyMemoryView_Type

* Belongs to the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Standing in for the Python memoryview type, this [`PyTypeObject`](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) instance is the very same object that the Python side knows as [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview).

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyMemoryView_FromObject([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj)

*Return value: New reference.** Belongs to the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Build a memoryview object out of some object that offers the buffer interface. Where *obj* permits writable buffer exports, the resulting memoryview is read/write; failing that, the exporter decides whether it comes out read-only or read/write.

 PyBUF_READ

* Belongs to the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) as of version 3.11.*

The flag you pass when you want a readonly buffer.

 PyBUF_WRITE

* Belongs to the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) as of version 3.11.*

The flag you pass when you want a writable buffer.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyMemoryView_FromMemory(char *mem, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) size, int flags)

*Return value: New reference.** Belongs to the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) as of version 3.7.*

Build a memoryview object that takes *mem* for its underlying buffer. The *flags* argument is either `PyBUF_READ` or `PyBUF_WRITE`.

Added in version 3.3.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyMemoryView_FromBuffer(const [Py_buffer](https://docs.python.org/3.14/c-api/buffer.html#c.Py_buffer) *view)

*Return value: New reference.** Belongs to the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) as of version 3.11.*

Build a memoryview object that wraps the supplied buffer structure *view*. When you are dealing with plain byte buffers, `PyMemoryView_FromMemory()` is the better choice.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyMemoryView_GetContiguous([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj, int buffertype, char order)

*Return value: New reference.** Belongs to the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Build a memoryview object onto a [contiguous](https://docs.python.org/3.14/glossary.html#term-contiguous) span of memory — laid out in either ‘C’ or ‘F’ortran *order* — drawn from an object that supplies the buffer interface. Should that memory already be contiguous, the memoryview refers straight to the original storage; if not, a copy is taken and the memoryview refers to a fresh bytes object.

The *buffertype* argument is either `PyBUF_READ` or `PyBUF_WRITE`.

 int PyMemoryView_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj)

Yield true when the object *obj* happens to be a memoryview object. Subclassing [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) is not something the language permits at present. This call can never fail.

 [Py_buffer](https://docs.python.org/3.14/c-api/buffer.html#c.Py_buffer) *PyMemoryView_GET_BUFFER([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *mview)

Hand back a pointer to the private copy the memoryview keeps of the exporter’s buffer. Here *mview* **must** be a memoryview instance; since the macro performs no type check, that verification falls to you, and skipping it courts crashes.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyMemoryView_GET_BASE([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *mview)

Give back a pointer to the exporting object underpinning the memoryview, or `NULL` whenever the memoryview was produced by either `PyMemoryView_FromMemory()` or `PyMemoryView_FromBuffer()`. Here *mview* **must** be a memoryview instance.

[Subject index](INDEX.md) · [Following source contract](../instance-method-objects/pyinstancemethod-type-to-pyinstancemethod-get-function.md)
