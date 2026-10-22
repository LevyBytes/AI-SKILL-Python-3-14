# json / Encoders and Decoders: `json.JSONEncoder`, `default()`, `encode()`, `iterencode()`

*class *json.JSONEncoder(***, *skipkeys=False*, *ensure_ascii=True*, *check_circular=True*, *allow_nan=True*, *sort_keys=False*, *indent=None*, *separators=None*, *default=None*)

Extensible JSON encoder for Python data structures.

Out of the box it handles these objects and types:

| Python | JSON |
| --- | --- |
| dict | object |
| list, tuple | array |
| str | string |
| int, float, int- & float-derived Enums | number |
| True | true |
| False | false |
| None | null |

Changed in version 3.4: Enum classes derived from int and from float are now supported.

To teach it about further objects, subclass it and write a `default()` method together with another method that, where possible, hands back a serializable object for `o`; otherwise it ought to defer to the superclass implementation (so that [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is raised).

When *skipkeys* is false (the default), trying to encode keys other than [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), [`int`](https://docs.python.org/3.14/library/functions.html#int), [`float`](https://docs.python.org/3.14/library/functions.html#float), [`bool`](https://docs.python.org/3.14/library/functions.html#bool) or `None` raises a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError). When *skipkeys* is true, those items are quietly omitted.

When *ensure_ascii* is true (the default), the result is assured to have every non-ASCII and non-printable character from the input escaped. When *ensure_ascii* is false, characters appear unchanged, save for those that have to be escaped: the quotation mark, the reverse solidus, and the control characters U+0000 through U+001F.

When *check_circular* is true (the default), lists, dicts, and custom encoded objects are examined for circular references while encoding so as to head off infinite recursion (which would raise a [`RecursionError`](https://docs.python.org/3.14/library/exceptions.html#RecursionError)). If it is false, no such examination happens.

When *allow_nan* is true (the default), `NaN`, `Infinity`, and `-Infinity` are encoded verbatim. Although this departs from the JSON specification, it lines up with the behavior of most JavaScript-based encoders and decoders. Otherwise, encoding such floats produces a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError).

When *sort_keys* is true (default: `False`), dictionary output is emitted sorted by key; this helps regression tests, since it lets JSON serializations be compared from one day to the next.

When *indent* is a non-negative integer or a string, the members of JSON arrays and objects are pretty-printed at that indentation level. An indent level that is 0, negative, or `""` inserts newlines only. `None` (the default) picks the most compact form. A positive integer indent adds that many spaces for each level. Where *indent* is a string (for example `"\t"`), that string indents each level.

Changed in version 3.2: Besides integers, *indent* may now be given as a string.

When given, *separators* is expected to be an `(item_separator, key_separator)` tuple. It defaults to `(', ', ': ')` when *indent* is `None` and to `(',', ': ')` otherwise. For the most compact JSON representation, supply `(',', ':')` so that no whitespace remains.

Changed in version 3.4: When *indent* is not `None`, the default becomes `(',', ': ')`.

When given, *default* is expected to be a function called for objects that cannot otherwise be serialized. It ought to hand back a JSON-encodable form of the object or raise a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError). When it is not given, a `TypeError` is raised.

Changed in version 3.6: All parameters are now [keyword-only](https://docs.python.org/3.14/glossary.html#keyword-only-parameter).

 default(*o*)

Write this method in a subclass so that it hands back a serializable object for *o*, or defers to the base implementation (so that a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is raised).

As an example, supporting arbitrary iterators could lead you to write `default()` along these lines:

```python
def default(self, o):
   try:
       iterable = iter(o)
   except TypeError:
       pass
   else:
       return list(iterable)
   # Let the base class default method raise the TypeError
   return super().default(o)

```

 encode(*o*)

Hand back a JSON string representation of a Python data structure, *o*. As an example:

```python
>>> json.JSONEncoder().encode({"foo": ["bar", "baz"]})
'{"foo": ["bar", "baz"]}'

```

 iterencode(*o*)

Encode the supplied object, *o*, yielding each string representation as it becomes available. As an example:

```python
for chunk in json.JSONEncoder().iterencode(bigobject):
    mysocket.write(chunk)

```

[Subject index](INDEX.md) · [Previous](json-jsondecoder-decode-to-json-jsondecoder-raw-decode.md) · [Continue](json-jsondecodeerror.md) · [Owning module, declaration or section: json](json-encoding-and-decoding-overview.md) · [Owning module, declaration or section: Encoders and Decoders](json-jsondecoder-class.md)
