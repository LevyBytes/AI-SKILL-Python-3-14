# Codec lookup API

### Codec lookup API

Across the functions below, the *encoding* string is first folded to all lower-case characters before lookup, which renders encodings located by this means effectively case-insensitive. Where no codec turns up, a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) gets set and `NULL` is handed back.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyCodec_Encoder(const char *encoding)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Obtain an encoder function for the given *encoding*.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyCodec_Decoder(const char *encoding)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Obtain a decoder function for the given *encoding*.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyCodec_IncrementalEncoder(const char *encoding, const char *errors)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Obtain an [`IncrementalEncoder`](https://docs.python.org/3.14/library/codecs.html#codecs.IncrementalEncoder) object for the given *encoding*.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyCodec_IncrementalDecoder(const char *encoding, const char *errors)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Obtain an [`IncrementalDecoder`](https://docs.python.org/3.14/library/codecs.html#codecs.IncrementalDecoder) object for the given *encoding*.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyCodec_StreamReader(const char *encoding, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *stream, const char *errors)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Obtain a [`StreamReader`](https://docs.python.org/3.14/library/codecs.html#codecs.StreamReader) factory function for the given *encoding*.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyCodec_StreamWriter(const char *encoding, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *stream, const char *errors)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Obtain a [`StreamWriter`](https://docs.python.org/3.14/library/codecs.html#codecs.StreamWriter) factory function for the given *encoding*.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pycodec-register-to-pycodec-decode.md) · [Following source contract](pycodec-registererror-to-pycodec-namereplaceerrors.md)
