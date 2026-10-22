# argument parsing C API: Encoded strings and buffer conversion formats

`w*` (read-write [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object)) [Py_buffer]

Any object that supports the read-write buffer interface works with this format. It populates a [`Py_buffer`](https://docs.python.org/3.14/c-api/buffer.html#c.Py_buffer) structure that the caller supplies. Embedded null bytes are allowed in the buffer. Once finished with the buffer, the caller has to call [`PyBuffer_Release()`](https://docs.python.org/3.14/c-api/buffer.html#c.PyBuffer_Release).

`es` ([`str`](https://docs.python.org/3.14/library/stdtypes.html#str)) [const char *encoding, char **buffer]

A take on `s` used to encode Unicode into a character buffer. It functions only for encoded data that has no embedded NUL bytes.

Two arguments are needed by this format. The first serves purely as input, and has to be a const char* aimed at the name of an encoding given as a NUL-terminated string, or else `NULL`, in which case the `'utf-8'` encoding applies. Should Python not recognize the named encoding, an exception is raised. The second argument has to be a char**; the pointer it points at will be set to a buffer holding the argument text. That text gets encoded using the encoding named by the first argument.

`PyArg_ParseTuple()` reserves a buffer of the required size, copies the encoded data into it, and points **buffer* at the freshly reserved storage. Freeing that reserved buffer after use, by calling [`PyMem_Free()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_Free), is the caller’s job.

`et` ([`str`](https://docs.python.org/3.14/library/stdtypes.html#str), [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) or [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray)) [const char *encoding, char **buffer]

Identical to `es`, save that byte string objects pass straight through with no recoding. The implementation instead presumes the byte string object already uses the encoding handed in as the parameter.

`es#` ([`str`](https://docs.python.org/3.14/library/stdtypes.html#str)) [const char *encoding, char **buffer, [`Py_ssize_t`](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) *buffer_length]

A take on `s#` used to encode Unicode into a character buffer. In contrast to the `es` format, this take permits input data containing NUL characters.

Three arguments are needed. The first serves purely as input, and has to be a const char* aimed at the name of an encoding given as a NUL-terminated string, or else `NULL`, in which case the `'utf-8'` encoding applies. Should Python not recognize the named encoding, an exception is raised. The second argument has to be a char**; the pointer it points at will be set to a buffer holding the argument text. That text gets encoded using the encoding named by the first argument. As for the third argument, it has to point at an integer; that referenced integer ends up holding the count of bytes in the output buffer.

There are two modes of operation:

When **buffer* points at a `NULL` pointer, the function reserves a buffer of the required size, copies the encoded data into it, and sets **buffer* to point at the freshly reserved storage. Freeing that reserved buffer after usage, by calling [`PyMem_Free()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_Free), is the caller’s job.

When **buffer* points at a non-`NULL` pointer (a buffer already reserved), `PyArg_ParseTuple()` treats that location as the buffer and reads the starting value of **buffer_length* as the buffer size. It then copies the encoded data into the buffer and NUL-terminates it. Should the buffer prove too small, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) will be set.

Either way, **buffer_length* ends up holding the length of the encoded data, not counting the trailing NUL byte.

`et#` ([`str`](https://docs.python.org/3.14/library/stdtypes.html#str), [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) or [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray)) [const char *encoding, char **buffer, [`Py_ssize_t`](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) *buffer_length]

Identical to `es#`, save that byte string objects pass straight through with no recoding. The implementation instead presumes the byte string object already uses the encoding handed in as the parameter.

Changed in version 3.12: the `u`, `u#`, `Z`, and `Z#` formats were dropped, since their implementation depended on a legacy `Py_UNICODE*` representation.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](string-buffer-memory-ownership.md) · [Following source contract](numbers.md)
