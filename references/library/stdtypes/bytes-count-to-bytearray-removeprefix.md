# stdtypes: `bytes.count()`, `bytearray.count()`, `bytes.removeprefix()`, `bytearray.removeprefix()`

### Bytes and Bytearray Operations

The common sequence operations work on both bytes and bytearray objects. They cooperate not only with operands sharing their type but with any [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object). Thanks to that latitude, you can intermix them in operations without triggering errors. Still, which type comes back as the result can hinge on how the operands are ordered.

Note

The methods belonging to bytes and bytearray objects won't take strings as arguments, just as string methods won't take bytes as arguments. So, for example, you must write:

```python
a = "abc"
b = a.replace("a", "f")

```

and:

```python
a = b"abc"
b = a.replace(b"a", b"f")

```

A number of bytes and bytearray operations presume ASCII compatible binary formats, so they're best left aside when handling arbitrary binary data. The relevant limits are detailed below.

Note

Applying these ASCII based operations to binary data held in a format that isn't ASCII based can corrupt that data.

You can apply the following methods of bytes and bytearray objects to arbitrary binary data.

 bytes.count(*sub*[, *start*[, *end*]])

 bytearray.count(*sub*[, *start*[, *end*]])

Return how many times the subsequence *sub* occurs without overlap inside the range [*start*, *end*]. The optional *start* and *end* arguments follow slice notation conventions.

For the subsequence you're after, any [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) is acceptable, as is an integer from 0 to 255.

When *sub* is empty, the count returned is the number of empty slices sitting between characters, which equals the bytes object's length plus one.

Changed in version 3.3: An integer from 0 to 255 is now also taken as the subsequence.

 bytes.removeprefix(*prefix*, */*)

 bytearray.removeprefix(*prefix*, */*)

When the binary data leads off with the *prefix* string, return `bytes[len(prefix):]`. If not, return a copy of the original binary data:

```python
>>> b'TestHook'.removeprefix(b'Test')
b'Hook'
>>> b'BaseTestCase'.removeprefix(b'Test')
b'BaseTestCase'

```

The *prefix* may be any [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object).

Note

The bytearray flavour of this method works *not* in place — it consistently builds a fresh object, regardless of whether anything changed.

Added in version 3.9.

[Subject index](INDEX.md) · [Previous](bytearray-bytearray-hex-to-bytearray-bytearray-resize.md) · [Continue](bytes-removesuffix-to-bytearray-index.md)
