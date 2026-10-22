# Python 3.12.0 alpha 1 / library / codeop

[gh-96052](https://github.com/python/cpython/issues/96052): Compiler warning handling (SyntaxWarning plus DeprecationWarning) inside [`codeop.compile_command()`](https://docs.python.org/3.14/library/codeop.html#codeop.compile_command) during incomplete-input checks is fixed. Earlier it produced warnings and threw a SyntaxError. The function now consistently hands back `None` for incomplete input and emits no warnings at all.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
