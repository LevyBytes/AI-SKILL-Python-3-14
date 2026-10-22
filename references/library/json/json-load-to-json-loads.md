# json: `json.load()`, `json.loads()`

json.load(*fp*, ***, *cls=None*, *object_hook=None*, *parse_float=None*, *parse_int=None*, *parse_constant=None*, *object_pairs_hook=None*, ***kw*)

Turn *fp* back into a Python object by applying the JSON-to-Python conversion table.

Parameters:

- **fp** ([file-like object](https://docs.python.org/3.14/glossary.html#term-file-like-object)) – A [text file](https://docs.python.org/3.14/glossary.html#term-text-file) or [binary file](https://docs.python.org/3.14/glossary.html#term-binary-file) supporting `.read()` that holds the JSON document to be deserialized.

- **cls** (a `JSONDecoder` subclass) – When supplied, a custom JSON decoder. Any extra keyword arguments handed to `load()` are forwarded to the constructor of *cls*. When `None` (the default), `JSONDecoder` is used.

- **object_hook** ([callable](https://docs.python.org/3.14/glossary.html#term-callable) | None) – When supplied, a function invoked with whatever results from decoding each JSON object literal (a [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict)). Whatever it returns replaces the `dict`. This mechanism enables custom decoders, such as [JSON-RPC](https://www.jsonrpc.org) class hinting. Default `None`.

- **object_pairs_hook** ([callable](https://docs.python.org/3.14/glossary.html#term-callable) | None) – When supplied, a function invoked with whatever results from decoding each JSON object literal, delivered as an ordered list of pairs. Its return value supplants the [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict). This mechanism enables custom decoders. Should *object_hook* be supplied as well, *object_pairs_hook* wins. Default `None`.

- **parse_float** ([callable](https://docs.python.org/3.14/glossary.html#term-callable) | None) – When supplied, a function invoked with the string of each JSON float being decoded. When `None` (the default), the effect matches `float(num_str)`. Use this to turn JSON floats into custom datatypes, for instance [`decimal.Decimal`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal).

- **parse_int** ([callable](https://docs.python.org/3.14/glossary.html#term-callable) | None) – When supplied, a function invoked with the string of each JSON int being decoded. When `None` (the default), the effect matches `int(num_str)`. Use this to turn JSON integers into custom datatypes, for instance [`float`](https://docs.python.org/3.14/library/functions.html#float).

- **parse_constant** ([callable](https://docs.python.org/3.14/glossary.html#term-callable) | None) – When supplied, a function invoked with whichever of these strings applies: `'-Infinity'`, `'Infinity'`, or `'NaN'`. Use this to throw an exception whenever invalid JSON numbers turn up. Default `None`.

Raises:

- **JSONDecodeError** – When the data being deserialized is not a valid JSON document.

- [**UnicodeDecodeError**](https://docs.python.org/3.14/library/exceptions.html#UnicodeDecodeError) – Raised when the bytes handed in for decoding are not encoded as UTF-8, UTF-16 or UTF-32.

Changed in version 3.1:

- Added the optional *object_pairs_hook* parameter.

- *parse_constant* doesn’t get called on ‘null’, ‘true’, ‘false’ anymore.

Changed in version 3.6:

- All optional parameters are now [keyword-only](https://docs.python.org/3.14/glossary.html#keyword-only-parameter).

- *fp* is now allowed to be a [binary file](https://docs.python.org/3.14/glossary.html#term-binary-file); whatever encoding it carries ought to be UTF-8, UTF-16 or UTF-32.

Changed in version 3.11: To guard against denial-of-service attacks, the default *parse_int* of [`int()`](https://docs.python.org/3.14/library/functions.html#int) now caps how long an integer string may be, drawing on the interpreter’s [integer string conversion length limitation](https://docs.python.org/3.14/library/stdtypes.html#int-max-str-digits).

 json.loads(*s*, ***, *cls=None*, *object_hook=None*, *parse_float=None*, *parse_int=None*, *parse_constant=None*, *object_pairs_hook=None*, ***kw*)

Behaves just like `load()`, except that rather than a file-like object it deserializes *s* (a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) or [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) instance holding a JSON document) into a Python object via this conversion table.

Changed in version 3.6: *s* is now permitted to be [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) or [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) as well; whatever encoding it uses ought to be UTF-8, UTF-16 or UTF-32.

Changed in version 3.9: The keyword argument *encoding* has been removed.

[Subject index](INDEX.md) · [Previous](json-dump-to-json-dumps.md) · [Continue](json-jsondecoder-class.md) · [Owning module, declaration or section: json](json-encoding-and-decoding-overview.md) · [Owning module, declaration or section: Basic Usage](json-dump-to-json-dumps.md)
