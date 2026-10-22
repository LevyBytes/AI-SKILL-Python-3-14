# stdtypes: `int.from_bytes()`, `int.as_integer_ratio()`, `int.is_integer()`

*classmethod *int.from_bytes(*bytes*, *byteorder='big'*, ***, *signed=False*)

Return the integer that the supplied byte array represents.

```python
>>> int.from_bytes(b'\x00\x10', byteorder='big')
16
>>> int.from_bytes(b'\x00\x10', byteorder='little')
4096
>>> int.from_bytes(b'\xfc\x00', byteorder='big', signed=True)
-1024
>>> int.from_bytes(b'\xfc\x00', byteorder='big', signed=False)
64512
>>> int.from_bytes([255, 0, 0], byteorder='big')
16711680

```

The *bytes* argument has to be either a [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) or an iterable that yields bytes.

How the integer is laid out in bytes is governed by the *byteorder* argument, which defaults to `"big"`. With *byteorder* set to `"big"`, the most significant byte sits at the start of the byte array. With *byteorder* set to `"little"`, the most significant byte sits at the end of the byte array. When you want the host system's native byte order, pass [`sys.byteorder`](https://docs.python.org/3.14/library/sys.html#sys.byteorder) as the byte order value.

Whether two’s complement gets used to represent the integer is signaled by the *signed* argument.

Equivalent to:

```python
def from_bytes(bytes, byteorder='big', signed=False):
    if byteorder == 'little':
        little_ordered = list(bytes)
    elif byteorder == 'big':
        little_ordered = list(reversed(bytes))
    else:
        raise ValueError("byteorder must be either 'little' or 'big'")

    n = sum(b << i*8 for i, b in enumerate(little_ordered))
    if signed and little_ordered and (little_ordered[-1] & 0x80):
        n -= 1 << 8*len(little_ordered)

    return n

```

Added in version 3.2.

Changed in version 3.11: Added default argument value for `byteorder`.

 int.as_integer_ratio()

Return a pair of integers whose ratio matches the original integer and carries a positive denominator. For integers (whole numbers), that ratio is always the integer itself as numerator over `1` as denominator.

Added in version 3.8.

 int.is_integer()

Returns `True`. It exists so that duck typing lines up with `float.is_integer()`.

Added in version 3.12.

[Subject index](INDEX.md) · [Previous](int-to-bytes.md) · [Continue](float-as-integer-ratio-to-float-hex.md) · [Owning module, declaration or section: Additional Methods on Integer Types](int-bit-length-to-int-bit-count.md)
