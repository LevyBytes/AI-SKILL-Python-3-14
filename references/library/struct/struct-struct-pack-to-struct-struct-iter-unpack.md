# struct.Struct: `pack()`, `pack_into()`, `unpack()`, `unpack_from()`, `iter_unpack()`

`pack(*v1*, *v2*, *...*)`

Behaves just like the `pack()` function but on the compiled format. (Here `len(result)` comes out equal to `size`.)

`pack_into(*buffer*, *offset*, *v1*, *v2*, *...*)`

Behaves just like the `pack_into()` function but on the compiled format.

`unpack(*buffer*)`

Behaves just like the `unpack()` function but on the compiled format. In bytes the buffer’s size has to equal `size`.

`unpack_from(*buffer*, *offset=0*)`

Behaves just like the `unpack_from()` function but on the compiled format. In bytes, measured from position *offset*, the buffer must be at least `size`.

`iter_unpack(*buffer*)`

Behaves just like the `iter_unpack()` function but on the compiled format. In bytes the buffer’s size has to be a multiple of `size`.

Added in version 3.4.

`format`

This is the format string that this Struct object was built from.

Changed in version 3.7: this format string is held as [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) these days in place of [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes).

`size`

This is the worked-out size of the struct — and thus of the bytes object the `pack()` method turns out — that matches [`format`](https://docs.python.org/3.14/library/functions.html#format).

Changed in version 3.13: a struct’s *repr()* output is different now, reading as:

```python
>>> Struct('i')
Struct('i')

```

[Subject index](INDEX.md) · [Previous](struct-struct-class.md) · [Owning module, declaration or section: struct](struct-interpret-bytes-as-packed-binary-data.md) · [Owning module, declaration or section: struct.Struct](struct-struct-class.md) · [Owning module, declaration or section: Classes](struct-struct-class.md)
