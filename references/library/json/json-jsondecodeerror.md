# json — Exceptions

### Exceptions

 *exception *json.JSONDecodeError(*msg*, *doc*, *pos*)

Subclass of [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) carrying these extra attributes:

 msg

The unformatted error message.

 doc

The JSON document being parsed.

 pos

The start index of *doc* where parsing failed.

 lineno

The line corresponding to *pos*.

 colno

The column corresponding to *pos*.

Added in version 3.5.

[Subject index](INDEX.md) · [Previous](json-jsonencoder-class-to-json-jsonencoder-iterencode.md) · [Continue](standard-compliance-and-interoperability.md) · [Owning module, declaration or section: json](json-encoding-and-decoding-overview.md)
