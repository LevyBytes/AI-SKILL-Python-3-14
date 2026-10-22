# Python 3.11.0 alpha 2 / c api / weakref

[bpo-35134](https://bugs.python.org/issue?@action=redirect&bpo=35134): Drop [`PyWeakref_GET_OBJECT()`](https://docs.python.org/3.14/c-api/weakref.html#c.PyWeakref_GET_OBJECT) from the limited C API. Because the `PyWeakReference` structure stays opaque under the limited C API, it never functioned there.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
