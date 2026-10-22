# Python 3.5.0 alpha 1 / library / urllib parse

[bpo-22118](https://bugs.python.org/issue?@action=redirect&bpo=22118): For resolving relative URLs, urllib.parse now follows RFC 3986 semantics in place of RFCs 1808 and 2396. Demian Brecht wrote the patch.

[bpo-20879](https://bugs.python.org/issue?@action=redirect&bpo=20879): Postpone setting up the encoding and decoding tables for the base32, ascii85 and base85 codecs inside the base64 module, and likewise postpone building the unquote_to_bytes() table of the urllib.parse module, so memory isn’t squandered when those modules go unused.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
