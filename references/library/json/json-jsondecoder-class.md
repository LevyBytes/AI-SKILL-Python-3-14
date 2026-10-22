# json: `json.JSONDecoder`

### Encoders and Decoders

 *class *json.JSONDecoder(***, *object_hook=None*, *parse_float=None*, *parse_int=None*, *parse_constant=None*, *strict=True*, *object_pairs_hook=None*)

Simple JSON decoder.

By default it carries out these decoding translations:

| JSON | Python |
| --- | --- |
| object | dict |
| array | list |
| string | str |
| number (int) | int |
| number (real) | float |
| true | True |
| false | False |
| null | None |

Beyond that, it recognizes `NaN`, `Infinity`, and `-Infinity` as the matching `float` values, even though these fall outside the JSON spec.

*object_hook* names an optional function that receives the result of every decoded JSON object, and whatever it returns stands in for the supplied [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict). You can rely on this to supply custom deserializations (for example, to enable [JSON-RPC](https://www.jsonrpc.org) class hinting).

*object_pairs_hook* names an optional function that receives the result of every decoded JSON object as an ordered list of pairs. The value returned by *object_pairs_hook* is used in place of the [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict). This feature lets you build custom decoders. When *object_hook* is defined too, *object_pairs_hook* takes priority.

Changed in version 3.1: Added support for *object_pairs_hook*.

*parse_float* names an optional function that receives the string of every JSON float being decoded. The default behavior matches `float(num_str)`. You can use this to swap in a different datatype or parser for JSON floats (for example [`decimal.Decimal`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal)).

*parse_int* names an optional function that receives the string of every JSON int being decoded. The default behavior matches `int(num_str)`. You can use this to swap in a different datatype or parser for JSON integers (for example [`float`](https://docs.python.org/3.14/library/functions.html#float)).

*parse_constant* names an optional function that receives one of these strings: `'-Infinity'`, `'Infinity'`, `'NaN'`. You can use this to throw an exception whenever invalid JSON numbers appear.

When *strict* is false (`True` being the default), control characters are permitted within strings. Here, control characters means those whose character codes lie in the 0–31 range, among them `'\t'` (tab), `'\n'`, `'\r'` and `'\0'`.

Should the data being deserialized fail to be a valid JSON document, a `JSONDecodeError` is raised.

Changed in version 3.6: All parameters are now [keyword-only](https://docs.python.org/3.14/glossary.html#keyword-only-parameter).

[Subject index](INDEX.md) · [Previous](json-load-to-json-loads.md) · [Continue](json-jsondecoder-decode-to-json-jsondecoder-raw-decode.md) · [Owning module, declaration or section: json](json-encoding-and-decoding-overview.md)
