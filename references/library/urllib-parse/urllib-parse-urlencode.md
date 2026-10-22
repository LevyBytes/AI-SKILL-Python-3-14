# urllib.parse: `urllib.parse.urlencode()`

urllib.parse.urlencode(*query*, *doseq=False*, *safe=''*, *encoding=None*, *errors=None*, *quote_via=quote_plus*)

Take a mapping, or a sequence of two-element tuples whose entries may be [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) or [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) objects, and produce a percent-encoded ASCII text string. Should you intend that string as the *data* of a POST handled by [`urlopen()`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.urlopen), encode it to bytes first; skipping that step leads to a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

What comes out is a run of `key=value` pairs joined by `'&'` characters, with both the *key* and the *value* run through the *quote_via* function. The default choice, `quote_plus()`, escapes spaces as a `'+'` character and renders ‘/’ as `%2F`, matching the convention for GET requests (`application/x-www-form-urlencoded`). You may instead hand `quote()` as *quote_via*, which writes spaces as `%20` and leaves ‘/’ untouched. When you want the finest grip on what gets escaped, pick `quote` and give *safe* a value.

If you supply *query* as a sequence of two-element tuples, each tuple's opening element acts as a key and its second as a value. That value can itself be a sequence; when it is and the optional *doseq* parameter comes out `True`, a separate `key=value` pair joined by `'&'` is emitted for every item in the value sequence under that key. Within the encoded result, the parameters appear in the same order as the tuples in the sequence.

Those *safe*, *encoding*, and *errors* parameters get forwarded to *quote_via*, though *encoding* and *errors* travel through only when a given query element is a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str).

For undoing this encoding, the module supplies `parse_qs()` and `parse_qsl()`, which read query strings back into Python data structures.

See the [urllib examples](https://docs.python.org/3.14/library/urllib.request.html#urllib-examples) for a demonstration of using the `urllib.parse.urlencode()` method to build a URL's query string or the data body of a POST request.

Changed in version 3.2: *query* now accepts bytes alongside string objects.

Changed in version 3.5: the *quote_via* parameter was introduced.

Deprecated since version 3.14: it is now deprecated to accept objects whose value is false — for example `0` and `[]` — apart from empty strings, byte-like objects, and `None`.

See also

[WHATWG](https://url.spec.whatwg.org/) - URL Living standard

The Working Group behind the URL Standard, which lays out URLs, domains, IP addresses, the application/x-www-form-urlencoded format, and the API that goes with them.

[**RFC 3986**](https://datatracker.ietf.org/doc/html/rfc3986.html) - Uniform Resource Identifiers

This serves as the standard in force today (STD66), and edits to the urllib.parse module ought to stay in line with it. You will spot a few departures here and there, almost all of them kept for backward compatibility or to satisfy the de-facto parsing behavior that the major browsers commonly exhibit.

[**RFC 2732**](https://datatracker.ietf.org/doc/html/rfc2732.html) - Format for Literal IPv6 Addresses in URL’s.

It lays down what is required when parsing IPv6 URLs.

[**RFC 2396**](https://datatracker.ietf.org/doc/html/rfc2396.html) - Uniform Resource Identifiers (URI): Generic Syntax

The document that sets out the shared syntactic rules covering both Uniform Resource Names (URNs) and Uniform Resource Locators (URLs).

[**RFC 2368**](https://datatracker.ietf.org/doc/html/rfc2368.html) - The mailto URL scheme.

What is required when parsing mailto URL schemes.

[**RFC 1808**](https://datatracker.ietf.org/doc/html/rfc1808.html) - Relative Uniform Resource Locators

This Request For Comments spells out how an absolute URL and a relative one are combined, and it throws in a good many “Abnormal Examples” that dictate how the edge cases get handled.

[**RFC 1738**](https://datatracker.ietf.org/doc/html/rfc1738.html) - Uniform Resource Locators (URL)

It pins down the formal grammar and meaning that absolute URLs carry.

[Subject index](INDEX.md) · [Previous](urllib-parse-quote-plus-to-urllib-parse-unquote-to-bytes.md) · [Owning module, declaration or section: urllib.parse](urllib-parse-parse-urls-into-components.md) · [Owning module, declaration or section: URL Quoting](urllib-parse-quote.md)
