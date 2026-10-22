# Python 3.9.0 alpha 4 / c api / files and paths

[bpo-35081](https://bugs.python.org/issue?@action=redirect&bpo=35081): Relocate the `bytes_methods.h` header file into the internal C API as `pycore_bytes_methods.h`: it carries only private symbols (prefixed by `_Py`), apart from the `PyDoc_STRVAR_shared()` macro.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
