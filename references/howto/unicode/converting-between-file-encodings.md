# Converting Between File Encodings

#### Converting Between File Encodings

Translating between encodings seamlessly is what the [`StreamRecoder`](https://docs.python.org/3.14/library/codecs.html#codecs.StreamRecoder) class does: it consumes a stream that yields data in encoding #1 and presents itself as a stream yielding data in encoding #2.

Say, for example, you hold an input file *f* encoded in Latin-1; you can enclose it in a [`StreamRecoder`](https://docs.python.org/3.14/library/codecs.html#codecs.StreamRecoder) so that it yields bytes encoded in UTF-8:

```python
new_f = codecs.StreamRecoder(f,
    # en/decoder: used by read() to encode its results and
    # by write() to decode its input.
    codecs.getencoder('utf-8'), codecs.getdecoder('utf-8'),

    # reader/writer: used to read and write to the stream.
    codecs.getreader('latin-1'), codecs.getwriter('latin-1') )

```

[Subject index](INDEX.md) · [Previous source context](tips-for-writing-unicode-aware-programs.md) · [Following source context](files-in-an-unknown-encoding.md)
