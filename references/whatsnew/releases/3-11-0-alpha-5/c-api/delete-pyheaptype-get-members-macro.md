# Python 3.11.0 alpha 5 / c api / delete pyheaptype get members macro

[bpo-40170](https://bugs.python.org/issue?@action=redirect&bpo=40170): Delete the `PyHeapType_GET_MEMBERS()` macro. Its exposure in the public C API was a mistake, since only Python itself should use it. Reach for the `PyTypeObject.tp_members` member instead. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
