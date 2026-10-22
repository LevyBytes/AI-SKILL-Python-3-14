# Python 3.10.0 beta 1 / library / ctypes

[bpo-32745](https://bugs.python.org/issue?@action=redirect&bpo=32745): Fixed a regression affecting ctypes' [`ctypes.c_wchar_p`](https://docs.python.org/3.14/library/ctypes.html#ctypes.c_wchar_p) type, where embedded null characters triggered a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError). Zackery Spytz supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
