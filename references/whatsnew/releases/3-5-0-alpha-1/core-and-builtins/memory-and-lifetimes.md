# Python 3.5.0 alpha 1 / core and builtins / memory and lifetimes

[bpo-22038](https://bugs.python.org/issue?@action=redirect&bpo=22038): When they are available, pyatomic.h now leans on stdatomic.h or GCC built-in functions for atomic memory access. Vitor de Lima and Gustavo Temple wrote the patch.

[bpo-21377](https://bugs.python.org/issue?@action=redirect&bpo=21377): When its first argument carries a reference count of 1, PyBytes_Concat() now attempts an in-place concatenation. Nikolaus Rath supplied the patch.

[bpo-23165](https://bugs.python.org/issue?@action=redirect&bpo=23165): Run the overflow checks ahead of allocating memory within the _Py_char2wchar function.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
