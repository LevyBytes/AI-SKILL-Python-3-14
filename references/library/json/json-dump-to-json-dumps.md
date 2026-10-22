# json: `json.dump()`, `json.dumps()`

### Basic Usage

 json.dump(*obj*, *fp*, ***, *skipkeys=False*, *ensure_ascii=True*, *check_circular=True*, *allow_nan=True*, *cls=None*, *indent=None*, *separators=None*, *default=None*, *sort_keys=False*, ***kw*)

Write *obj* out as a JSON-formatted stream into *fp* (an object that behaves like a [file-like object](https://docs.python.org/3.14/glossary.html#term-file-like-object) and supports `.write()`), following this Python-to-JSON conversion table.

Note

Because JSON — unlike [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle) and [`marshal`](https://docs.python.org/3.14/library/marshal.html#module-marshal) — has no framing, calling `dump()` more than once against the same *fp* to write several objects yields a JSON file that is not valid.

Parameters:

- **obj** ([*object*](https://docs.python.org/3.14/library/functions.html#object)) – The Python object to be serialized.

- **fp** ([file-like object](https://docs.python.org/3.14/glossary.html#term-file-like-object)) – The file-like object *obj* will be serialized to. Output from the `json` module is always [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) rather than [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes), which means `fp.write()` has to accept `str` input.

- **skipkeys** ([*bool*](https://docs.python.org/3.14/library/functions.html#bool)) – When set to `True`, any key whose type is not one of the basic ones ([`str`](https://docs.python.org/3.14/library/stdtypes.html#str), [`int`](https://docs.python.org/3.14/library/functions.html#int), [`float`](https://docs.python.org/3.14/library/functions.html#float), `bool`, `None`) is dropped rather than triggering a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError). Default `False`.

- **ensure_ascii** ([*bool*](https://docs.python.org/3.14/library/functions.html#bool)) – When `True` (the default), every non-ASCII and non-printable character in the input is escaped in the result. When `False`, characters pass through unchanged, apart from those that have to be escaped: the quotation mark, the reverse solidus, and the control characters U+0000 through U+001F.

- **check_circular** ([*bool*](https://docs.python.org/3.14/library/functions.html#bool)) – When `False`, the check for circular references among container types is bypassed, so a circular reference ends in a [`RecursionError`](https://docs.python.org/3.14/library/exceptions.html#RecursionError) (or something worse). Default `True`.

- **allow_nan** ([*bool*](https://docs.python.org/3.14/library/functions.html#bool)) – When `False`, attempting to serialize out-of-range [`float`](https://docs.python.org/3.14/library/functions.html#float) values (`nan`, `inf`, `-inf`) raises a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError), keeping strictly to the JSON specification. When `True` (the default), the JavaScript counterparts (`NaN`, `Infinity`, `-Infinity`) are emitted instead.

- **cls** (a `JSONEncoder` subclass) – When supplied, names a custom JSON encoder whose `default()` method has been overridden so that custom datatypes can be serialized. When `None` (the default), `JSONEncoder` applies.

- **indent** ([*int*](https://docs.python.org/3.14/library/functions.html#int)* | *[*str*](https://docs.python.org/3.14/library/stdtypes.html#str)* | **None*) – Given a positive integer or a string, the members of JSON arrays and objects are pretty-printed at that indentation level. A positive integer adds that number of spaces for each level; a string (for instance `"\t"`) supplies the text used to indent each level. With zero, a negative value, or `""` (the empty string), only newlines appear. With `None` (the default), nothing newline-related is added.

- **separators** ([*tuple*](https://docs.python.org/3.14/library/stdtypes.html#tuple)* | **None*) – A two-tuple of the form `(item_separator, key_separator)`. When `None` (the default), *separators* becomes `(', ', ': ')` whenever *indent* is `None`, and `(',', ': ')` in all other cases. To squeeze JSON down to its smallest form, pass `(',', ':')` so no whitespace remains.

- **default** ([callable](https://docs.python.org/3.14/glossary.html#term-callable) | None) – A function invoked for any object that cannot otherwise be serialized. It is expected to hand back a JSON-encodable form of the object or to raise a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError). When `None` (the default), a `TypeError` is raised.

- **sort_keys** ([*bool*](https://docs.python.org/3.14/library/functions.html#bool)) – When `True`, dictionary output is emitted in key-sorted order. Default `False`.

Changed in version 3.2: Besides integers, *indent* may now be given as a string.

Changed in version 3.4: When *indent* is not `None`, the default becomes `(',', ': ')`.

Changed in version 3.6: All optional parameters are now [keyword-only](https://docs.python.org/3.14/glossary.html#keyword-only-parameter).

 json.dumps(*obj*, ***, *skipkeys=False*, *ensure_ascii=True*, *check_circular=True*, *allow_nan=True*, *cls=None*, *indent=None*, *separators=None*, *default=None*, *sort_keys=False*, ***kw*)

Render *obj* into a JSON-formatted [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) according to this conversion table. Each argument carries the same meaning it has in `dump()`.

Note

In JSON, the keys of key/value pairs are invariably of type [`str`](https://docs.python.org/3.14/library/stdtypes.html#str). Converting a dictionary to JSON forces all of its keys to become strings. Because of that coercion, round-tripping a dictionary through JSON and back may not reproduce the original. Put another way, `loads(dumps(x)) != x` whenever x contains non-string keys.

[Subject index](INDEX.md) · [Previous](json-json-encoder-and-decoder-code-example-import-json.md) · [Continue](json-load-to-json-loads.md) · [Owning module, declaration or section: json](json-encoding-and-decoding-overview.md)
