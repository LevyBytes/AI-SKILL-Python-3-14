# Python 3.5.3 release candidate 1 / security / random

[bpo-27278](https://bugs.python.org/issue?@action=redirect&bpo=27278): Correct the os.urandom() implementation that uses getrandom() on Linux. Clamp the size to INT_MAX and keep looping until enough random bytes are gathered, rather than casting a Py_ssize_t straight to int.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
