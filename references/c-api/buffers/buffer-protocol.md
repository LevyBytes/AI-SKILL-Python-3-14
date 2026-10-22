# Buffer Protocol

# Buffer

### Buffer Protocol

A number of objects in Python act as wrappers around an underlying memory array, or *buffer*. Among these are the built-in [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) and [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) types, along with certain extension types such as [`array.array`](https://docs.python.org/3.14/library/array.html#array.array). For specialized purposes — image processing or numeric analysis, for instance — third-party libraries may introduce types of their own.

These types each carry distinct semantics, yet they have one trait in common: each sits on top of a memory buffer that can be quite large. In certain scenarios, then, reaching that buffer directly — with no copying in between — becomes valuable.

At both the C and Python levels, Python supplies exactly this capability through the buffer protocol. The protocol has two sides:

- from the producer's perspective, a type may export a "buffer interface" that lets instances of that type publish details about the buffer beneath them. That interface is covered in the section [Buffer Object Structures](https://docs.python.org/3.14/c-api/typeobj.html#buffer-structs); on the Python side, refer to [Emulating buffer types](https://docs.python.org/3.14/reference/datamodel.html#python-buffer-protocol).

- from the consumer's perspective, there are several routes to securing a pointer to an object's raw underlying data (a method parameter, say). On the Python side, see [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview).

Basic objects like [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) and [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) present the buffer underneath them as a stream of bytes. Other presentations exist too; the items surfaced by an [`array.array`](https://docs.python.org/3.14/library/array.html#array.array), for example, may span several bytes each.

One example of a buffer-interface consumer is the [`write()`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase.write) method belonging to file objects: anything able to export a stream of bytes via the buffer interface can be written out to a file. Whereas `write()` requires only read-only access to the inner contents of the object handed to it, certain other methods — [`readinto()`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase.readinto) among them — demand write access to their argument's contents. With the buffer interface, objects can choose to permit or deny the export of read-write versus read-only buffers.

A consumer of the buffer interface has two routes to acquiring a buffer over a target object:

- invoke `PyObject_GetBuffer()` supplying the appropriate parameters;

- invoke [`PyArg_ParseTuple()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTuple) (or one of the related functions) using a `y*`, `w*`, or `s*` [format code](https://docs.python.org/3.14/c-api/arg.html#arg-parsing).

Either way, once the buffer is no longer wanted, `PyBuffer_Release()` has to be invoked. Neglecting this may produce assorted problems, resource leaks among them.

Added in version 3.12: Python code can now reach the buffer protocol; refer to [Emulating buffer types](https://docs.python.org/3.14/reference/datamodel.html#python-buffer-protocol) plus [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview).

[Subject index](INDEX.md) · [Following source contract](buffer-structure.md)
