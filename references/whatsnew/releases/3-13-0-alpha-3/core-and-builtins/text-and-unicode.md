# Python 3.13.0 alpha 3 / core and builtins / text and unicode

[gh-99606](https://github.com/python/cpython/issues/99606): Have the code generated for an empty f-string match the code generated for an empty normal string.

[gh-94606](https://github.com/python/cpython/issues/94606): Resolved a UnicodeEncodeError arising when `email.message.get_payload()` reads a message holding a Unicode surrogate character while the message body is not well-formed for surrogateescape encoding. Sidney Markowitz supplied this patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
