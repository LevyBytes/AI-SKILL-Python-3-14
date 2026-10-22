# Python 3.8.0 alpha 2 / core and builtins / fresh internal py addpendingcall added acts relative interpreter you hand

[bpo-33608](https://bugs.python.org/issue?@action=redirect&bpo=33608): A fresh internal _Py_AddPendingCall() was added that acts relative to the interpreter you hand it. With it we can reuse the present implementation to request that one interpreter perform work the current interpreter cannot, such as decref-ing an object owned by the other interpreter. The pre-existing Py_AddPendingCall() acts only relative to the main interpreter.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
