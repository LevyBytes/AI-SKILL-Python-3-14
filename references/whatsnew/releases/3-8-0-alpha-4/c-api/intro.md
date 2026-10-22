# Python 3.8.0 alpha 4 / c api / intro

[bpo-36641](https://bugs.python.org/issue?@action=redirect&bpo=36641): Both [PyDoc_VAR](https://docs.python.org/3.14/c-api/intro.html#c.PyDoc_VAR)(name) and [PyDoc_STRVAR](https://docs.python.org/3.14/c-api/intro.html#c.PyDoc_STRVAR)(name, str) now emit `static const char name[]` rather than `static char name[]`. Inada Naoki contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
