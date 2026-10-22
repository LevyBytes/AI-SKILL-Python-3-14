# Python 3.10.0 beta 1 / core and builtins / typeobj

[bpo-43977](https://bugs.python.org/issue?@action=redirect&bpo=43977): During pattern matching, rely on [`tp_flags`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_flags) on the class object to decide whether the subject counts as a sequence or a mapping. This sidesteps importing [`collections.abc`](https://docs.python.org/3.14/library/collections.abc.html#module-collections.abc) during pattern matching.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
