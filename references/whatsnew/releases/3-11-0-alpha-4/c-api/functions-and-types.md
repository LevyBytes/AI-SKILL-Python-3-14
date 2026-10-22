# Python 3.11.0 alpha 4 / c api / functions and types

[bpo-46007](https://bugs.python.org/issue?@action=redirect&bpo=46007): From the limited C API, the `PyUnicode_CHECK_INTERNED()` macro is now omitted. That macro could never function there, since it relied on internal structures absent from the limited C API. Victor Stinner contributed the fix.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
