# Python 3.10.0 alpha 2 / c api / structures

[bpo-42015](https://bugs.python.org/issue?@action=redirect&bpo=42015): Closes a possible crash while freeing method objects in cases where a dynamically allocated [`PyMethodDef`](https://docs.python.org/3.14/c-api/structures.html#c.PyMethodDef)'s lifetime hangs off the `self` argument handed to a [`PyCFunction`](https://docs.python.org/3.14/c-api/structures.html#c.PyCFunction).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
