# urllib.parse: `urllib.parse.parse_qs()`, `urllib.parse.parse_qsl()`, `urllib.parse.urlunsplit()`, `urllib.parse.urlparse()`, `urllib.parse.urlunparse()`

urllib.parse.parse_qs(*qs*, *keep_blank_values=False*, *strict_parsing=False*, *encoding='utf-8'*, *errors='replace'*, *max_num_fields=None*, *separator='&'*)

Parse a query string supplied as a string argument (data of type *application/x-www-form-urlencoded*). The result comes back as a dictionary, whose keys are the distinct query variable names and whose values are lists holding the values for each name.

The optional *keep_blank_values* argument is a flag governing whether blank values in percent-encoded queries should count as blank strings. A true value means blanks are kept as blank strings. The default false value means blank values are dropped and treated as though they had never appeared.

The optional *strict_parsing* argument is a flag governing the handling of parsing errors. When false (the default), errors pass by silently. When true, errors raise a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) exception.

The optional *encoding* and *errors* parameters dictate how percent-encoded sequences are decoded into Unicode characters, in the manner the [`bytes.decode()`](https://docs.python.org/3.14/library/stdtypes.html#bytes.decode) method accepts.

The optional *max_num_fields* argument caps how many fields are read. When it is set, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is thrown if more than *max_num_fields* fields are read.

The optional *separator* argument is the symbol that divides the query arguments. Its default is `&`.

To turn dictionaries like these back into query strings, use the `urllib.parse.urlencode()` function with the `doseq` parameter set to `True`.

Changed in version 3.2: The *encoding* and *errors* parameters were added.

Changed in version 3.8: The *max_num_fields* parameter was added.

Changed in version 3.10: The *separator* parameter was added, defaulting to `&`. Releases before Python 3.10 let you use either `;` or `&` as a query parameter separator; that was narrowed to one single separator key, defaulting to `&`.

Deprecated since version 3.14: It is now deprecated to accept objects that are falsy (such as `0` and `[]`), apart from empty strings, byte-like objects, and `None`.

 urllib.parse.parse_qsl(*qs*, *keep_blank_values=False*, *strict_parsing=False*, *encoding='utf-8'*, *errors='replace'*, *max_num_fields=None*, *separator='&'*)

Parse a query string supplied as a string argument (data of type *application/x-www-form-urlencoded*). The result comes back as a list of name, value pairs.

The optional *keep_blank_values* argument is a flag governing whether blank values in percent-encoded queries should count as blank strings. A true value means blanks are kept as blank strings. The default false value means blank values are dropped and treated as though they had never appeared.

The optional *strict_parsing* argument is a flag governing the handling of parsing errors. When false (the default), errors pass by silently. When true, errors raise a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) exception.

The optional *encoding* and *errors* parameters dictate how percent-encoded sequences are decoded into Unicode characters, in the manner the [`bytes.decode()`](https://docs.python.org/3.14/library/stdtypes.html#bytes.decode) method accepts.

The optional *max_num_fields* argument caps how many fields are read. When it is set, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is thrown if more than *max_num_fields* fields are read.

The optional *separator* argument is the symbol that divides the query arguments. Its default is `&`.

To turn lists of pairs like these into query strings, use the `urllib.parse.urlencode()` function.

Changed in version 3.2: Introduced the *encoding* and *errors* parameters.

Changed in version 3.8: Introduced the *max_num_fields* parameter.

Changed in version 3.10: Introduced the *separator* parameter, whose default value is `&`. In Python releases prior to 3.10, both `;` and `&` were accepted as a query parameter separator; this was tightened so that just one separator key is permitted, with `&` serving as the default.

 urllib.parse.urlunsplit(*parts*)

Build a URL out of a tuple of the kind `urlsplit()` returns. The *parts* argument may be any five-item iterable. The outcome can be a marginally different yet equivalent URL when the URL originally parsed carried superfluous delimiters (such as a `?` with an empty query; per the RFC, those count as equivalent).

 urllib.parse.urlparse(*urlstring*, *scheme=None*, *allow_fragments=True*)

This works like `urlsplit()`, except it also breaks the *path* piece apart into *path* and *params*. The function hands back a 6-item [named tuple](https://docs.python.org/3.14/glossary.html#term-named-tuple) `ParseResult` or `ParseResultBytes`. Its elements match those of the `urlsplit()` result, save that *params* is slotted in at index 3, between *path* and *query*.

The basis for this function is the obsoleted [**RFC 1738**](https://datatracker.ietf.org/doc/html/rfc1738.html) and [**RFC 1808**](https://datatracker.ietf.org/doc/html/rfc1808.html), which named *params* the principal URL component. Newer URL syntax permits parameters on each segment of the URL’s *path* portion (refer to [**RFC 3986**](https://datatracker.ietf.org/doc/html/rfc3986.html)). As a rule, prefer `urlsplit()` over `urlparse()`. Pulling the path segments and parameters apart calls for a dedicated function.

 urllib.parse.urlunparse(*parts*)

Join the pieces of a tuple of the kind `urlparse()` returns into one complete URL as a string. The *parts* argument may be any six-item iterable. The outcome can be a marginally different yet equivalent URL when the URL originally parsed carried superfluous delimiters (such as a ? with an empty query; per the RFC, those count as equivalent).

[Subject index](INDEX.md) · [Previous](url-parsing-contract-warning.md) · [Continue](urllib-parse-urljoin-to-urllib-parse-unwrap.md) · [Owning module, declaration or section: urllib.parse](urllib-parse-parse-urls-into-components.md) · [Owning module, declaration or section: URL Parsing](url-parsing.md)
