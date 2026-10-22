# Python 3.6.0 alpha 1 / tools demos / python

[bpo-26799](https://bugs.python.org/issue?@action=redirect&bpo=26799): Repair python-gdb.py so that, rather than reading the C types one time when the Python code loads, it fetches the C types lazily. Those C types can shift if python-gdb.py loads ahead of the Python executable. Thomas Ilsche wrote the patch.

[bpo-25440](https://bugs.python.org/issue?@action=redirect&bpo=25440): Repair the output produced by python-config --extension-suffix.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
