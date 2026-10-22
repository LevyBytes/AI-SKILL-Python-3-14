# io.BytesIO: `getbuffer()`, `getvalue()`, `read1()`, `readinto1()`

getbuffer()

Hand back a readable, writable view onto the buffer’s contents without duplicating them. Furthermore, altering the view will quietly propagate the changes through to the buffer’s contents:

```python
>>> b = io.BytesIO(b"abcdef")
>>> view = b.getbuffer()
>>> view[2:4] = b"56"
>>> b.getvalue()
b'ab56ef'

```

Note

For as long as the view is alive, neither resizing nor closing the `BytesIO` object is permitted.

Added in version 3.2.

 getvalue()

Hand back [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) holding the buffer’s full contents.

 read1(*size=-1*, */*)

For `BytesIO`, this behaves identically to `read()`.

Changed in version 3.7: The *size* argument is now optional.

 readinto1(*b*, */*)

For `BytesIO`, this behaves identically to `readinto()`.

Added in version 3.5.

[Subject index](INDEX.md) · [Previous](io-bytesio-class.md) · [Continue](io-bufferedreader-class-to-io-bufferedreader-read1.md) · [Owning module, declaration or section: io](io-core-tools-for-working-with-streams.md) · [Owning module, declaration or section: io.BytesIO](io-bytesio-class.md) · [Owning module, declaration or section: Buffered Streams](io-bytesio-class.md)
