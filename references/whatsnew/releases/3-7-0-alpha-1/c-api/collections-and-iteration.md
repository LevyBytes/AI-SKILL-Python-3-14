# Python 3.7.0 alpha 1 / c api / collections and iteration

[bpo-27867](https://bugs.python.org/issue?@action=redirect&bpo=27867): The PySlice_GetIndicesEx() function is now deprecated, becoming a macro when Py_LIMITED_API is either unset or set to a value in the range 0x03050400 up to (but excluding) 0x03060000, or alternatively 0x03060100 or above. The PySlice_Unpack() and PySlice_AdjustIndices() functions were added.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
