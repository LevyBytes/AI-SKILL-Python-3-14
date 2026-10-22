# Python 3.9.0 alpha 4 / c api / keep trashcan mechanism out limited c api needs access

[bpo-39542](https://bugs.python.org/issue?@action=redirect&bpo=39542): Keep the trashcan mechanism out of the limited C API: it needs access to PyTypeObject and PyThreadState structure fields, yet those structures stay opaque within the limited C API.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
