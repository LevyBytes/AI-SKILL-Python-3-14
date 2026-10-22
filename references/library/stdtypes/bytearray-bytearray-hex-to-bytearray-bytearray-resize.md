# stdtypes / bytes, bytearray, memoryview / Bytearray Objects: `fromhex()`, `hex()`, `resize()`

*classmethod *fromhex(*string*, */*)

Decoding the supplied string object, this `bytearray` class method hands back a bytearray object. Every byte has to be represented by two hexadecimal digits in the string, and ASCII whitespace is skipped over.

```python
>>> bytearray.fromhex('2Ef0 F1f2  ')
bytearray(b'.\xf0\xf1\xf2')

```

Changed in version 3.7: across the string, `bytearray.fromhex()` now disregards every ASCII whitespace character rather than only spaces.

Changed in version 3.14: as input, `bytearray.fromhex()` now takes ASCII `bytes` along with [bytes-like objects](https://docs.python.org/3.14/glossary.html#term-bytes-like-object).

Going the other direction, a conversion function turns a bytearray object into its hexadecimal representation.

 hex(***, *bytes_per_sep=1*)

 hex(*sep*, *bytes_per_sep=1*)

Hand back a string object that holds, per byte of the instance, two hexadecimal digits.

```python
>>> bytearray(b'\xf0\xf1\xf2').hex()
'f0f1f2'

```

Added in version 3.5.

Changed in version 3.8: As with `bytes.hex()`, `bytearray.hex()` now takes optional *sep* and *bytes_per_sep* parameters for slotting separators among the bytes of the hex output.

 resize(*size*, */*)

Adjust the `bytearray` so it holds *size* bytes. The value of *size* has to be at least 0.

Should the `bytearray` have to shrink, any bytes past *size* get cut off.

Should the `bytearray` have to grow, every freshly added byte beyond *size* is filled with null bytes.

The effect matches this:

```python
>>> def resize(ba, size):
...     if len(ba) > size:
...         del ba[size:]
...     else:
...         ba += b'\0' * (size - len(ba))

```

Examples:

```python
>>> shrink = bytearray(b'abc')
>>> shrink.resize(1)
>>> (shrink, len(shrink))
(bytearray(b'a'), 1)
>>> grow = bytearray(b'abc')
>>> grow.resize(5)
>>> (grow, len(grow))
(bytearray(b'abc\x00\x00'), 5)

```

Added in version 3.14.

Because a bytearray object is a sequence of integers (much like a list), given a bytearray object *b*, `b[0]` yields an integer, whereas `b[0:1]` yields a bytearray object of length 1. (Text strings differ here, since indexing them and slicing them both yield a string of length 1.)

A bytearray object's representation relies on the bytes literal format (`bytearray(b'...')`), as that tends to be handier than, say, `bytearray([46, 46, 46])`. Turning a bytearray object into a list of integers is always possible with `list(b)`.

See also

For detailed information on thread-safety guarantees for `bytearray` objects, see [Thread safety for bytearray objects](https://docs.python.org/3.14/library/threadsafety.html#thread-safety-bytearray).

[Subject index](INDEX.md) · [Previous](bytearray-class-to-bytearray-class.md) · [Continue](bytes-count-to-bytearray-removeprefix.md) · [Owning module, declaration or section: bytearray; bytearray](bytearray-class-to-bytearray-class.md) · [Owning module, declaration or section: Bytearray Objects](bytearray-class-to-bytearray-class.md)
