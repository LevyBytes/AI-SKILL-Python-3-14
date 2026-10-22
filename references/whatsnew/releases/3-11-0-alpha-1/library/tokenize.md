# Python 3.11.0 alpha 1 / library / tokenize

[bpo-44667](https://bugs.python.org/issue?@action=redirect&bpo=44667): [`tokenize.tokenize()`](https://docs.python.org/3.14/library/tokenize.html#tokenize.tokenize) stops wrongly emitting a `NEWLINE` token when the source lacks a trailing newline character yet its final line is a comment, because the function already emits a `NL` token there. Pablo Galindo authored this patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
