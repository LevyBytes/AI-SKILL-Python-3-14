# Python 3.8.0 alpha 3 / security / text and unicode

[bpo-36216](https://bugs.python.org/issue?@action=redirect&bpo=36216): Makes urlsplit() raise ValueError whenever the URL holds characters that, under IDNA encoding (NFKC-normalization), decompose into characters that alter the way the URL gets parsed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
