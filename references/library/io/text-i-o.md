# io: Text stream encoding and newline translation

### Text I/O

Text I/O takes in and hands back [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) objects. Consequently, when the backing store is inherently byte-based (a file, say), data is encoded and decoded behind the scenes, and platform-specific newline characters may optionally be translated as well.

A text stream is most simply created via [`open()`](https://docs.python.org/3.14/library/functions.html#open), with an encoding given if you wish:

```python
f = open("myfile.txt", "r", encoding="utf-8")

```

You can also obtain in-memory text streams through `StringIO` objects:

```python
f = io.StringIO("some initial text data")

```

Note

If you are dealing with a non-blocking stream, keep in mind that read calls on text I/O objects may raise a [`BlockingIOError`](https://docs.python.org/3.14/library/exceptions.html#BlockingIOError) whenever the stream is unable to complete the request right away.

Full coverage of the text stream API appears in the documentation of `TextIOBase`.

### Text I/O

Text I/O layered over binary storage (a file, say) runs markedly slower than binary I/O over that same storage, since it has to convert between unicode and binary data by way of a character codec. This can grow apparent when working through enormous quantities of text data such as sizeable log files. On top of that, `tell()` and `seek()` are each rather slow on account of the reconstruction algorithm involved.

`StringIO`, on the other hand, is a native in-memory unicode container, so it performs at a speed comparable to `BytesIO`.

[Subject index](INDEX.md) · [Previous](io-core-tools-for-working-with-streams.md) · [Continue](binary-i-o.md) · [Owning module, declaration or section: io](io-core-tools-for-working-with-streams.md) · [Previous](binary-i-o.md) · [Continue](multi-threading.md)
