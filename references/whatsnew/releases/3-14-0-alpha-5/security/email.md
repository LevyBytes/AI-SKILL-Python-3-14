# Python 3.14.0 alpha 5 / security / email

[gh-80222](https://github.com/python/cpython/issues/80222): A bug in folding quoted strings while flattening an email message under a modern email policy has been fixed. Earlier, when a quoted string was folded so that it ran across more than a single line, the enclosing quotes and any internal escapes were dropped. In theory this could be exploited to spoof header lines through a carefully built quoted string if the rendered email was then sent or parsed again.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
