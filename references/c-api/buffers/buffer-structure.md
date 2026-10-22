# buffers C API: Buffer memory representation and lifetime overview

### Buffer structure

Buffer structures (or just "buffers") serve as a means of presenting one object's binary data to the Python programmer. They double as a zero-copy slicing mechanism as well. Because they can reference a region of memory, almost any data can be surfaced to the Python programmer with little effort. That memory might be a big, constant array residing in a C extension, it might be a raw memory region to be manipulated before handing it to an operating system library, or it might serve to carry structured data around in its native, in-memory layout.

Unlike the majority of data types that the Python interpreter surfaces, buffers are not [`PyObject`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) pointers; instead they are plain C structures. As a result, creating and copying them is trivial. Should a general-purpose wrapper around a buffer be required, a [memoryview](https://docs.python.org/3.14/c-api/memoryview.html#memoryview-objects) object can be built.

For brief guidance on authoring an exporting object, consult [Buffer Object Structures](https://docs.python.org/3.14/c-api/typeobj.html#buffer-structs). To obtain a buffer, consult `PyObject_GetBuffer()`.

[Subject index](INDEX.md) · [Previous source contract](buffer-protocol.md) · [Following source contract](py-buffer-to-pybuf-max-ndim.md)
