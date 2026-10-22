# Python 3.11.0 beta 1 / c api / functions and types

[gh-88279](https://github.com/python/cpython/issues/88279): These C functions are now deprecated: `PySys_SetArgv()`, `PySys_SetArgvEx()`, `PySys_SetPath()`. Victor Stinner authored the patch.

[gh-80527](https://github.com/python/cpython/issues/80527): Flag these functions as deprecated under [**PEP 623**](https://peps.python.org/pep-0623/): `PyUnicode_AS_DATA()`, `PyUnicode_AS_UNICODE()`, `PyUnicode_GET_DATA_SIZE()`, `PyUnicode_GET_SIZE()`. Victor Stinner authored the patch.

[bpo-40421](https://bugs.python.org/issue?@action=redirect&bpo=40421): A new `PyFrame_GetLasti` C-API function lets C code reach a frame object’s `f_lasti` attribute safely.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
