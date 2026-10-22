# Python 3.5.2 release candidate 1 / tools demos / python

[bpo-26799](https://bugs.python.org/issue?@action=redirect&bpo=26799): Corrected python-gdb.py so that, instead of fetching C types just once when the Python code loads, it now obtains C types on demand. Those C types may differ if python-gdb.py loads ahead of the Python executable. Thomas Ilsche wrote this patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
