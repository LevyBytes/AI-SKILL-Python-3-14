# Python 3.9.0 alpha 6 / c api / number

[bpo-40170](https://bugs.python.org/issue?@action=redirect&bpo=40170): Always present [`PyIndex_Check()`](https://docs.python.org/3.14/c-api/number.html#c.PyIndex_Check) as an opaque function so implementation details stay hidden: the `PyIndex_Check()` macro is dropped. That macro had been reaching straight into the [`PyTypeObject.tp_as_number`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_as_number) member.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
