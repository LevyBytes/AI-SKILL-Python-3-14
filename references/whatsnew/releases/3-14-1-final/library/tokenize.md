# Python 3.14.1 final / library / tokenize

[gh-63161](https://github.com/python/cpython/issues/63161): Corrects [`tokenize.detect_encoding()`](https://docs.python.org/3.14/library/tokenize.html#tokenize.detect_encoding). A non-UTF-8 shebang and comments are supported when a non-UTF-8 encoding is declared. Decoding errors for a non-UTF-8 encoding are caught. Null bytes within source code are caught.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
