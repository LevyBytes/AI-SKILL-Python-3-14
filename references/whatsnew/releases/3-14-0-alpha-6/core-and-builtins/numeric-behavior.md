# Python 3.14.0 alpha 6 / core and builtins / numeric behavior

[gh-91079](https://github.com/python/cpython/issues/91079): C stack overflow protection now looks at how much stack has been consumed instead of relying on a counter. Many cases can therefore recurse more deeply while staying safe.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
