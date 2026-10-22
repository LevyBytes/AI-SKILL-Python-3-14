# Python 3.14.0 beta 1 / core and builtins / text and unicode

[gh-131878](https://github.com/python/cpython/issues/131878): On Windows, the new REPL's support for unicode characters made of two or more codepoints is fixed.

[gh-129958](https://github.com/python/cpython/issues/129958): A bug is fixed that inconsistently permitted newlines within format specifiers of single-quoted f-strings. Pablo Galindo wrote this patch.

[gh-132661](https://github.com/python/cpython/issues/132661): [**PEP 750**](https://peps.python.org/pep-0750/) (Template Strings) is implemented. New t-string syntax is added, along with the new internal `string.templatelib.Template` and `string.templatelib.Interpolation` types.

[gh-131798](https://github.com/python/cpython/issues/131798): By setting the return type to string, the JIT can drop unicode guards after `_BINARY_OP_SUBSCR_STR_INT`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
