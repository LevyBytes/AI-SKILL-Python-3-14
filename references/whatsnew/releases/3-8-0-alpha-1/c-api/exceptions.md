# Python 3.8.0 alpha 1 / c api / exceptions

[bpo-23927](https://bugs.python.org/issue?@action=redirect&bpo=23927): Repaired [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError) inside [`PyArg_ParseTupleAndKeywords()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTupleAndKeywords) whenever the `w*` format unit applies to an optional parameter.

[bpo-33818](https://bugs.python.org/issue?@action=redirect&bpo=33818): From now on [`PyExceptionClass_Name()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyExceptionClass_Name) yields `const char *` rather than `char *`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
