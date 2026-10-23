# json - Character Encodings

### Character Encodings

Per the RFC, JSON has to be carried in UTF-8, UTF-16, or UTF-32, and UTF-8 is the suggested default for the widest interoperability.

Although the RFC allows it without demanding it, the serializer here keeps *ensure_ascii=True* as its default, so the output is escaped and the strings it yields hold printable ASCII characters only.

Setting aside the *ensure_ascii* parameter, this module is framed purely around translating between Python objects and [`Unicode strings`](https://docs.python.org/3.14/library/stdtypes.html#str), so apart from that it never tackles character encodings head-on.

A byte order mark (BOM) at the head of a JSON text is forbidden by the RFC, and this module's serializer emits no BOM. While the RFC allows JSON deserializers to skip a leading BOM, it stops short of requiring it. Here, the deserializer instead throws a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) whenever a leading BOM turns up.

The RFC stops short of outright banning JSON strings that hold byte sequences with no valid Unicode mapping (unpaired UTF-16 surrogates, say), though it warns such cases can break interoperability. Out of the box, this module takes in and emits the code points behind those sequences whenever they appear in the original [`str`](https://docs.python.org/3.14/library/stdtypes.html#str).

[Subject index](INDEX.md) · [Previous](standard-compliance-and-interoperability.md) · [Owning module, declaration or section: json](json-encoding-and-decoding-overview.md) · [Continue](infinite-and-nan-number-values.md)
