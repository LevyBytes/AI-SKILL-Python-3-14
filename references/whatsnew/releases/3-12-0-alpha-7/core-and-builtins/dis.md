# Python 3.12.0 alpha 7 / core and builtins / dis

[gh-89987](https://github.com/python/cpython/issues/89987): Trim how many inline [`CACHE`](https://docs.python.org/3.14/library/dis.html#opcode-CACHE) entries `BINARY_SUBSCR` carries.

[gh-100982](https://github.com/python/cpython/issues/100982): Substitute [`COMPARE_OP`](https://docs.python.org/3.14/library/dis.html#opcode-COMPARE_OP) for every appearance of `COMPARE_AND_BRANCH`.

[gh-90997](https://github.com/python/cpython/issues/90997): Cut down on the count of inline [`CACHE`](https://docs.python.org/3.14/library/dis.html#opcode-CACHE) entries consumed by [`LOAD_GLOBAL`](https://docs.python.org/3.14/library/dis.html#opcode-LOAD_GLOBAL).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
