# Python 3.9.0 beta 1 / library / text and unicode

[bpo-40612](https://bugs.python.org/issue?@action=redirect&bpo=40612): Repair corner cases in how SyntaxError is formatted. When the offset is <= 0, the caret is suppressed. When the offset runs past the line length, the caret appears just beyond the final character.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
