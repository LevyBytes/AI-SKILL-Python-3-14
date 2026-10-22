# How do I read (or write) binary data?

### How do I read (or write) binary data?

When reading or writing intricate binary data formats, the [`struct`](https://docs.python.org/3.14/library/struct.html#module-struct) module is your best bet. It lets you take a string holding binary data (typically numbers) and turn it into Python objects, and the reverse as well.

As an example, the code below reads two 2-byte integers plus one 4-byte integer in big-endian format from a file:

```python
import struct

with open(filename, "rb") as f:
    s = f.read(8)
    x, y, z = struct.unpack(">hhl", s)

```

In the format string the ?>? forces big-endian data; ?h? reads a single ?short integer? (2 bytes) and ?l? reads a single ?long integer? (4 bytes) out of the string.

For data of a more uniform kind (say, a homogeneous list of ints or floats), the [`array`](https://docs.python.org/3.14/library/array.html#module-array) module is another option.

Note

When reading and writing binary data, you must open the file in binary mode (here, by passing `"rb"` to [`open()`](https://docs.python.org/3.14/library/functions.html#open)). Use `"r"` instead (the default) and the file opens in text mode, so `f.read()` returns [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) objects in place of [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) objects.

[Subject index](INDEX.md)
