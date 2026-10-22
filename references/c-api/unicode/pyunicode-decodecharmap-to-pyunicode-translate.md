# Character Map Codecs

### Character Map Codecs

What makes this codec unusual is that it can serve to build many distinct codecs (and indeed that is how the bulk of the standard codecs in the `encodings` package were produced). Mappings drive how the codec encodes and decodes characters. Each mapping object that is supplied has to honor the [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__) mapping interface; dictionaries and sequences serve well.

The mapping codec APIs are listed below:

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_DecodeCharmap(const char *str, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) length, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *mapping, const char *errors)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Build a Unicode object by decoding *size* bytes from the encoded string *str* by way of the supplied *mapping* object. Return `NULL` if the codec raised an exception.

When *mapping* is `NULL`, Latin-1 decoding takes effect. Otherwise *mapping* has to map byte ordinals (integers in the range from 0 to 255) onto Unicode strings, integers (which then count as Unicode ordinals) or `None`. Data bytes that go unmapped – those that trigger a [`LookupError`](https://docs.python.org/3.14/library/exceptions.html#LookupError), together with those that map to `None`, `0xFFFE` or `'\ufffe'` – count as undefined mappings and produce an error.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_AsCharmapString([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *mapping)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Use the supplied *mapping* object to encode a Unicode object and hand back the outcome as a bytes object. Error handling is “strict”. Return `NULL` if the codec raised an exception.

The *mapping* object has to map Unicode ordinal integers onto bytes objects, integers in the range from 0 to 255 or `None`. Character ordinals that go unmapped (those that trigger a [`LookupError`](https://docs.python.org/3.14/library/exceptions.html#LookupError)) along with those mapped to `None` count as “undefined mapping” and produce an error.

The codec API below is unusual in that it maps Unicode onto Unicode.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_Translate([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *table, const char *errors)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Apply a character mapping table to a string to translate it, then hand back the Unicode object that results. Return `NULL` if the codec raised an exception.

The mapping table has to map Unicode ordinal integers onto Unicode ordinal integers or `None` (which deletes the character).

A mapping table only needs to provide the [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__) interface; dictionaries and sequences serve well. Character ordinals that go unmapped (those that trigger a [`LookupError`](https://docs.python.org/3.14/library/exceptions.html#LookupError)) stay untouched and are copied verbatim.

*errors* carries its usual codec meaning. It may be `NULL`, which signals that the default error handling should apply.

[Subject index](INDEX.md) · [Previous source contract](pyunicode-decodeascii-to-pyunicode-asasciistring.md) · [Following source contract](pyunicode-decodembcs-to-pyunicode-encodecodepage.md)
