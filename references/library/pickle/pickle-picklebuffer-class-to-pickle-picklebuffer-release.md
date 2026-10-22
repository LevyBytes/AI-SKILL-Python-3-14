# pickle / Module Interface: `pickle.PickleBuffer`, `raw()`, `release()`

*class *pickle.PickleBuffer(*buffer*)

A wrapper around a buffer that holds picklable data. *buffer* has to be a [buffer-providing](https://docs.python.org/3.14/c-api/buffer.html#bufferobjects) object, such as a [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) or an N-dimensional array.

`PickleBuffer` is itself a buffer provider, so you can pass it to other APIs that expect a buffer-providing object, such as [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview).

Serializing `PickleBuffer` objects works only under pickle protocol 5 or above. Out-of-band serialization is something they qualify for.

Added in version 3.8.

 raw()

Return a [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) of the memory region behind this buffer. The object returned is a one-dimensional, C-contiguous memoryview whose format is `B` (unsigned bytes). [`BufferError`](https://docs.python.org/3.14/library/exceptions.html#BufferError) is raised when the buffer is neither C- nor Fortran-contiguous.

 release()

Release the underlying buffer exposed by the PickleBuffer object.

[Subject index](INDEX.md) · [Previous](pickle-unpickler-class-to-pickle-unpickler-find-class.md) · [Continue](what-can-be-pickled-and-unpickled.md) · [Owning module, declaration or section: pickle](pickle-python-object-serialization.md) · [Owning module, declaration or section: Module Interface](pickle-highest-protocol-to-pickle-unpicklingerror.md)
