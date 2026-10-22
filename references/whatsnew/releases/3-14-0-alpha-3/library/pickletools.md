# Python 3.14.0 alpha 3 / library / pickletools

[gh-126997](https://github.com/python/cpython/issues/126997): Correct STRING and GLOBAL opcode handling for non-ASCII arguments within [`pickletools`](https://docs.python.org/3.14/library/pickletools.html#module-pickletools). [`pickletools.dis()`](https://docs.python.org/3.14/library/pickletools.html#pickletools.dis) now renders non-ASCII bytes inside STRING, BINSTRING and SHORT_BINSTRING arguments in escaped form (`\xXX`).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
