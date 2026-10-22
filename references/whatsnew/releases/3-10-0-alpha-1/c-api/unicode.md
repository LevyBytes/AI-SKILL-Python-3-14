# Python 3.10.0 alpha 1 / c api / unicode

[bpo-41692](https://bugs.python.org/issue?@action=redirect&bpo=41692): The `PyUnicode_InternImmortal()` function is deprecated from now on and is slated for removal in Python 3.12; reach for [`PyUnicode_InternInPlace()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_InternInPlace) instead. Victor Stinner authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
