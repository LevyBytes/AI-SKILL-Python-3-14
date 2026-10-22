# argument parsing C API: String and binary-buffer argument parsing formats

### Strings and buffers

Note

For Python 3.12 and earlier, you must define the macro `PY_SSIZE_T_CLEAN` ahead of including `Python.h` if you want to use any of the `#` format variants (`s#`, `y#`, and so on) described below. Starting with Python 3.13, this requirement no longer applies.

With these formats you can reach an object as one contiguous block of memory. There is no need for you to supply raw storage for the unicode or bytes region returned.

Buffers carry no trailing NUL unless the text says otherwise.

Strings and buffers may reach C through three distinct routes:

- Formats like `y*` and `s*` populate a [`Py_buffer`](https://docs.python.org/3.14/c-api/buffer.html#c.Py_buffer) structure. Doing so locks the backing buffer, which lets the caller go on using the buffer even within a [`Py_BEGIN_ALLOW_THREADS`](https://docs.python.org/3.14/c-api/threads.html#c.Py_BEGIN_ALLOW_THREADS) block, free of the danger that mutable data gets resized or torn down. Consequently, **you have to call** [`PyBuffer_Release()`](https://docs.python.org/3.14/c-api/buffer.html#c.PyBuffer_Release) once the data has been handled (or whenever you bail out early).

- The `es`, `es#`, `et` and `et#` formats reserve the output buffer. **You have to call** [`PyMem_Free()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_Free) once the data has been handled (or whenever you bail out early).

- The remaining formats accept either a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) or a read-only [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object), such as [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes), and hand back a `const char *` pointer aimed at its buffer. Here the buffer is “borrowed”: the matching Python object owns it, and it lives exactly as long as that object does. No memory cleanup falls on you.

For the backing buffer to be borrowed safely, the object’s [`PyBufferProcs.bf_releasebuffer`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyBufferProcs.bf_releasebuffer) field has to be `NULL`. That rules out frequently used mutable objects like [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray), and even certain read-only ones such as a [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) over [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes).

Apart from that `bf_releasebuffer` condition, nothing checks whether the supplied object is immutable (for instance, whether it would grant a request for a writable buffer, or whether some other thread could alter the data).

`s` ([`str`](https://docs.python.org/3.14/library/stdtypes.html#str)) [const char *]

Turn a Unicode object into a C pointer to a character string. The character pointer variable whose address you supply receives a pointer to an existing string. That C string ends in NUL. No embedded null code points may appear in the Python string; should any appear, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) exception is raised. The `'utf-8'` encoding handles converting Unicode objects into C strings. Should that conversion not succeed, a [`UnicodeError`](https://docs.python.org/3.14/library/exceptions.html#UnicodeError) is raised.

Note

[bytes-like objects](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) are not accepted by this format. When you want to take filesystem paths and turn them into C character strings, the better choice is the `O&` format paired with [`PyUnicode_FSConverter()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_FSConverter) as the *converter*.

Changed in version 3.5: Earlier, a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) was raised whenever embedded null code points turned up inside the Python string.

`s*` ([`str`](https://docs.python.org/3.14/library/stdtypes.html#str) or [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object)) [Py_buffer]

Both Unicode objects and bytes-like objects are valid for this format. It populates a [`Py_buffer`](https://docs.python.org/3.14/c-api/buffer.html#c.Py_buffer) structure that the caller supplies. Here the resulting C string is allowed to hold embedded NUL bytes. The `'utf-8'` encoding handles converting Unicode objects into C strings.

`s#` ([`str`](https://docs.python.org/3.14/library/stdtypes.html#str), read-only [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object)) [const char *, [`Py_ssize_t`](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t)]

Behaves like `s*`, but hands back a borrowed buffer. Two C variables receive the result: the first is a pointer to a C string, the second is that string’s length. Embedded null bytes are permitted in the string. The `'utf-8'` encoding handles converting Unicode objects into C strings.

`z` ([`str`](https://docs.python.org/3.14/library/stdtypes.html#str) or `None`) [const char *]

Behaves like `s`, except the Python object is allowed to be `None` too, and in that event the C pointer is set to `NULL`.

`z*` ([`str`](https://docs.python.org/3.14/library/stdtypes.html#str), [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) or `None`) [Py_buffer]

Behaves like `s*`, except the Python object is allowed to be `None` too, and in that event the `buf` member of the [`Py_buffer`](https://docs.python.org/3.14/c-api/buffer.html#c.Py_buffer) structure is set to `NULL`.

`z#` ([`str`](https://docs.python.org/3.14/library/stdtypes.html#str), read-only [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) or `None`) [const char *, [`Py_ssize_t`](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t)]

Behaves like `s#`, except the Python object is allowed to be `None` too, and in that event the C pointer is set to `NULL`.

`y` (read-only [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object)) [const char *]

Here a bytes-like object is turned into a C pointer aimed at a borrowed character string; Unicode objects are rejected. No embedded null bytes may sit inside the bytes buffer; if any do, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) exception is raised.

Changed in version 3.5: Earlier, a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) was raised whenever embedded null bytes turned up inside the bytes buffer.

`y*` ([bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object)) [Py_buffer]

A variant of `s*` that turns away Unicode objects and permits bytes-like objects alone. **This is the recommended way to accept binary data.**

`y#` (read-only [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object)) [const char *, [`Py_ssize_t`](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t)]

A take on `s#` that rejects Unicode objects, allowing only bytes-like objects.

`S` ([`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes)) [PyBytesObject *]

Demands that the Python object be a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object, with no conversion attempted. A [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is raised when the object is not a bytes object. You may also declare the C variable as [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*.

`Y` ([`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray)) [PyByteArrayObject *]

Demands that the Python object be a [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) object, with no conversion attempted. A [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is raised when the object is not a `bytearray` object. You may also declare the C variable as [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*.

`U` ([`str`](https://docs.python.org/3.14/library/stdtypes.html#str)) [PyObject *]

Demands that the Python object be a Unicode object, with no conversion attempted. A [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is raised when the object is not a Unicode object. You may also declare the C variable as [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*.

[Subject index](INDEX.md) · [Previous source contract](parsing-arguments.md) · [Following source contract](strings-and-buffers-w-read-write-bytes-like-object-py-buffer.md)
