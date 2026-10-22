# Python 3.10.0 alpha 1 / c api / dict

[bpo-40839](https://bugs.python.org/issue?@action=redirect&bpo=40839): For historical reasons, invoking [`PyDict_GetItem()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_GetItem) without holding the [GIL](https://docs.python.org/3.14/glossary.html#term-GIL) used to be permitted. That is permitted no longer.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
