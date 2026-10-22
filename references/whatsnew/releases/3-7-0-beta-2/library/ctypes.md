# Python 3.7.0 beta 2 / library / ctypes

[bpo-32647](https://bugs.python.org/issue?@action=redirect&bpo=32647): The ctypes module formerly relied on indirect linking to reach dlopen. The shared extension now links explicitly with libdl on platforms that have dl.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
