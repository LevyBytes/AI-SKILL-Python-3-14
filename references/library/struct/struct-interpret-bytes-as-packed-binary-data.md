# struct`struct` - Interpret bytes as packed binary data

# Struct

### `struct` - Interpret bytes as packed binary data

**Source code:** [Lib/struct.py](https://github.com/python/cpython/tree/3.14/Lib/struct.py)

---

Use this module to translate back and forth between Python values and C structs that are held as Python [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) objects. Terse format strings spell out which conversions you want to and from Python values. There are two broadly separate ways its functions and objects get used: shuttling data to and from outside sources such as files or network sockets, and moving data between your Python program and the C layer underneath.

Note

If you supply no prefix character, native mode applies by default. In that mode packing and unpacking follow whatever platform and compiler the running Python interpreter was compiled with. Packing a particular C struct yields pad bytes that keep the involved C types correctly aligned, and unpacking honors that same alignment. By contrast, once you move data across external sources it falls to the programmer to settle the byte order and any padding sitting between the fields. Consult Byte Order, Size, and Alignment for the specifics.

A number of `struct` functions, plus methods on `Struct`, accept a *buffer* argument. What that means is an object satisfying the [Buffer Protocol](https://docs.python.org/3.14/c-api/buffer.html#bufferobjects) that exposes a buffer which is either readable or read-writable. By far the usual choices here are [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) and [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray); however, plenty of additional types presentable as a byte array also support the buffer protocol, letting them be read or filled in place with no extra copy out of a `bytes` object.

[Subject index](INDEX.md) · [Continue](struct-error-to-struct-calcsize.md)
