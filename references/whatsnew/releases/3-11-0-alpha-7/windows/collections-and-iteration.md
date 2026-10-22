# Python 3.11.0 alpha 7 / windows / collections and iteration

[bpo-46566](https://bugs.python.org/issue?@action=redirect&bpo=46566): The [Python install manager](https://docs.python.org/3.14/using/windows.html#launcher) is upgraded to accept a new `-V:company/tag` argument for complete [**PEP 514**](https://peps.python.org/pep-0514/) support and to recognize ARM64 installs. Although the `-64` suffix on arguments is now deprecated, it still picks any install that is not 32-bit. With `PYLAUNCHER_ALLOW_INSTALL` set, naming a version that is not installed will try fetching the requested version out of the Microsoft Store.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
