# Python 3.14.1 final / core and builtins / traceback

[gh-63161](https://github.com/python/cpython/issues/63161): Accommodate a non-UTF-8 shebang plus comments inside Python source files whenever a non-UTF-8 encoding is declared. Catch a decoding error within comments for the default (UTF-8) encoding. Within a traceback, display the line plus position of the decoding error under the default encoding. Within a traceback, present the line holding the coding cookie whenever it clashes with the BOM.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
