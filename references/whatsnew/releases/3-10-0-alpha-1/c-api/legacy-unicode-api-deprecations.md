# Python 3.10.0 alpha 1 / c api / legacy unicode api deprecations

[bpo-36346](https://bugs.python.org/issue?@action=redirect&bpo=36346): Flag `Py_UNICODE_COPY`, `Py_UNICODE_FILL`, `PyUnicode_WSTR_LENGTH`, `PyUnicode_FromUnicode`, `PyUnicode_AsUnicode`, and `PyUnicode_AsUnicodeAndSize` as deprecated within C. Strip out `Py_UNICODE_MATCH`, which had been deprecated and broken ever since Python 3.3.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
