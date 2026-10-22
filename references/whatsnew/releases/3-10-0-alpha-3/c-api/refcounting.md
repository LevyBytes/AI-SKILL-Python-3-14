# Python 3.10.0 alpha 3 / c api / refcounting

[bpo-42262](https://bugs.python.org/issue?@action=redirect&bpo=42262): Introduced the [`Py_NewRef()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_NewRef) and [`Py_XNewRef()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_XNewRef) functions, which bump an object's reference count and hand the object back. Victor Stinner provided this patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
