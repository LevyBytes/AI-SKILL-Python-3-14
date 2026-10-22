# Python 3.8.0 alpha 1 / tools demos / python

[bpo-34989](https://bugs.python.org/issue?@action=redirect&bpo=34989): When figuring out the line number for a Python frame, python-gdb.py now copes with errors.

[bpo-32962](https://bugs.python.org/issue?@action=redirect&bpo=32962): While invoking `string()`, python-gdb now traps `UnicodeDecodeError` exceptions.

[bpo-32962](https://bugs.python.org/issue?@action=redirect&bpo=32962): On read_var(), python-gdb now traps ValueError; for instance when Python carries no debug symbols.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
