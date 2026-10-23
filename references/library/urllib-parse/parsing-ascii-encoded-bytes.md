# urllib.parse - Parsing ASCII Encoded Bytes

### Parsing ASCII Encoded Bytes

Originally the URL parsing functions were built to work on character strings only. In real use, being able to handle properly quoted and encoded URLs as sequences of ASCII bytes proves handy. Because of that, every URL parsing function in this module works on [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) and [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) objects in addition to [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) objects.

When [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) data goes in, the result too holds only `str` data. When [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) or [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) data goes in, the result holds only `bytes` data.

Trying to combine [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) data with [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) or [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) within one function call raises a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError), while trying to feed in non-ASCII byte values sets off a [`UnicodeDecodeError`](https://docs.python.org/3.14/library/exceptions.html#UnicodeDecodeError).

To make converting result objects between [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) and [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) easier, every return value from a URL parsing function offers either an `encode()` method (when the result holds `str` data) or a `decode()` method (when the result holds `bytes` data). These methods’ signatures align with those of the matching `str` and `bytes` methods (except the default encoding is `'ascii'` instead of `'utf-8'`). Each yields a value of the matching type, holding either `bytes` data (for `encode()` methods) or `str` data (for `decode()` methods).

Applications that must deal with potentially improperly quoted URLs carrying non-ASCII data will have to handle their own decoding from bytes to characters before they call the URL parsing methods.

What is described in this section holds only for the URL parsing functions. The URL quoting functions follow their own rules when emitting or accepting byte sequences, as spelled out in the documentation of each URL quoting function.

Changed in version 3.2: The URL parsing functions now take ASCII encoded byte sequences as well

[Subject index](INDEX.md) · [Previous](url-parsing-security.md) · [Continue](urllib-parse-splitresult-geturl.md) · [Owning module, declaration or section: urllib.parse](urllib-parse-parse-urls-into-components.md)
