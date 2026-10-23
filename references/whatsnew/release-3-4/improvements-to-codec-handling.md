# What's New In Python 3.4 / Improvements to Codec Handling - codecs

### Improvements to Codec Handling

From its very inception, the [`codecs`](https://docs.python.org/3.14/library/codecs.html#module-codecs) module was meant to function as a type-neutral dynamic system for encoding and decoding. Yet its tight integration with the Python text model, particularly the type restricted convenience methods sitting on the builtin [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) and [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) types, has long masked that reality.

A key step toward clearing up the situation: the [`codecs.encode()`](https://docs.python.org/3.14/library/codecs.html#codecs.encode) and [`codecs.decode()`](https://docs.python.org/3.14/library/codecs.html#codecs.decode) convenience functions now carry proper documentation across Python 2.7, 3.3 and 3.4. Although these functions have lived in the [`codecs`](https://docs.python.org/3.14/library/codecs.html#module-codecs) module (and the regression test suite has exercised them) ever since Python 2.4, formerly they could only be found via runtime introspection.

In contrast to the convenience methods on [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) and [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray), the [`codecs`](https://docs.python.org/3.14/library/codecs.html#module-codecs) convenience functions accept arbitrary codecs across both Python 2 and Python 3, instead of being confined to Unicode text encodings (in Python 3) or `basestring` <-> `basestring` conversions (in Python 2).

Within Python 3.4, the interpreter can recognize the known non-text encodings shipped in the standard library and steer users toward these general purpose convenience functions when suitable:

```python
>>> b"abcdef".decode("hex")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
LookupError: 'hex' is not a text encoding; use codecs.decode() to handle arbitrary codecs

>>> "hello".encode("rot13")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
LookupError: 'rot13' is not a text encoding; use codecs.encode() to handle arbitrary codecs

>>> open("foo.txt", encoding="hex")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
LookupError: 'hex' is not a text encoding; use codecs.open() to handle arbitrary codecs

```

In a related shift, wherever this is achievable without breaking backwards compatibility, exceptions thrown while encoding and decoding now get wrapped inside a chained exception of the matching type that names the codec responsible for the error:

```python
>>> import codecs

>>> codecs.decode(b"abcdefgh", "hex")
Traceback (most recent call last):
  File "/usr/lib/python3.4/encodings/hex_codec.py", line 20, in hex_decode
    return (binascii.a2b_hex(input), len(input))
binascii.Error: Non-hexadecimal digit found

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
binascii.Error: decoding with 'hex' codec failed (Error: Non-hexadecimal digit found)

>>> codecs.encode("hello", "bz2")
Traceback (most recent call last):
  File "/usr/lib/python3.4/encodings/bz2_codec.py", line 17, in bz2_encode
    return (bz2.compress(input), len(input))
  File "/usr/lib/python3.4/bz2.py", line 498, in compress
    return comp.compress(data) + comp.flush()
TypeError: 'str' does not support the buffer interface

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: encoding with 'bz2' codec failed (TypeError: 'str' does not support the buffer interface)

```

Lastly, as the samples above demonstrate, these enhancements have allowed bringing back the convenience aliases for the non-Unicode codecs that were themselves reinstated in Python 3.2. Consequently, encoding binary data to and from its hexadecimal form (for instance) can now be expressed as:

```python
>>> from codecs import encode, decode
>>> encode(b"hello", "hex")
b'68656c6c6f'
>>> decode(b"68656c6c6f", "hex")
b'hello'

```

The binary and text transforms shipped with the standard library are documented under [Binary Transforms](https://docs.python.org/3.14/library/codecs.html#binary-transforms) and [Text Transforms](https://docs.python.org/3.14/library/codecs.html#text-transforms).

(Contributed by Nick Coghlan in [bpo-7475](https://bugs.python.org/issue?@action=redirect&bpo=7475), [bpo-17827](https://bugs.python.org/issue?@action=redirect&bpo=17827), [bpo-17828](https://bugs.python.org/issue?@action=redirect&bpo=17828) and [bpo-19619](https://bugs.python.org/issue?@action=redirect&bpo=19619).)

[Subject index](INDEX.md) · [Previous source section](pep-446-newly-created-file-descriptors-are-non-inheritable.md) · [Next source section](pep-451-a-modulespec-type-for-the-import-system.md) · [Release/subject declaration](release-highlights.md)
