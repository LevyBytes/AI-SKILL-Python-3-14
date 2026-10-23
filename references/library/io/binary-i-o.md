# io - Binary I/O

### Binary I/O

Binary I/O (which also goes by *buffered I/O*) takes [bytes-like objects](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) and yields [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) objects. There is no encoding, decoding, or newline translation along the way. Streams of this category serve every variety of non-text data, and they also fit cases where you want to handle text data by hand.

A binary stream is most simply created via [`open()`](https://docs.python.org/3.14/library/functions.html#open) by putting `'b'` into the mode string:

```python
f = open("myfile.jpg", "rb")

```

You can also obtain in-memory binary streams through `BytesIO` objects:

```python
f = io.BytesIO(b"some initial binary data: \x00\x01")

```

Full coverage of the binary stream API appears in the docs of `BufferedIOBase`.

Additional routes to making text or binary streams may come from other library modules. Consult [`socket.socket.makefile()`](https://docs.python.org/3.14/library/socket.html#socket.socket.makefile) for one such example.

### Binary I/O

Because it reads and writes only sizeable chunks even when the user requests a lone byte, buffered I/O masks whatever inefficiency lurks in calling and running the operating system’s unbuffered I/O routines. How much you gain turns on the OS and on the variety of I/O being done. On certain current OSes such as Linux, for instance, unbuffered disk I/O can run just as quickly as buffered I/O. The takeaway, all the same, is that buffered I/O delivers predictable performance no matter the platform or the backing device. So for binary data, buffered I/O is nearly always the better choice over unbuffered I/O.

[Subject index](INDEX.md) · [Previous](text-i-o.md) · [Continue](raw-i-o.md) · [Owning module, declaration or section: io](io-core-tools-for-working-with-streams.md) · [Previous](performance.md) · [Continue](text-i-o.md)
