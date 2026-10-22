# Python 3.12.0 alpha 2 / c api / memory and lifetimes

[gh-98978](https://github.com/python/cpython/issues/98978): Resolve a use-after-free affecting the `Py_SetPythonHome(NULL)`, `Py_SetProgramName(NULL)` and `_Py_SetProgramFullPath(NULL)` function calls. Benedikt Reinartz reported the issue. Victor Stinner authored the patch.

[gh-96853](https://github.com/python/cpython/issues/96853): `Py_InitializeEx` now invokes `PyConfig_Clear` properly once the interpreter has been set up (the earlier omission avoided a memory leak only because the wrapper function populates none of the dynamically allocated config fields)

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
