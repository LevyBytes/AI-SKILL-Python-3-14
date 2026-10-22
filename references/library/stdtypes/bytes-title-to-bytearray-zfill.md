# stdtypes: `bytes.title()`, `bytearray.title()`, `bytes.upper()`, `bytearray.upper()`, `bytes.zfill()`, `bytearray.zfill()`

bytes.title()

 bytearray.title()

Hand back a titlecased rendition of the binary sequence in which words open with an uppercase ASCII character and the rest of the characters are lowercase. Uncased byte values stay untouched.

As an illustration:

```python
>>> b'Hello world'.title()
b'Hello World'

```

Lowercase ASCII characters are the byte values in the sequence `b'abcdefghijklmnopqrstuvwxyz'`. Uppercase ASCII characters are the byte values in the sequence `b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`. Every other byte value is uncased.

The algorithm leans on a straightforward language-independent notion of a word as runs of consecutive letters. That notion holds up in many situations, but it does mean apostrophes inside contractions and possessives act as word boundaries, which might not be what you want:

```python
>>> b"they're bill's friends from the UK".title()
b"They'Re Bill'S Friends From The Uk"

```

You can craft a workaround for apostrophes with regular expressions:

```python
>>> import re
>>> def titlecase(s):
...     return re.sub(rb"[A-Za-z]+('[A-Za-z]+)?",
...                   lambda mo: mo.group(0)[0:1].upper() +
...                              mo.group(0)[1:].lower(),
...                   s)
...
>>> titlecase(b"they're bill's friends.")
b"They're Bill's Friends."

```

Note

The bytearray flavour of this method does *not* operate in place - it always yields a fresh object, even when nothing was altered.

 bytes.upper()

 bytearray.upper()

Hand back a copy of the sequence in which all the lowercase ASCII characters are turned into their matching uppercase counterpart.

As an illustration:

```python
>>> b'Hello World'.upper()
b'HELLO WORLD'

```

Lowercase ASCII characters are the byte values in the sequence `b'abcdefghijklmnopqrstuvwxyz'`. Uppercase ASCII characters are the byte values in the sequence `b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`.

Note

The bytearray flavour of this method does *not* operate in place - it always yields a fresh object, even when nothing was altered.

 bytes.zfill(*width*, */*)

 bytearray.zfill(*width*, */*)

Hand back a copy of the sequence padded on the left with ASCII `b'0'` digits to reach a sequence of length *width*. A leading sign prefix (`b'+'`/ `b'-'`) is dealt with by placing the padding *after* the sign character rather than ahead of it. With `bytes` objects, you get the original sequence back whenever *width* does not exceed `len(seq)`.

As an illustration:

```python
>>> b"42".zfill(5)
b'00042'
>>> b"-42".zfill(5)
b'-0042'

```

Note

The bytearray flavour of this method does *not* operate in place - it always yields a fresh object, even when nothing was altered.

[Subject index](INDEX.md) · [Previous](bytes-lower-to-bytearray-swapcase.md) · [Continue](printf-bytes-formatting-overview.md) · [Owning module, declaration or section: Bytes and Bytearray Operations](bytes-count-to-bytearray-removeprefix.md)
