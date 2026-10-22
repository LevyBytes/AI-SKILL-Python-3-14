# Python 3.6.0 beta 1 / library / os

[bpo-27776](https://bugs.python.org/issue?@action=redirect&bpo=27776): To raise security, the [`os.urandom()`](https://docs.python.org/3.14/library/os.html#os.urandom) function will now wait on Linux 3.17 and later until the system urandom entropy pool finishes initializing. [**PEP 524**](https://peps.python.org/pep-0524/) covers this change.

[bpo-27778](https://bugs.python.org/issue?@action=redirect&bpo=27778): A fresh [`os.getrandom()`](https://docs.python.org/3.14/library/os.html#os.getrandom) function surfaces the Linux `getrandom()` syscall. [**PEP 524**](https://peps.python.org/pep-0524/) covers this change.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
