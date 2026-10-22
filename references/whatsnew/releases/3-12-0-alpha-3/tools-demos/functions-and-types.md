# Python 3.12.0 alpha 3 / tools demos / functions and types

[gh-64490](https://github.com/python/cpython/issues/64490): Argument Clinic varargs bugfixes

  - Fix out-of-bounds error in `_PyArg_UnpackKeywordsWithVararg()`.

  - Fix incorrect check which allowed more than one varargs in clinic.py.

  - Fix miscalculation of `noptargs` in generated code.

  - Skip emitting `noptargs` whenever a vararg argument is present yet no optional argument exists.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
