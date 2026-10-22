# stdtypes: `int.to_bytes()`

int.to_bytes(*length=1*, *byteorder='big'*, ***, *signed=False*)

Return a byte array that represents an integer.

```python
>>> (1024).to_bytes(2, byteorder='big')
b'\x04\x00'
>>> (1024).to_bytes(10, byteorder='big')
b'\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00'
>>> (-1024).to_bytes(10, byteorder='big', signed=True)
b'\xff\xff\xff\xff\xff\xff\xff\xff\xfc\x00'
>>> x = 1000
>>> x.to_bytes((x.bit_length() + 7) // 8, byteorder='little')
b'\xe8\x03'

```

The integer gets represented with *length* bytes, which defaults to 1. Should the integer not fit in the given number of bytes, an [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) is raised.

How the integer is laid out in bytes is governed by the *byteorder* argument, which defaults to `"big"`. With *byteorder* set to `"big"`, the most significant byte sits at the start of the byte array. With *byteorder* set to `"little"`, the most significant byte sits at the end of the byte array.

Whether two’s complement gets used to represent the integer is governed by the *signed* argument. Passing a negative integer while *signed* is `False` raises an [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError). The default for *signed* is `False`.

You can lean on the defaults to handily convert an integer into a single byte object:

```python
>>> (65).to_bytes()
b'A'

```

That said, while relying on the default arguments, refrain from converting a value above 255, or you'll be handed an [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError).

Equivalent to:

```python
def to_bytes(n, length=1, byteorder='big', signed=False):
    if byteorder == 'little':
        order = range(length)
    elif byteorder == 'big':
        order = reversed(range(length))
    else:
        raise ValueError("byteorder must be either 'little' or 'big'")

    return bytes((n >> i*8) & 0xff for i in order)

```

Added in version 3.2.

Changed in version 3.11: Added default argument values for `length` and `byteorder`.

[Subject index](INDEX.md) · [Previous](int-bit-length-to-int-bit-count.md) · [Continue](int-as-integer-ratio-to-int-is-integer.md) · [Owning module, declaration or section: Additional Methods on Integer Types](int-bit-length-to-int-bit-count.md)
