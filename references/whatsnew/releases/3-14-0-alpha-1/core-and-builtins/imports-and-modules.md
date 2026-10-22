# Python 3.14.0 alpha 1 / core and builtins / imports and modules

[gh-119560](https://github.com/python/cpython/issues/119560): A faulty assert from beta 1 is gone. That assert tripped whenever `PyState_FindModule()` ran inside an extension module's init function ahead of the module def being initialized.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
