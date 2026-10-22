# Python 3.5.3 release candidate 1 / core and builtins / debug

[bpo-28648](https://bugs.python.org/issue?@action=redirect&bpo=28648): Repair a crash in Py_DecodeLocale() within a debug build on Mac OS X while decoding astral characters. Xiang Zhang supplied the patch.

[bpo-28426](https://bugs.python.org/issue?@action=redirect&bpo=28426): Repair a potential crash inside PyUnicode_AsDecodedObject() in a debug build.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
