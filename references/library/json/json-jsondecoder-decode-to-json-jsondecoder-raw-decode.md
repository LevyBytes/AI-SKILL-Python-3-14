# json.JSONDecoder: `decode()`, `raw_decode()`

decode(*s*)

Hand back the Python representation of *s* (a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) instance holding a JSON document).

A `JSONDecodeError` is raised should the supplied JSON document be invalid.

 raw_decode(*s*)

Read a JSON document out of *s* (a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) whose start is a JSON document) and hand back a 2-tuple consisting of the Python representation and the index within *s* at which the document finished.

This is handy for pulling a JSON document out of a string that carries surplus data afterward.

[Subject index](INDEX.md) · [Previous](json-jsondecoder-class.md) · [Continue](json-jsonencoder-class-to-json-jsonencoder-iterencode.md) · [Owning module, declaration or section: json](json-encoding-and-decoding-overview.md) · [Owning module, declaration or section: json.JSONDecoder](json-jsondecoder-class.md) · [Owning module, declaration or section: Encoders and Decoders](json-jsondecoder-class.md)
