# json — Top-level Non-Object, Non-Array Values

### Top-level Non-Object, Non-Array Values

Under the now-superseded JSON spec from [**RFC 4627**](https://datatracker.ietf.org/doc/html/rfc4627.html), the topmost value of a JSON text had to be a JSON object or array (a Python [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) or [`list`](https://docs.python.org/3.14/library/stdtypes.html#list)) and was barred from being a JSON null, boolean, number, or string. That limitation was lifted by [**RFC 7159**](https://datatracker.ietf.org/doc/html/rfc7159.html), and neither this module's serializer nor its deserializer has ever enforced it.

Even so, to maximize interoperability you might choose to honor that limitation of your own accord.

[Subject index](INDEX.md) · [Previous](repeated-names-within-an-object.md) · [Continue](implementation-limitations.md) · [Owning module, declaration or section: json](json-encoding-and-decoding-overview.md)
