# Python 3.6.1 release candidate 1 / c api / collections and iteration

[bpo-27867](https://bugs.python.org/issue?@action=redirect&bpo=27867): When Py_LIMITED_API is unset, set to a value between 0x03050400 and 0x03060000 (exclusive), or set to 0x03060100 or above, the PySlice_GetIndicesEx() function is swapped out for a macro.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
