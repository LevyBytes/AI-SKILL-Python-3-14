# Python 3.9.0 alpha 1 / core and builtins / text and unicode

[bpo-37348](https://bugs.python.org/issue?@action=redirect&bpo=37348): Inada Naoki contributed an optimization for decoding short ASCII strings via the UTF-8 and ascii codecs. Roughly 15% faster is `b"foo".decode()`.

[bpo-24214](https://bugs.python.org/issue?@action=redirect&bpo=24214): Bettered the surrogatepass error handler's support within the UTF-8 and UTF-16 incremental decoders.

[bpo-35551](https://bugs.python.org/issue?@action=redirect&bpo=35551): Refreshed encodings: - Dropped the ?tis260? encoding, an alias pointing at the nonexistent ?tactis? codec. - Introduced ?mac_centeuro? as an alias of the mac_latin2 encoding.

[bpo-37433](https://bugs.python.org/issue?@action=redirect&bpo=37433): Anthony Sottile fixed the `SyntaxError` indicator that printed an excess of spaces for multi-line strings.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
