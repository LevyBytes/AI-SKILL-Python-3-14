# stdtypes: Byte-string partitioning, translation and alignment

bytes.rpartition(*sep*, */*)

 bytearray.rpartition(*sep*, */*)

Divide the sequence at the final appearance of *sep*, then hand back a 3-tuple holding the portion preceding the separator, the separator itself (or its bytearray copy), and the portion following the separator. When the separator cannot be located, the returned 3-tuple holds two empty bytes or bytearray objects, with a copy of the original sequence appended.

The separator you search for can be any [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object).

 bytes.startswith(*prefix*[, *start*[, *end*]])

 bytearray.startswith(*prefix*[, *start*[, *end*]])

Yield `True` when the binary data begins with the given *prefix*; otherwise yield `False`. The *prefix* may instead be a tuple of prefixes to check for. Supplying the optional *start* begins the test at that index. Supplying the optional *end* halts the comparison at that index.

The prefix(es) you search for can be any [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object).

 bytes.translate(*table*, */*, *delete=b''*)

 bytearray.translate(*table*, */*, *delete=b''*)

Hand back a copy of the bytes or bytearray object in which every byte found in the optional *delete* argument is dropped, while the surviving bytes have been remapped through the supplied translation table, which has to be a bytes object 256 long.

The `bytes.maketrans()` method can build such a translation table for you.

Pass `None` for the *table* argument when the translation should only delete characters:

```python
>>> b'read this short text'.translate(None, b'aeiou')
b'rd ths shrt txt'

```

Changed in version 3.6: passing *delete* as a keyword argument is now supported.

The bytes and bytearray methods listed below carry default behaviours that presume ASCII compatible binary formats, yet they remain usable on arbitrary binary data once you supply suitable arguments. Be aware that none of the bytearray methods in this section operate in place; each one instead yields fresh objects.

 bytes.center(*width*, *fillbyte=b' '*, */*)

 bytearray.center(*width*, *fillbyte=b' '*, */*)

Hand back a copy of the object centered inside a sequence whose length is *width*. The specified *fillbyte* supplies the padding (an ASCII space by default). With `bytes` objects, you get the original sequence back whenever *width* does not exceed `len(s)`.

Note

The bytearray flavour of this method does *not* operate in place - it always yields a fresh object, even when nothing was altered.

 bytes.ljust(*width*, *fillbyte=b' '*, */*)

 bytearray.ljust(*width*, *fillbyte=b' '*, */*)

Hand back a copy of the object left justified inside a sequence whose length is *width*. The specified *fillbyte* supplies the padding (an ASCII space by default). With `bytes` objects, you get the original sequence back whenever *width* does not exceed `len(s)`.

Note

The bytearray flavour of this method does *not* operate in place - it always yields a fresh object, even when nothing was altered.

 bytes.lstrip(*bytes=None*, */*)

 bytearray.lstrip(*bytes=None*, */*)

Hand back a copy of the sequence in which the indicated leading bytes are dropped. The *bytes* argument is a binary sequence naming the collection of byte values to strip. When left out or set to `None`, the *bytes* argument falls back to dropping ASCII whitespace. Note that the *bytes* argument is not treated as a prefix; instead, every combination of its values gets stripped:

```python
>>> b'   spacious   '.lstrip()
b'spacious   '
>>> b'www.example.com'.lstrip(b'cmowz.')
b'example.com'

```

The binary sequence of byte values to drop can be any [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object). Consult `removeprefix()` for a method that strips a single prefix string instead of an entire set of characters. As an illustration:

```python
>>> b'Arthur: three!'.lstrip(b'Arthur: ')
b'ee!'
>>> b'Arthur: three!'.removeprefix(b'Arthur: ')
b'three!'

```

Note

The bytearray flavour of this method does *not* operate in place - it always yields a fresh object, even when nothing was altered.

[Subject index](INDEX.md) · [Previous](bytes-rindex-and-bytearray-rindex.md) · [Continue](bytes-rjust-to-bytearray-split.md) · [Owning module, declaration or section: Bytes and Bytearray Operations](bytes-count-to-bytearray-removeprefix.md)
