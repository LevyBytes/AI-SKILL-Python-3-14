# Python 3.13.0 alpha 1 / c api / unicode

[gh-106320](https://github.com/python/cpython/issues/106320): The private `_PyUnicode_AsString()` alias for [`PyUnicode_AsUTF8()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_AsUTF8) is removed. It had lingered for backward compatibility with Python 3.0 - 3.2. Since Python 3.3 `PyUnicode_AsUTF8()` has been available. To stay compatible with Python 3.2 and earlier you can use the [`PyUnicode_AsUTF8String()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_AsUTF8String) function. Victor Stinner wrote the patch.

[gh-110289](https://github.com/python/cpython/issues/110289): New [`PyUnicode_EqualToUTF8AndSize()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_EqualToUTF8AndSize) and [`PyUnicode_EqualToUTF8()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_EqualToUTF8) functions are added.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
