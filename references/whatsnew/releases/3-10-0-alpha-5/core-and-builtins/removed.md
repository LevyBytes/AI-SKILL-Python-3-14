# Python 3.10.0 alpha 5 / core and builtins / removed

[bpo-42990](https://bugs.python.org/issue?@action=redirect&bpo=42990): Reorganize the `PyEval_` family of functions.

  - A fresh function, `_PyEval_Vector`, lands to make calls into Python from C simpler.

  - `_PyEval_EvalCodeWithName` is removed

  - `PyEval_EvalCodeEx` stays in the API, though it sees no internal use

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
