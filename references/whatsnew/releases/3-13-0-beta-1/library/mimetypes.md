# Python 3.13.0 beta 1 / library / mimetypes

[gh-66543](https://github.com/python/cpython/issues/66543): A new [`mimetypes.guess_file_type()`](https://docs.python.org/3.14/library/mimetypes.html#mimetypes.guess_file_type) function operates on a file path. Handing a file path rather than a URL to [`guess_type()`](https://docs.python.org/3.14/library/mimetypes.html#mimetypes.guess_type) is now [soft deprecated](https://docs.python.org/3.14/glossary.html#term-soft-deprecated).

[gh-101137](https://github.com/python/cpython/issues/101137): The mime type `text/x-rst` is now recognized by [`mimetypes`](https://docs.python.org/3.14/library/mimetypes.html#module-mimetypes).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
