# Python 3.6.0 alpha 3 / security / random

[bpo-27278](https://bugs.python.org/issue?@action=redirect&bpo=27278): Corrected the os.urandom() implementation that relies on getrandom() under Linux. Cap the size at INT_MAX and keep looping until enough random bytes have been gathered, rather than casting a Py_ssize_t straight to int.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
