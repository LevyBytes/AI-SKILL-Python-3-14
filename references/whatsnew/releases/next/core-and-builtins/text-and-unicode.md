# Python next / core and builtins / text and unicode

[gh-151461](https://github.com/python/cpython/issues/151461): Adjust direct execution of files carrying invalid source encodings such that the actual codec lookup or decoding fault is surfaced rather than the catch-all `SyntaxError: encoding problem` message. Bartosz Sławecki authored the change.

[gh-151238](https://github.com/python/cpython/issues/151238): Repair a segfault while compiling a concatenated f-string or t-string should a fault arise as one of its components is processed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
