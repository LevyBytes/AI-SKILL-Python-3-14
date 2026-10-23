# Built-in Functions

*class *bytearray(*source=b''*)

 *class *bytearray(*source*, *encoding*, *errors='strict'*)

Give back a fresh array of bytes. The [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) class is a mutable sequence holding integers within 0 <= x < 256. It carries nearly all the customary methods of mutable sequences, covered in [Mutable Sequence Types](https://docs.python.org/3.14/library/stdtypes.html#typesseq-mutable), plus most of the methods belonging to the [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) type, covered in [Bytes and Bytearray Operations](https://docs.python.org/3.14/library/stdtypes.html#bytes-methods).

You can initialize the array through several different routes by way of the optional *source* parameter:

- When it is a *string*, the *encoding* parameter (and, optionally, *errors*) is required as well; [`bytearray()`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) then renders the string to bytes through [`str.encode()`](https://docs.python.org/3.14/library/stdtypes.html#str.encode).

- When it is an *integer*, the array takes on that length and starts out filled with null bytes.

- When it is an object that supports the [buffer interface](https://docs.python.org/3.14/c-api/buffer.html#bufferobjects), a read-only buffer over that object seeds the bytes array.

- When it is an *iterable*, it has to be an iterable yielding integers within `0 <= x < 256`, which become the array’s starting contents.

Supply no argument and you get an array of length 0.

Consult [Binary Sequence Types - bytes, bytearray, memoryview](https://docs.python.org/3.14/library/stdtypes.html#binaryseq) and [Bytearray Objects](https://docs.python.org/3.14/library/stdtypes.html#typebytearray) as well.

[Subject index](INDEX.md) · [Previous](breakpoint.md) · [Continue](bytes-class-to-bytes-class.md) · [Owning module, declaration or section: Built-in Functions](INDEX.md)
