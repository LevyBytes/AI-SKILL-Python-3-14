# Python 3.8.0 alpha 1 / c api / tests and documentation

[bpo-35713](https://bugs.python.org/issue?@action=redirect&bpo=35713): The `PyByteArray_Init()` along with `PyByteArray_Fini()` functions are now gone. Doing nothing ever since Python 2.7.4 and Python 3.2.0, they sat outside the limited API (stable ABI) and lacked documentation.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
