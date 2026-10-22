# stdtypes: `bytes.lower()`, `bytearray.lower()`, `bytes.splitlines()`, `bytearray.splitlines()`, `bytes.swapcase()`, `bytearray.swapcase()`

bytes.lower()

 bytearray.lower()

Hand back a copy of the sequence in which all the uppercase ASCII characters are turned into their matching lowercase counterpart.

As an illustration:

```python
>>> b'Hello World'.lower()
b'hello world'

```

Lowercase ASCII characters are the byte values in the sequence `b'abcdefghijklmnopqrstuvwxyz'`. Uppercase ASCII characters are the byte values in the sequence `b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`.

Note

The bytearray flavour of this method does *not* operate in place - it always yields a fresh object, even when nothing was altered.

 bytes.splitlines(*keepends=False*)

 bytearray.splitlines(*keepends=False*)

Hand back a list of the lines within the binary sequence, breaking at ASCII line boundaries. This method relies on the [universal newlines](https://docs.python.org/3.14/glossary.html#term-universal-newlines) approach for breaking lines apart. Line breaks stay out of the resulting list unless *keepends* is supplied and true.

As an illustration:

```python
>>> b'ab c\n\nde fg\rkl\r\n'.splitlines()
[b'ab c', b'', b'de fg', b'kl']
>>> b'ab c\n\nde fg\rkl\r\n'.splitlines(keepends=True)
[b'ab c\n', b'\n', b'de fg\r', b'kl\r\n']

```

In contrast to `split()` when a delimiter string *sep* is supplied, this method hands back an empty list for the empty string, and a trailing line break does not add an extra line:

```python
>>> b"".split(b'\n'), b"Two lines\n".split(b'\n')
([b''], [b'Two lines', b''])
>>> b"".splitlines(), b"One line\n".splitlines()
([], [b'One line'])

```

 bytes.swapcase()

 bytearray.swapcase()

Hand back a copy of the sequence in which all the lowercase ASCII characters are turned into their matching uppercase counterpart and vice-versa.

As an illustration:

```python
>>> b'Hello World'.swapcase()
b'hELLO wORLD'

```

Lowercase ASCII characters are the byte values in the sequence `b'abcdefghijklmnopqrstuvwxyz'`. Uppercase ASCII characters are the byte values in the sequence `b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`.

In contrast to `str.swapcase()`, the binary versions always satisfy `bin.swapcase().swapcase() == bin`. Case conversions stay symmetrical in ASCII, although the same is not generally true for arbitrary Unicode code points.

Note

The bytearray flavour of this method does *not* operate in place - it always yields a fresh object, even when nothing was altered.

[Subject index](INDEX.md) · [Previous](bytes-isascii-to-bytearray-isupper.md) · [Continue](bytes-title-to-bytearray-zfill.md) · [Owning module, declaration or section: Bytes and Bytearray Operations](bytes-count-to-bytearray-removeprefix.md)
