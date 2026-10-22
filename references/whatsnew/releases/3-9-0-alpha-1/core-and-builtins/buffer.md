# Python 3.9.0 alpha 1 / core and builtins / buffer

[bpo-15913](https://bugs.python.org/issue?@action=redirect&bpo=15913): Joannah Nanjekye contributed an implementation of the [`PyBuffer_SizeFromFormat()`](https://docs.python.org/3.14/c-api/buffer.html#c.PyBuffer_SizeFromFormat) function (documented earlier but never implemented): it calls [`struct.calcsize()`](https://docs.python.org/3.14/library/struct.html#struct.calcsize).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
