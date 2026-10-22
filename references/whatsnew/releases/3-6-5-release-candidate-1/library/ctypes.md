# Python 3.6.5 release candidate 1 / library / ctypes

[bpo-30353](https://bugs.python.org/issue?@action=redirect&bpo=30353): Repair ctypes pass-by-value for structs under 64-bit Cygwin/MinGW.

[bpo-32647](https://bugs.python.org/issue?@action=redirect&bpo=32647): Previously the ctypes module relied on indirect linking to reach dlopen. On platforms providing dl, its shared extension is now linked against libdl explicitly.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
