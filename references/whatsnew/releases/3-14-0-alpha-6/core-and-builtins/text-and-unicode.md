# Python 3.14.0 alpha 6 / core and builtins / text and unicode

[bpo-44369](https://bugs.python.org/issue?@action=redirect&bpo=44369): Syntax errors for strings that are closed incorrectly have been improved. Pablo Galindo supplied the patch.

[gh-130804](https://github.com/python/cpython/issues/130804): The new REPL on Windows now supports unicode characters correctly.

[gh-130618](https://github.com/python/cpython/issues/130618): A defect that raised `UnicodeDecodeError` or `SystemError` when f-strings contained `lambda` expressions holding non-ASCII characters has been corrected. Pablo Galindo supplied the patch.

[gh-130415](https://github.com/python/cpython/issues/130415): The JIT is now better at optimizing strings when they appear in boolean contexts.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
