# stdtypes: `bytes.strip()`, `bytearray.strip()`, `bytes.capitalize()`, `bytearray.capitalize()`, `bytes.expandtabs()`, `bytearray.expandtabs()`, `bytes.isalnum()`, `bytearray.isalnum()`, `bytes.isalpha()`, `bytearray.isalpha()`

bytes.strip(*bytes=None*, */*)

 bytearray.strip(*bytes=None*, */*)

Hand back a copy of the sequence in which the indicated leading and trailing bytes are dropped. The *bytes* argument is a binary sequence naming the collection of byte values to strip. When left out or set to `None`, the *bytes* argument falls back to dropping ASCII whitespace. Note that the *bytes* argument is treated as neither a prefix nor a suffix; instead, every combination of its values gets stripped:

```python
>>> b'   spacious   '.strip()
b'spacious'
>>> b'www.example.com'.strip(b'cmowz.')
b'example'

```

The binary sequence of byte values to drop can be any [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object).

Note

The bytearray flavour of this method does *not* operate in place - it always yields a fresh object, even when nothing was altered.

The bytes and bytearray methods listed below presume ASCII compatible binary formats and ought not to be used on arbitrary binary data. Be aware that none of the bytearray methods in this section operate in place; each one instead yields fresh objects.

 bytes.capitalize()

 bytearray.capitalize()

Hand back a copy of the sequence in which each byte is read as an ASCII character, with the first byte made uppercase and everything else made lowercase. Byte values outside ASCII are carried over unchanged.

Note

The bytearray flavour of this method does *not* operate in place - it always yields a fresh object, even when nothing was altered.

 bytes.expandtabs(*tabsize=8*)

 bytearray.expandtabs(*tabsize=8*)

Hand back a copy of the sequence in which every ASCII tab character is swapped for one or more ASCII spaces, the count depending on the current column and the supplied tab size. Tab stops land every *tabsize* bytes (8 by default, which puts tab stops at columns 0, 8, 16 and onward). To expand the sequence, the current column starts at zero and the sequence is walked byte by byte. Should that byte be an ASCII tab character (`b'\t'`), spaces (one or several) get appended to the result until the current column reaches the next tab stop. (The tab character itself is not carried over.) When the present byte is an ASCII newline (`b'\n'`) or carriage return (`b'\r'`), it is carried over and the current column is reset to zero. Every other byte value is carried over unchanged and the current column rises by one, no matter how that byte value looks when printed:

```python
>>> b'01\t012\t0123\t01234'.expandtabs()
b'01      012     0123    01234'
>>> b'01\t012\t0123\t01234'.expandtabs(4)
b'01  012 0123    01234'

```

Note

The bytearray flavour of this method does *not* operate in place - it always yields a fresh object, even when nothing was altered.

 bytes.isalnum()

 bytearray.isalnum()

Yield `True` when every byte in the sequence is an alphabetical ASCII character or an ASCII decimal digit and the sequence is non-empty; otherwise yield `False`. Alphabetic ASCII characters are the byte values in the sequence `b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'`. ASCII decimal digits are the byte values in the sequence `b'0123456789'`.

As an illustration:

```python
>>> b'ABCabc1'.isalnum()
True
>>> b'ABC abc1'.isalnum()
False

```

 bytes.isalpha()

 bytearray.isalpha()

Yield `True` when every byte in the sequence is an alphabetic ASCII character and the sequence is non-empty; otherwise yield `False`. Alphabetic ASCII characters are the byte values in the sequence `b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'`.

As an illustration:

```python
>>> b'ABCabc'.isalpha()
True
>>> b'ABCabc1'.isalpha()
False

```

[Subject index](INDEX.md) · [Previous](bytes-rjust-to-bytearray-split.md) · [Continue](bytes-isascii-to-bytearray-isupper.md) · [Owning module, declaration or section: Bytes and Bytearray Operations](bytes-count-to-bytearray-removeprefix.md)
