# io.TextIOWrapper: `seek()`, `tell()`

seek(*cookie*, *whence=os.SEEK_SET*, */*)

Set where the stream is positioned. Hand back the new stream position as an [`int`](https://docs.python.org/3.14/library/functions.html#int).

The following argument combinations name the four supported operations:

- `seek(0, SEEK_SET)`: Rewind to the start of the stream.

- `seek(cookie, SEEK_SET)`: Restore a previous position; *cookie* **must be** a number returned by `tell()`.

- `seek(0, SEEK_END)`: Fast-forward to the end of the stream.

- `seek(0, SEEK_CUR)`: Leave the current stream position unchanged.

Every other argument combination is invalid and may raise exceptions.

See also

[`os.SEEK_SET`](https://docs.python.org/3.14/library/os.html#os.SEEK_SET), [`os.SEEK_CUR`](https://docs.python.org/3.14/library/os.html#os.SEEK_CUR), and [`os.SEEK_END`](https://docs.python.org/3.14/library/os.html#os.SEEK_END).

 tell()

Hand back the stream position as an opaque number. Whatever `tell()` returns can be fed into `seek()` to restore a previous stream position.

[Subject index](INDEX.md) · [Previous](io-textiowrapper-class-to-io-textiowrapper-reconfigure.md) · [Continue](io-stringio-class-to-io-stringio-getvalue.md) · [Owning module, declaration or section: io](io-core-tools-for-working-with-streams.md) · [Owning module, declaration or section: io.TextIOWrapper](io-textiowrapper-class-to-io-textiowrapper-reconfigure.md) · [Owning module, declaration or section: Text I/O](io-textiobase-class.md)
