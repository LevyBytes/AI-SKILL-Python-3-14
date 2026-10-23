# Binary Sequence Types`bytes`, `bytearray`, `memoryview`

### Binary Sequence Types`bytes`, `bytearray`, `memoryview`

`bytes` and `bytearray` are the fundamental built-in types for handling binary data. Backing them is `memoryview`, which leans on the [buffer protocol](https://docs.python.org/3.14/c-api/buffer.html#bufferobjects) to reach the memory held by other binary objects while avoiding a copy.

For compact storage of elementary data types such as 32-bit integers and IEEE754 double-precision floating values, turn to the [`array`](https://docs.python.org/3.14/library/array.html#module-array) module.

[Subject index](INDEX.md) · [Previous](string-format-conversion-table.md) · [Continue](bytes-class-to-bytes-class.md)
