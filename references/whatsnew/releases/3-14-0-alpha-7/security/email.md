# Python 3.14.0 alpha 7 / security / email

[gh-121284](https://github.com/python/cpython/issues/121284): Fixed a bug in how rfc2047 encoded-words are folded while flattening an email message under a modern email policy. Formerly, an encoded-word too long for a line would get decoded, broken across lines, and re-encoded. Yet commas and other special characters from the original text might be left unencoded and unquoted. In theory this offered a way to spoof header lines through a carefully crafted encoded-word, should the rendered email then be transmitted or re-parsed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
