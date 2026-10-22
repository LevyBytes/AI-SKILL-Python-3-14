# Python 3.12.0 alpha 4 / library / ctypes

[bpo-36880](https://bugs.python.org/issue?@action=redirect&bpo=36880): Repair a reference-counting bug that could crash when a [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes) callback whose return type is [`py_object`](https://docs.python.org/3.14/library/ctypes.html#ctypes.py_object) returns `None`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
