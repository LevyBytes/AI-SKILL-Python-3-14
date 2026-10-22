# struct — Byte Order, Size, and Alignment

### Byte Order, Size, and Alignment

Out of the box, C types take the machine’s own native format and byte order, kept aligned by inserting pad bytes where the C compiler’s rules require them. That default exists so the bytes of a packed struct line up perfectly with how the matching C struct sits in memory. Choosing native byte order and padding versus the standard formats comes down to what your application needs.

Failing that, you can put a leading character at the front of the format string to spell out the packed data’s byte order, size, and alignment, per this table:

| Character | Byte order | Size | Alignment |
| --- | --- | --- | --- |
| `@` | native | native | native |
| `=` | native | standard | none |
| `<` | little-endian | standard | none |
| `>` | big-endian | standard | none |
| `!` | network (= big-endian) | standard | none |

Should the leading character be none of the above, `'@'` is taken as the default.

Note

Take the value 1023 (written `0x3ff` in hexadecimal); its bytes come out as:

- `03 ff` in big-endian (`>`)

- `ff 03` in little-endian (`<`)

Python example:

```python
>>> import struct
>>> struct.pack('>h', 1023)
b'\x03\xff'
>>> struct.pack('<h', 1023)
b'\xff\x03'

```

Whether native byte order is big-endian or little-endian hinges on the host machine. To illustrate, Intel x86, AMD64 (x86-64), and Apple M1 run little-endian, whereas IBM z along with numerous older architectures run big-endian. Query [`sys.byteorder`](https://docs.python.org/3.14/library/sys.html#sys.byteorder) when you need to learn your machine’s endianness.

To fix native size and alignment the C compiler’s `sizeof` expression is consulted, and that always rides along with native byte order.

By contrast, standard size is governed solely by the format character — refer to the table over in the Format Characters section.

Mind the gap between `'@'` and `'='`: each adopts native byte order, yet only the second one standardizes size and alignment.

Writing `'!'` selects network byte order, which is invariably big-endian as laid down in [IETF RFC 1700](https://datatracker.ietf.org/doc/html/rfc1700).

You cannot request a non-native byte order to force byte-swapping; instead pick whichever of `'<'` or `'>'` suits you.

Notes:

1.

Automatic padding shows up solely in the gaps between one structure member and the next. None is placed at the front or the tail of the encoded struct.

2.

Choosing non-native size and alignment — say with ‘<’, ‘>’, ‘=’, and ‘!’ — suppresses padding entirely.

3.

If you want a structure’s tail aligned to some type’s alignment requirement, finish the format using that type’s code together with a zero repeat count. See Examples.

[Subject index](INDEX.md) · [Previous](format-strings.md) · [Continue](format-characters.md) · [Owning module, declaration or section: struct](struct-interpret-bytes-as-packed-binary-data.md)
