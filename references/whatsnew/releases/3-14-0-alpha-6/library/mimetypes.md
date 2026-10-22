# Python 3.14.0 alpha 6 / library / mimetypes

[gh-128703](https://github.com/python/cpython/issues/128703): Repairs [`mimetypes.guess_type()`](https://docs.python.org/3.14/library/mimetypes.html#mimetypes.guess_type) so it falls back on the default mapping for an empty `Content-Type` held in the registry.

[gh-93096](https://github.com/python/cpython/issues/93096): The command line for [`mimetypes`](https://docs.python.org/3.14/library/mimetypes.html#module-mimetypes) is now documented. On a failure it now leaves with `1` rather than `0`, and bad command-line parameters yield `2` instead of `1`. On top of that, errors go to stderr rather than stdout and their wording was trimmed. Oleg Iarygin and Hugo van Kemenade supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
