# stdtypes: `bytearray`

### Bytearray Objects

`bytearray` objects are a mutable counterpart to `bytes` objects.

 *class *bytearray(*source=b''*)

 *class *bytearray(*source*, *encoding*, *errors='strict'*)

Bytearray objects have no literal syntax of their own; you instead build them every time by invoking the constructor:

- Creating an empty instance: `bytearray()`

- Creating a zero-filled instance with a given length: `bytearray(10)`

- From an iterable of integers: `bytearray(range(20))`

- Copying existing binary data via the buffer protocol: `bytearray(b'Hi!')`

Because bytearray objects can be mutated, they offer the mutable sequence operations on top of the shared bytes and bytearray operations laid out in Bytes and Bytearray Operations.

Also see the [bytearray](https://docs.python.org/3.14/library/functions.html#func-bytearray) built-in.

Given that 2 hexadecimal digits line up exactly with one byte, hexadecimal numbers see frequent use as a way to spell out binary data. For that reason, the bytearray type carries an extra class method for reading data in that notation:

[Subject index](INDEX.md) · [Previous](bytes-bytes-hex-to-bytes-bytes-hex.md) · [Continue](bytearray-bytearray-hex-to-bytearray-bytearray-resize.md)
