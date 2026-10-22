# Python 3.8.0 alpha 4 / c api / datetime

[bpo-36025](https://bugs.python.org/issue?@action=redirect&bpo=36025): Repaired an inadvertent shift in the datetime C API whereby the [`PyDate_FromTimestamp()`](https://docs.python.org/3.14/c-api/datetime.html#c.PyDate_FromTimestamp) function read its arguments as one lone timestamp instead of an arguments tuple, which made existing code begin raising [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError). This backwards-incompatible regression had appeared solely in Python 3.8 alpha releases. Paul Ganssle wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
