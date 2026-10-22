# 11.3. Working with binary data record layouts

### 11.3. Working with binary data record layouts

For handling binary record formats of varying length, the [`struct`](https://docs.python.org/3.14/library/struct.html#module-struct) module supplies the [`pack()`](https://docs.python.org/3.14/library/struct.html#struct.pack) and [`unpack()`](https://docs.python.org/3.14/library/struct.html#struct.unpack) functions. In the snippet below, the header data of a ZIP file is iterated over without recourse to the [`zipfile`](https://docs.python.org/3.14/library/zipfile.html#module-zipfile) module. The pack codes `"H"` and `"I"` stand for unsigned numbers of two and four bytes respectively, while the leading `"<"` signals standard size with little-endian byte ordering:

```python
import struct

with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):                      # show the first 3 file headers
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size     # skip to the next header

```

[Subject index](INDEX.md) · [Previous source section](templating.md) · [Following source section](multi-threading.md)
