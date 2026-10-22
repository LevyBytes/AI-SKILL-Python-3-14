# struct — Format Strings

### Format Strings

When you pack or unpack, the format string is what lays out the data. You assemble it from format characters, each of which names the kind of data being packed or unpacked. On top of those, certain special characters dictate byte order, size, and alignment. A format string is made of an optional leading prefix character that states the data's overall traits, followed by one or more format characters that name the actual values and their padding.

[Subject index](INDEX.md) · [Previous](struct-error-to-struct-calcsize.md) · [Continue](byte-order-size-and-alignment.md) · [Owning module, declaration or section: struct](struct-interpret-bytes-as-packed-binary-data.md)
