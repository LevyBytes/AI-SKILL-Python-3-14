# Python 3.12.0 alpha 3 / core and builtins / compiler and parser

[gh-90994](https://github.com/python/cpython/issues/90994): Sharpen the diagnostics emitted on a syntax error involving call arguments. Three situations now get handled: - A named argument receives no value, eg `foo(a=)`. - A star argument is given a value, eg `foo(*args=[0])`. - A double-star keyword argument is assigned a value, eg `foo(**kwarg={'a': 0})`.

[gh-99708](https://github.com/python/cpython/issues/99708): Resolve a defect in which the compiler crashed on an if expression whose body block was empty.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
