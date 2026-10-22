# Text Sequence Type — `str`

### Text Sequence Type — `str`

In Python, textual content is represented by `str` objects, otherwise called *strings*. Each string is an immutable run of Unicode code points. You can spell out string literals in several styles:

- Single quotes: `'allows embedded "double" quotes'`

- Double quotes: `"allows embedded 'single' quotes"`

- Triple quoted: `'''Three single quotes'''`, `"""Three double quotes"""`

A triple-quoted string is allowed to run across several lines, and every bit of whitespace inside it ends up in the literal.

Where string literals belonging to one expression are divided by nothing but whitespace, the compiler quietly merges them into a single literal. So `("spam " "eggs") == "spam eggs"`.

Consult [String and Bytes literals](https://docs.python.org/3.14/reference/lexical_analysis.html#strings) for the full set of string-literal forms, the [escape sequences](https://docs.python.org/3.14/reference/lexical_analysis.html#escape-sequences) they accept, and the `r` (“raw”) prefix, which switches off most escape-sequence handling.

The `str` constructor offers another route, producing strings out of other objects.

Because Python has no distinct “character” type, subscripting a string yields one-character strings. In other words, given a non-empty string *s*, `s[0] == s[0:1]`.

Likewise no mutable string type exists, yet `str.join()` or [`io.StringIO`](https://docs.python.org/3.14/library/io.html#io.StringIO) lets you assemble strings from several pieces with good efficiency.

Changed in version 3.3: To stay compatible with the Python 2 line, string literals may once more carry the `u` prefix. That prefix changes nothing about what a string literal means, and it will not pair with the `r` prefix.

 *class *str(***, *encoding='utf-8'*, *errors='strict'*)

 *class *str(*object*)

 *class *str(*object*, *encoding*, *errors='strict'*)

 *class *str(*object*, ***, *errors*)

Hand back a string form of *object*. Supply no *object* and you get the empty string back. In every other case, how `str()` acts hinges on whether *encoding* or *errors* was passed, in the manner below.

Where you give neither *encoding* nor *errors*, `str(object)` yields [`type(object).__str__(object)`](https://docs.python.org/3.14/reference/datamodel.html#object.__str__) — the “informal” or pleasantly printable rendering of *object*. With a string object, that is simply the string as-is. Should *object* lack a `__str__()` method, `str()` instead resorts to giving back [`repr(object)`](https://docs.python.org/3.14/library/functions.html#repr).

Where one or both of *encoding* and *errors* is supplied, *object* ought to be a [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) (say, `bytes` or `bytearray`). Here, when *object* is a `bytes` (or `bytearray`) object, `str(bytes, encoding, errors)` amounts to `bytes.decode(encoding, errors)`. If not, the bytes object sitting behind the buffer object is fetched first, ahead of the `bytes.decode()` call. Consult Binary Sequence Types — bytes, bytearray, memoryview and the [Buffer Protocol](https://docs.python.org/3.14/c-api/buffer.html#bufferobjects) for details on buffer objects.

Handing a `bytes` object to `str()` with neither the *encoding* nor the *errors* arguments lands in that first scenario, returning the informal string rendering (note as well the [`-b`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-b) command-line option to Python). To illustrate:

```python
>>> str(b'Zoot!')
"b'Zoot!'"

```

For deeper coverage of the `str` class and what its methods do, turn to Text Sequence Type — str and the String Methods material further down. When you need formatted output, look at the [f-strings](https://docs.python.org/3.14/reference/lexical_analysis.html#f-strings) and [Format string syntax](https://docs.python.org/3.14/library/string.html#formatstrings) material. The [Text Processing Services](https://docs.python.org/3.14/library/text.html#stringservices) section is worth a look too.

[Subject index](INDEX.md) · [Previous](text-and-binary-sequence-type-methods-summary.md) · [Continue](str-capitalize-to-str-count.md)
