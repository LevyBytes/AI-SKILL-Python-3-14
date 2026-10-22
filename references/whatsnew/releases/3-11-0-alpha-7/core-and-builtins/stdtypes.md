# Python 3.11.0 alpha 7 / core and builtins / stdtypes

[bpo-46993](https://bugs.python.org/issue?@action=redirect&bpo=46993): Building a [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) from a [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) or [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple) is now 40% quicker. Kumar Aditya supplied the patch.

[bpo-47012](https://bugs.python.org/issue?@action=redirect&bpo=47012): Make iterating over [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) and [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) 30% quicker. Kumar Aditya supplied the patch.

[bpo-47009](https://bugs.python.org/issue?@action=redirect&bpo=47009): Sped up both [`list.append()`](https://docs.python.org/3.14/library/stdtypes.html#list.append) and list comprehensions by tuning for the frequent path where no resize occurs. Dennis Sweeney supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
