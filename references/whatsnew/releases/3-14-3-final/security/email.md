# Python 3.14.3 final / security / email

[gh-143935](https://github.com/python/cpython/issues/143935): A bug in how comments were folded when an email message is flattened under a modern email policy has been fixed. A comment made of a very long run of non-foldable characters could force a line wrap that left out the mandatory leading space on the continuation line, which made the rest of the comment read as a fresh header field. Carefully crafted inputs could therefore inject headers.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
