# Python 3.10.0 alpha 2 / library / functions and types

[bpo-41876](https://bugs.python.org/issue?@action=redirect&bpo=41876): The Tkinter font class repr makes use of the font name

[bpo-42157](https://bugs.python.org/issue?@action=redirect&bpo=42157): Dropped the `unicodedata.ucnhash_CAPI` attribute, which had been an internal PyCapsule object. Its associated private `_PyUnicode_Name_CAPI` structure migrated into the internal C API. Victor Stinner authored the patch.

[bpo-41052](https://bugs.python.org/issue?@action=redirect&bpo=41052): Using protocols 0 and 1 to pickle heap types written in C now raises an error rather than yielding bad data.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
