# struct - Examples

### Examples

Note

The native byte order examples — marked by the `'@'` format prefix, or by no prefix character at all — might differ from what your own machine yields, since that hinges on the platform and compiler.

Below, integers of three distinct sizes are packed and unpacked under big endian ordering:

```python
>>> from struct import *
>>> pack(">bhl", 1, 2, 3)
b'\x01\x00\x02\x00\x00\x00\x03'
>>> unpack('>bhl', b'\x01\x00\x02\x00\x00\x00\x03')
(1, 2, 3)
>>> calcsize('>bhl')
7

```

Try packing an integer that overflows the field as defined:

```python
>>> pack(">h", 99999)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
struct.error: 'h' format requires -32768 <= number <= 32767

```

Show how the `'s'` and `'c'` format characters differ:

```python
>>> pack("@ccc", b'1', b'2', b'3')
b'123'
>>> pack("@3s", b'123')
b'123'

```

You can give names to the unpacked fields by binding them to variables or by feeding the result into a named tuple:

```python
>>> record = b'raymond   \x32\x12\x08\x01\x08'
>>> name, serialnum, school, gradelevel = unpack('<10sHHb', record)

>>> from collections import namedtuple
>>> Student = namedtuple('Student', 'name serialnum school gradelevel')
>>> Student._make(unpack('<10sHHb', record))
Student(name=b'raymond   ', serialnum=4658, school=264, gradelevel=8)

```

Because padding is implicit in native mode, how you order the format characters can change the size there. Under standard mode it is up to you to add whatever padding you want. Notice in the first `pack` call further down that three NUL bytes appear right after the packed `'#'`, lining the next integer up on a four-byte boundary. The output here came from a little endian machine:

```python
>>> pack('@ci', b'#', 0x12131415)
b'#\x00\x00\x00\x15\x14\x13\x12'
>>> pack('@ic', 0x12131415, b'#')
b'\x15\x14\x13\x12#'
>>> calcsize('@ci')
8
>>> calcsize('@ic')
5

```

Given that the platform aligns its longs on 4-byte boundaries, the format `'llh0l'` shown here tacks two pad bytes onto the end:

```python
>>> pack('@llh0l', 1, 2, 3)
b'\x00\x00\x00\x01\x00\x00\x00\x02\x00\x03\x00\x00'

```

See also

Module [`array`](https://docs.python.org/3.14/library/array.html#module-array)

Stores uniform data packed into binary form.

Module [`json`](https://docs.python.org/3.14/library/json.html#module-json)

JSON encoder and decoder.

Module [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle)

Python object serialization.

[Subject index](INDEX.md) · [Previous](format-characters.md) · [Continue](applications.md) · [Owning module, declaration or section: struct](struct-interpret-bytes-as-packed-binary-data.md)
