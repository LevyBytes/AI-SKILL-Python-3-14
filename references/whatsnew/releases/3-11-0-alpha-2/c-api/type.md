# Python 3.11.0 alpha 2 / c api / type

[bpo-29103](https://bugs.python.org/issue?@action=redirect&bpo=29103): [`PyType_FromSpec*`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromModuleAndSpec) now duplicates the class name from the spec into a buffer the class owns, leaving the original free to be deallocated safely. Petr Viktorin contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
