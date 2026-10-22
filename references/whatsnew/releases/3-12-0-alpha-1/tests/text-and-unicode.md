# Python 3.12.0 alpha 1 / tests / text and unicode

[gh-95027](https://github.com/python/cpython/issues/95027): Under Windows, running the Python test suite with `-jN` now adopts the ANSI code page as the stdout temporary file's encoding, instead of UTF-8 which could produce decoding errors. Victor Stinner authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
