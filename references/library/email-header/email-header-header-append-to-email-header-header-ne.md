# email.header.Header: `append()`, `encode()`, `__str__()`, `__eq__()`, `__ne__()`

append(*s*, *charset=None*, *errors='strict'*)

Tack the string *s* onto the MIME header.

When supplied, the optional *charset* should be either a [`Charset`](https://docs.python.org/3.14/library/email.charset.html#email.charset.Charset) instance (refer to [`email.charset`](https://docs.python.org/3.14/library/email.charset.html#module-email.charset)) or a character set's name, which then gets turned into a `Charset` instance. Passing `None` (the default) tells it to fall back on the *charset* that was named in the constructor.

The value *s* can be a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) or [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) instance. Where it is a `bytes` instance, *charset* names the encoding of that byte string, and a [`UnicodeError`](https://docs.python.org/3.14/library/exceptions.html#UnicodeError) is raised should the string fail to decode under that character set.

Where *s* is a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) instance, *charset* acts as a hint about the character set of the string's characters.

Whichever the case, while a header is being built to comply with [**RFC 2822**](https://datatracker.ietf.org/doc/html/rfc2822.html) under [**RFC 2047**](https://datatracker.ietf.org/doc/html/rfc2047.html) rules, the string is encoded through the charset's output codec. Should that output codec be unable to encode the string, a UnicodeError is raised.

The optional *errors* is forwarded as the errors argument of the decode call whenever *s* is a byte string.

 encode(*splitchars=';, \t'*, *maxlinelen=None*, *linesep='\n'*)

Turn a message header into an RFC-compliant form, wrapping long lines where needed and wrapping non-ASCII portions in base64 or quoted-printable encodings.

The optional *splitchars* is a string of characters that the splitting algorithm leans on more heavily during ordinary header wrapping. It loosely echoes [**RFC 2822**](https://datatracker.ietf.org/doc/html/rfc2822.html)'s ‘higher level syntactic breaks’: when lines are split, break points sitting just after a splitchar are favoured, and the characters are favoured in the same order they occur in the string. You may put space and tab into the string to express which of the two is preferred as a break point in lines where none of the other split chars turn up. Lines that are [**RFC 2047**](https://datatracker.ietf.org/doc/html/rfc2047.html) encoded are left untouched by splitchars.

When given, *maxlinelen* takes the place of the instance's own maximum-line-length value.

The *linesep* names the characters that divide the folded header's lines. Its default is the value most convenient for Python application code (`\n`), though you may set `\r\n` to turn out headers whose line separators comply with the RFC.

Changed in version 3.2: Added the *linesep* argument.

On top of that, the `Header` class supplies several methods that back the standard operators and built-in functions.

 __str__()

Hands back a string that approximates the `Header`, treating the line length as unbounded. Each piece is turned into unicode through the encoding given and then stitched together as appropriate. Whichever pieces carry a charset of `'unknown-8bit'` get decoded as ASCII by way of the `'replace'` error handler.

Changed in version 3.2: Added handling for the `'unknown-8bit'` charset.

 __eq__(*other*)

With this method you can check two `Header` instances for equality.

 __ne__(*other*)

With this method you can check two `Header` instances for inequality.

The `email.header` module rounds things out with the handy functions below.

[Subject index](INDEX.md) · [Previous](email-header-header-class.md) · [Continue](email-header-decode-header-to-email-header-make-header.md) · [Owning module, declaration or section: email.header](email-header-header-class.md) · [Owning module, declaration or section: email.header.Header](email-header-header-class.md)
