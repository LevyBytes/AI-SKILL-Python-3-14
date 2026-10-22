# base64 — Legacy Interface

### Legacy Interface

 base64.decode(*input*, *output*)

Read and decode whatever the binary *input* file holds, then write the binary data that results into the *output* file. Both *input* and *output* have to be [file objects](https://docs.python.org/3.14/glossary.html#term-file-object). Reading from *input* keeps going until `input.readline()` hands back an empty bytes object.

 base64.decodebytes(*s*)

Decode the [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) *s* - which has to hold one or more lines of base64 encoded data - and give back the resulting [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes).

Added in version 3.1.

 base64.encode(*input*, *output*)

Read and encode whatever the binary *input* file holds, then write the base64 encoded data that results into the *output* file. Both *input* and *output* have to be [file objects](https://docs.python.org/3.14/glossary.html#term-file-object). Reading from *input* keeps going until `input.read()` hands back an empty bytes object. After every 76 bytes of output, `encode()` drops in a newline character (`b'\n'`), and it likewise guarantees the output finishes with a newline, in line with [**RFC 2045**](https://datatracker.ietf.org/doc/html/rfc2045.html) (MIME).

 base64.encodebytes(*s*)

Encode the [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) *s* - which may carry any arbitrary binary data - and give back [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) holding the base64-encoded data, with newlines (`b'\n'`) dropped in after every 76 bytes of output and a trailing newline guaranteed, all in line with [**RFC 2045**](https://datatracker.ietf.org/doc/html/rfc2045.html) (MIME).

Added in version 3.1.

A sample showing the module in action:

```python
>>> import base64
>>> encoded = base64.b64encode(b'data to be encoded')
>>> encoded
b'ZGF0YSB0byBiZSBlbmNvZGVk'
>>> data = base64.b64decode(encoded)
>>> data
b'data to be encoded'

```

[Subject index](INDEX.md) · [Previous](base64-z85decode.md) · [Continue](security-considerations.md) · [Owning module, declaration or section: base64](base64-base16-base32-base64-base85-data-encodings.md)
