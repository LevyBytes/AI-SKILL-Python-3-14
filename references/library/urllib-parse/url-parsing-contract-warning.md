# urllib.parse — URL Parsing — Contract: Warning

Warning

`urlsplit()` performs no validation. Consult URL parsing security for the specifics.

Changed in version 3.2: IPv6 URL parsing support was added.

Changed in version 3.3: Per [**RFC 3986**](https://datatracker.ietf.org/doc/html/rfc3986.html), the fragment is now parsed across every URL scheme (barring a false *allow_fragments*). Before this, only an allowlist of fragment-supporting schemes applied.

Changed in version 3.6: A port number out of range now raises [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) rather than giving back [`None`](https://docs.python.org/3.14/library/constants.html#None).

Changed in version 3.8: Any character that influences netloc parsing under NFKC normalization now triggers a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError).

Changed in version 3.10: ASCII newline plus tab characters get stripped out of the URL.

Changed in version 3.12: Leading WHATWG C0 control characters and spaces get stripped out of the URL.

[Subject index](INDEX.md) · [Previous](urllib-parse-urlsplit.md) · [Continue](urllib-parse-parse-qs-to-urllib-parse-urlunparse.md) · [Owning module, declaration or section: urllib.parse](urllib-parse-parse-urls-into-components.md) · [Owning module, declaration or section: URL Parsing](url-parsing.md) · [Owning module, declaration or section: urllib.parse.urlsplit](urllib-parse-urlsplit.md)
