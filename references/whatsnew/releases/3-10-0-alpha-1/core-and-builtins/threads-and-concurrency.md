# Python 3.10.0 alpha 1 / core and builtins / threads and concurrency

[bpo-40826](https://bugs.python.org/issue?@action=redirect&bpo=40826): Corrected GIL usage inside `PyOS_Readline()`: the GIL is locked to raise an exception, and the Python thread state is forwarded while testing for a pending signal.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
