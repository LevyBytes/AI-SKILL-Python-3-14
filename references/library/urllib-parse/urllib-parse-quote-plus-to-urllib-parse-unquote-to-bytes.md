# urllib.parse: `urllib.parse.quote_plus()`, `urllib.parse.quote_from_bytes()`, `urllib.parse.unquote()`, `urllib.parse.unquote_plus()`, `urllib.parse.unquote_to_bytes()`

Swap out the special characters within *string* for their `%*xx*` escape form. The characters `'_.-~'`, along with letters and digits, are always left alone. Out of the box, the routine is meant for escaping the path portion of a URL. You can name extra ASCII characters to leave unescaped through the optional *safe* parameter, which starts out as `'/'`.

You can pass *string* as a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) object or, just as well, as a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) one.

Changed in version 3.7: URL-string quoting switched its basis from [**RFC 2396**](https://datatracker.ietf.org/doc/html/rfc2396.html) over to [**RFC 3986**](https://datatracker.ietf.org/doc/html/rfc3986.html). The “~” character now counts among the unreserved ones.

How non-ASCII characters get handled is governed by the optional *encoding* and *errors* parameters, in the same form the [`str.encode()`](https://docs.python.org/3.14/library/stdtypes.html#str.encode) method takes. The *encoding* value starts at `'utf-8'`, and *errors* starts at `'strict'`, so any character that can't be handled triggers a [`UnicodeEncodeError`](https://docs.python.org/3.14/library/exceptions.html#UnicodeEncodeError). Passing *encoding* or *errors* when *string* is already a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) produces a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

Keep in mind that `quote(string, safe, encoding, errors)` amounts to the same thing as `quote_from_bytes(string.encode(encoding, errors), safe)`.

Example: `quote('/El Niño/')` yields `'/El%20Ni%C3%B1o/'`.

 urllib.parse.quote_plus(*string*, *safe=''*, *encoding=None*, *errors=None*)

Mirrors `quote()`, and on top of that turns spaces into plus signs — the form needed when escaping HTML form values that go into a URL query string. Any plus sign already present in the input gets escaped unless it appears in *safe*. Here *safe* also does not begin at `'/'`.

Example: `quote_plus('/El Niño/')` yields `'%2FEl+Ni%C3%B1o%2F'`.

 urllib.parse.quote_from_bytes(*bytes*, *safe='/'*)

Mirrors `quote()`, except it expects a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object in place of a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), and skips the step of encoding a string into bytes.

Example: `quote_from_bytes(b'a&\xef')` yields `'a%26%EF'`.

 urllib.parse.unquote(*string*, *encoding='utf-8'*, *errors='replace'*)

Turn each `%*xx*` escape back into the single character it stands for. The optional *encoding* and *errors* parameters control the decoding of percent-encoded sequences into Unicode characters, taking the form that the [`bytes.decode()`](https://docs.python.org/3.14/library/stdtypes.html#bytes.decode) method accepts.

Here too, *string* is allowed to be a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) object or instead a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) one.

The *encoding* value starts out as `'utf-8'`, while *errors* starts out as `'replace'`, so any sequence that isn't valid gets swapped for a placeholder character.

Example: `unquote('/El%20Ni%C3%B1o/')` yields `'/El Niño/'`.

Changed in version 3.9: the *string* parameter now takes bytes as well as str objects, where formerly it took only str.

 urllib.parse.unquote_plus(*string*, *encoding='utf-8'*, *errors='replace'*)

Mirrors `unquote()`, and additionally converts plus signs into spaces, which is what unquoting HTML form values calls for.

*string* must be a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str).

Example: `unquote_plus('/El+Ni%C3%B1o/')` yields `'/El Niño/'`.

 urllib.parse.unquote_to_bytes(*string*)

Turn each `%*xx*` escape into the single octet it represents, handing back a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object.

As before, *string* can come in as a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) object or alternatively as a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) one.

When it arrives as a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), any non-ASCII characters left unescaped in *string* get turned into UTF-8 bytes.

Example: `unquote_to_bytes('a%26%EF')` yields `b'a&\xef'`.

[Subject index](INDEX.md) · [Continue](urllib-parse-urlencode.md) · [Owning module, declaration or section: urllib.parse](urllib-parse-parse-urls-into-components.md) · [Owning module, declaration or section: URL Quoting](urllib-parse-quote.md) · [Owning module, declaration or section: urllib.parse.quote](urllib-parse-quote.md) · [Preceding source contract and version conditions](urllib-parse-quote.md)
