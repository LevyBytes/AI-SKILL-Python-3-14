# Python 3.9.0 alpha 3 / core and builtins / object

[bpo-38588](https://bugs.python.org/issue?@action=redirect&bpo=38588): Potential crashes within dict and list during calls to [`PyObject_RichCompareBool()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_RichCompareBool) were addressed.

[bpo-38610](https://bugs.python.org/issue?@action=redirect&bpo=38610): Several list methods could crash; this was avoided by retaining strong references to list elements across calls to [`PyObject_RichCompareBool()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_RichCompareBool).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
