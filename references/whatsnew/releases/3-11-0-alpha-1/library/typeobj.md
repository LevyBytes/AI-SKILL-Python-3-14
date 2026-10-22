# Python 3.11.0 alpha 1 / library / typeobj

[bpo-43977](https://bugs.python.org/issue?@action=redirect&bpo=43977): The correct [`Py_TPFLAGS_MAPPING`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_MAPPING) and [`Py_TPFLAGS_SEQUENCE`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_SEQUENCE) flags are now applied to subclasses built before their parent gets registered as a [`collections.abc.Mapping`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Mapping) or [`collections.abc.Sequence`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Sequence).

[bpo-42972](https://bugs.python.org/issue?@action=redirect&bpo=42972): The _thread.RLock type now implements the GC protocol completely: a traverse function plus the [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC) flag were added. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
