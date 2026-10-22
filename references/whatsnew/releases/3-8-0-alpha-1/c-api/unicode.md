# Python 3.8.0 alpha 1 / c api / unicode

[bpo-35322](https://bugs.python.org/issue?@action=redirect&bpo=35322): Repair the memory leak in [`PyUnicode_EncodeLocale()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_EncodeLocale) plus [`PyUnicode_EncodeFSDefault()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_EncodeFSDefault) during error handling.

[bpo-30863](https://bugs.python.org/issue?@action=redirect&bpo=30863): Neither [`PyUnicode_AsWideChar()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_AsWideChar) nor [`PyUnicode_AsWideCharString()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_AsWideCharString) keeps a cached `wchar_t*` form of string objects any longer.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
