# Python 3.10.0 alpha 3 / c api / functions and types

[bpo-40170](https://bugs.python.org/issue?@action=redirect&bpo=40170): No longer does the `Py_TRASHCAN_BEGIN` macro reach into PyTypeObject attributes; instead it can obtain the condition through the freshly added private `_PyTrash_cond()` function, which conceals the implementation specifics.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
