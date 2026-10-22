# Python 3.5.0 alpha 1 / library / re

[bpo-22638](https://bugs.python.org/issue?@action=redirect&bpo=22638): SSLv3 is now turned off across the whole standard library. Building a SSLContext by hand still lets you re-enable it.

[bpo-22415](https://bugs.python.org/issue?@action=redirect&bpo=22415): The debugging output for the GROUPREF_EXISTS opcode within the re module was fixed. Trailing spaces in the debugging output were removed.

[bpo-22051](https://bugs.python.org/issue?@action=redirect&bpo=22051): Examples are no longer reloaded by turtledemo when it re-runs them. Setting up variables and the gui belongs in main(), which fires on each demo run rather than at import time.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
