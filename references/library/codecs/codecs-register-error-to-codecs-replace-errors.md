# codecs: `codecs.register_error()`, `codecs.lookup_error()`, `codecs.strict_errors()`, `codecs.ignore_errors()`, `codecs.replace_errors()`

### Error Handlers

So that error handling stays simple and consistent, codecs can offer assorted error handling schemes that are selected through the *errors* string argument:

```python
>>> 'German ß, ♬'.encode(encoding='ascii', errors='backslashreplace')
b'German \\xdf, \\u266c'
>>> 'German ß, ♬'.encode(encoding='ascii', errors='xmlcharrefreplace')
b'German &#223;, &#9836;'
```

These error handlers work with every Python Standard Encodings codec:

| Value | Meaning |
| --- | --- |
| `'strict'` | Raise `UnicodeError` (or one of its subclasses); this is the fallback behavior. Implemented in `strict_errors()`. |
| `'ignore'` | Drop the malformed data and proceed with no warning. Implemented in `ignore_errors()`. |
| `'replace'` | Swap in a replacement marker. While encoding, emit `?` (ASCII character); while decoding, emit `�` (U+FFFD, the official REPLACEMENT CHARACTER). Implemented in `replace_errors()`. |
| `'backslashreplace'` | Swap in backslashed escape sequences. While encoding, emit the hexadecimal form of the Unicode code point using the formats `\x*hh*` `\u*xxxx*` `\U*xxxxxxxx*`; while decoding, emit the hexadecimal form of the byte value using the format `\x*hh*`. Implemented in `backslashreplace_errors()`. |
| `'surrogateescape'` | While decoding, swap each byte for a lone surrogate code spanning `U+DC80` through `U+DCFF`. That code is later restored to the identical byte whenever the `'surrogateescape'` error handler runs during encoding of the data. (Consult **PEP 383** for the full story.) |

These error handlers apply solely to encoding (and only within [text encodings](https://docs.python.org/3.14/glossary.html#term-text-encoding)):

| Value | Meaning |
| --- | --- |
| `'xmlcharrefreplace'` | Swap in an XML/HTML numeric character reference — a decimal rendering of the Unicode code point in the format `&#*num*;`. Implemented in `xmlcharrefreplace_errors()`. |
| `'namereplace'` | Swap in `\N{...}` escape sequences; whatever sits between the braces is the Name property taken from the Unicode Character Database. Implemented in `namereplace_errors()`. |

Beyond those, the following error handler is tied to the specific codecs noted:

| Value | Codecs | Meaning |
| --- | --- | --- |
| `'surrogatepass'` | utf-8, utf-16, utf-32, utf-16-be, utf-16-le, utf-32-be, utf-32-le | Permit a surrogate code point (`U+D800` - `U+DFFF`) to be encoded and decoded just like an ordinary code point. Without it, these codecs flag any surrogate code point found in `str` as an error. |

Added in version 3.1: The `'surrogateescape'` and `'surrogatepass'` error handlers.

Changed in version 3.4: The `'surrogatepass'` error handler gained support for the utf-16* and utf-32* codecs.

Added in version 3.5: The `'namereplace'` error handler.

Changed in version 3.5: The `'backslashreplace'` error handler became usable for decoding and translating as well.

You can widen the range of accepted values by registering a fresh named error handler:

 codecs.register_error(*name*, *error_handler*, */*)

Register the error handling function *error_handler* under the name *name*. Whenever *name* is given as the errors parameter, the *error_handler* argument is invoked during encoding and decoding once an error occurs.

When encoding, *error_handler* is called with a [`UnicodeEncodeError`](https://docs.python.org/3.14/library/exceptions.html#UnicodeEncodeError) instance that carries the location details of the error. The handler must either re-raise that exception (or raise another one) or return a tuple holding a replacement for the unencodable slice of the input plus a position at which encoding ought to resume. That replacement may be either [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) or [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes). When the replacement is bytes, the encoder merely copies them into the output buffer. When the replacement is a string, the encoder encodes it. Encoding then picks up on the original input at the stated position. A negative position is interpreted relative to the end of the input string. Should the computed position fall out of bounds, an [`IndexError`](https://docs.python.org/3.14/library/exceptions.html#IndexError) is raised.

Decoding and translating behave much the same, except that [`UnicodeDecodeError`](https://docs.python.org/3.14/library/exceptions.html#UnicodeDecodeError) or [`UnicodeTranslateError`](https://docs.python.org/3.14/library/exceptions.html#UnicodeTranslateError) is handed to the handler and the replacement returned by the error handler is placed straight into the output.

Error handlers registered earlier (the standard ones included) can be retrieved by name:

 codecs.lookup_error(*name*, */*)

Return the error handler previously registered under the name *name*.

Raises a [`LookupError`](https://docs.python.org/3.14/library/exceptions.html#LookupError) in case the handler cannot be found.

The standard error handlers listed below are additionally exposed as module level functions:

 codecs.strict_errors(*exception*)

Implements the `'strict'` error handling.

Every encoding or decoding error raises a [`UnicodeError`](https://docs.python.org/3.14/library/exceptions.html#UnicodeError).

 codecs.ignore_errors(*exception*)

Implements the `'ignore'` error handling.

Malformed data is skipped; encoding or decoding carries on without further notice.

 codecs.replace_errors(*exception*)

Implements the `'replace'` error handling.

Puts `?` (ASCII character) in place of encoding errors, or `�` (U+FFFD, the official REPLACEMENT CHARACTER) in place of decoding errors.

[Subject index](INDEX.md) · [Previous](codec-base-classes.md) · [Continue](codecs-backslashreplace-errors-to-codecs-namereplace-errors.md) · [Owning module, declaration or section: codecs](codecs-encode-to-codecs-lookup.md)
