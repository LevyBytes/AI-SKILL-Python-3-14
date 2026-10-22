# Python 3.14.0 beta 1 / library / mimetypes

[gh-132054](https://github.com/python/cpython/issues/132054): [`mimetypes`](https://docs.python.org/3.14/library/mimetypes.html#module-mimetypes) now recognizes the `application/yaml` mime type ([**RFC 9512**](https://datatracker.ietf.org/doc/html/rfc9512.html)). Patch by Sasha "Nelie" Chernykh and Hugo van Kemenade.

[gh-75223](https://github.com/python/cpython/issues/75223): Extensions lacking a dot are now deprecated in [`mimetypes.MimeTypes.add_type()`](https://docs.python.org/3.14/library/mimetypes.html#mimetypes.MimeTypes.add_type). Hugo van Kemenade wrote this patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
