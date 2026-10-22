# Python 3.11.0 alpha 1 / c api / functions

[bpo-45061](https://bugs.python.org/issue?@action=redirect&bpo=45061): Attach a deallocator to the [`bool`](https://docs.python.org/3.14/library/functions.html#bool) type so refcount bugs can be caught in C extensions that mistakenly invoke `Py_DECREF(Py_True);` or `Py_DECREF(Py_False);`. Victor Stinner contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
