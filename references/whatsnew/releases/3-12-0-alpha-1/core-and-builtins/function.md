# Python 3.12.0 alpha 1 / core and builtins / function

[gh-97943](https://github.com/python/cpython/issues/97943): Bugfix: [`PyFunction_GetAnnotations()`](https://docs.python.org/3.14/c-api/function.html#c.PyFunction_GetAnnotations) ought to hand back a borrowed reference. It had been handing back a new reference.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
