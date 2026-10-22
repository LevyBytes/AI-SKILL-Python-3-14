# Buffer request types

### Buffer request types

A buffer is generally obtained by issuing a buffer request to an exporting object through `PyObject_GetBuffer()`. Because the logical structure of the memory may range widely in complexity, the consumer relies on the *flags* argument to declare the precise buffer type it is equipped to deal with.

Every `Py_buffer` field is defined without ambiguity by the request type.

[Subject index](INDEX.md) · [Previous source contract](py-buffer-to-pybuf-max-ndim.md) · [Following source contract](request-independent-fields.md)
