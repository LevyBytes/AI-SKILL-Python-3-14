# Python 3.13.0 alpha 6 / library / mimetypes

[gh-66543](https://github.com/python/cpython/issues/66543): Teach [`mimetypes.guess_type()`](https://docs.python.org/3.14/library/mimetypes.html#mimetypes.guess_type) to parse, correctly, URLs that carry only a host name, URLs that include a fragment or query, plus Windows filenames holding nothing but a UNC sharepoint. Grew out of a patch from Dong-hee Na.

[gh-97901](https://github.com/python/cpython/issues/97901): The `text/rtf` mime type is now recognized by [`mimetypes`](https://docs.python.org/3.14/library/mimetypes.html#module-mimetypes).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
