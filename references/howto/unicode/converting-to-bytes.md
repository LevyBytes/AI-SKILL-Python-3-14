# Converting to Bytes

### Converting to Bytes

The counterpart to [`bytes.decode()`](https://docs.python.org/3.14/library/stdtypes.html#bytes.decode) is [`str.encode()`](https://docs.python.org/3.14/library/stdtypes.html#str.encode); it hands back a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) representation of the Unicode string, encoded under the requested *encoding*.

The *errors* parameter mirrors the parameter on the [`decode()`](https://docs.python.org/3.14/library/stdtypes.html#bytes.decode) method but allows a handful of extra handlers. Joining `'strict'`, `'ignore'`, and `'replace'` (which here drops in a question mark where the unencodable character sat) are three more: `'xmlcharrefreplace'`, dropping in an XML character reference; `backslashreplace`, dropping in a `\uNNNN` escape sequence; and `namereplace`, dropping in a `\N{...}` escape sequence.

The example that follows demonstrates the various outcomes:

```python
>>> u = chr(40960) + 'abcd' + chr(1972)
>>> u.encode('utf-8')
b'\xea\x80\x80abcd\xde\xb4'
>>> u.encode('ascii')
Traceback (most recent call last):
    ...
UnicodeEncodeError: 'ascii' codec can't encode character '\ua000' in
  position 0: ordinal not in range(128)
>>> u.encode('ascii', 'ignore')
b'abcd'
>>> u.encode('ascii', 'replace')
b'?abcd?'
>>> u.encode('ascii', 'xmlcharrefreplace')
b'&#40960;abcd&#1972;'
>>> u.encode('ascii', 'backslashreplace')
b'\\ua000abcd\\u07b4'
>>> u.encode('ascii', 'namereplace')
b'\\N{YI SYLLABLE IT}abcd\\u07b4'
```

You will find the low-level routines for registering and reaching the available encodings inside the [`codecs`](https://docs.python.org/3.14/library/codecs.html#module-codecs) module. Building new encodings also calls for familiarity with the `codecs` module. That said, the encoding and decoding functions this module returns are generally lower-level than is comfortable, and crafting new encodings is a specialized job, so this HOWTO will leave the module aside.

[Subject index](INDEX.md) · [Previous source context](the-string-type.md) · [Following source context](unicode-literals-in-python-source-code.md)
