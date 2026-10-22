# Python 3.9.0 alpha 5 / core and builtins / unicode

[bpo-39087](https://bugs.python.org/issue?@action=redirect&bpo=39087): Give [`PyUnicode_AsUTF8()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_AsUTF8) and [`PyUnicode_AsUTF8AndSize()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_AsUTF8AndSize) a small speedup for the case where they must populate the internal UTF-8 cache.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
