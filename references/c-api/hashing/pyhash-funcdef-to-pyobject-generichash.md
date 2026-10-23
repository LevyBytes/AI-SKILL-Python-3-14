# hashing C API: Hash function definition, pointer and buffer hashing

type PyHash_FuncDef

The hash-function definition that `PyHash_GetFuncDef()` draws on.

 Py_hash_t (*const hash)(const void*, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t))

Hash function.

 const char *name

The name of the hash function, given as a UTF-8 encoded string.

It maps onto the [`sys.hash_info.algorithm`](https://docs.python.org/3.14/library/sys.html#sys.hash_info.algorithm) constant.

 const int hash_bits

How wide, in bits, the hash value is internally.

It maps onto the [`sys.hash_info.hash_bits`](https://docs.python.org/3.14/library/sys.html#sys.hash_info.hash_bits) constant.

 const int seed_bits

How many bits the seed input spans.

It maps onto the [`sys.hash_info.seed_bits`](https://docs.python.org/3.14/library/sys.html#sys.hash_info.seed_bits) constant.

Added in version 3.4.

 PyHash_FuncDef *PyHash_GetFuncDef(void)

Retrieve the hash-function definition.

See also

[**PEP 456**](https://peps.python.org/pep-0456/) “Secure and interchangeable hash algorithm”.

Added in version 3.4.

 Py_hash_t Py_HashPointer(const void *ptr)

Produce a hash from a pointer: the pointer is treated as an integer (internally cast to `uintptr_t`). No dereferencing of the pointer takes place.

There is no failure path here: a `-1` return is impossible.

Added in version 3.13.

 Py_hash_t Py_HashBuffer(const void *ptr, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) len)

Work out and hand back the hash for a buffer spanning *len* bytes that begins at the address *ptr*. That hash is promised to line up with the one from [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes), [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview), and the rest of the built-in objects backing the [buffer protocol](https://docs.python.org/3.14/c-api/buffer.html#bufferobjects).

Reach for this when you are wiring up hashing on an immutable object whose [`tp_richcompare`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_richcompare) routine measures itself against the buffer of another object.

The value of *len* has to be `0` or larger.

It never fails.

Added in version 3.14.

 Py_hash_t PyObject_GenericHash([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj)

A catch-all hashing routine intended to drop into the `tp_hash` slot of a type object. What it yields hinges solely on the object's identity.

**CPython implementation detail:** Within CPython this amounts to the same thing as `Py_HashPointer()`.

Added in version 3.13.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyhash-api.md) · [Previous source contract](py-uhash-t-to-pyhash-imag.md)
