# stdtypes / bytes, bytearray, memoryview / Bytes Objects: `fromhex()`, `hex()`

*classmethod *fromhex(*string*, */*)

Decoding the supplied string object, this `bytes` class method hands back a bytes object. Every byte has to be represented by two hexadecimal digits in the string, and ASCII whitespace is skipped over.

```python
>>> bytes.fromhex('2Ef0 F1f2  ')
b'.\xf0\xf1\xf2'

```

Changed in version 3.7: across the string, `bytes.fromhex()` now disregards every ASCII whitespace character rather than only spaces.

Changed in version 3.14: as input, `bytes.fromhex()` now takes ASCII `bytes` along with [bytes-like objects](https://docs.python.org/3.14/glossary.html#term-bytes-like-object).

Going the other direction, a conversion function turns a bytes object into its hexadecimal representation.

 hex(***, *bytes_per_sep=1*)

 hex(*sep*, *bytes_per_sep=1*)

Hand back a string object that holds, per byte of the instance, two hexadecimal digits.

```python
>>> b'\xf0\xf1\xf2'.hex()
'f0f1f2'

```

To render the hex string more legibly, you can hand it a single-character separator *sep* parameter for inclusion in the output. That separator is, by default, dropped in between every byte. A further optional *bytes_per_sep* parameter governs the spacing. A positive value counts the separator placement starting from the right, while a negative value counts from the left.

```python
>>> value = b'\xf0\xf1\xf2'
>>> value.hex('-')
'f0-f1-f2'
>>> value.hex('_', 2)
'f0_f1f2'
>>> b'UUDDLRLRAB'.hex(' ', -4)
'55554444 4c524c52 4142'

```

Added in version 3.5.

Changed in version 3.8: `bytes.hex()` now takes optional *sep* and *bytes_per_sep* parameters for slotting separators among the bytes of the hex output.

Because a bytes object is a sequence of integers (much like a tuple), given a bytes object *b*, `b[0]` yields an integer, whereas `b[0:1]` yields a bytes object of length 1. (Text strings differ here, since indexing them and slicing them both yield a string of length 1.)

A bytes object's representation relies on the literal format (`b'...'`), as that tends to be handier than, say, `bytes([46, 46, 46])`. Turning a bytes object into a list of integers is always possible with `list(b)`.

[Subject index](INDEX.md) · [Previous](bytes-class-to-bytes-class.md) · [Continue](bytearray-class-to-bytearray-class.md) · [Owning module, declaration or section: bytes; bytes](bytes-class-to-bytes-class.md) · [Owning module, declaration or section: Bytes Objects](bytes-class-to-bytes-class.md)
