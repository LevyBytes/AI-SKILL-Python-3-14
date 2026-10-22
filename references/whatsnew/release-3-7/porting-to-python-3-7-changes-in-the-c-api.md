# What's New In Python 3.7 / Porting to Python 3.7 / Changes in the C API

### Changes in the C API

The [`PySlice_GetIndicesEx()`](https://docs.python.org/3.14/c-api/slice.html#c.PySlice_GetIndicesEx) function counts as unsafe where sequences can be resized. Whenever the slice indices are not [`int`](https://docs.python.org/3.14/library/functions.html#int) instances but rather objects supplying the `__index__()` method, the sequence may be resized once its length has been handed to `PySlice_GetIndicesEx()`. That can result in indices being returned outside the sequence's length. To steer clear of such trouble, lean on the new functions [`PySlice_Unpack()`](https://docs.python.org/3.14/c-api/slice.html#c.PySlice_Unpack) and [`PySlice_AdjustIndices()`](https://docs.python.org/3.14/c-api/slice.html#c.PySlice_AdjustIndices). Serhiy Storchaka contributed this through [bpo-27867](https://bugs.python.org/issue?@action=redirect&bpo=27867).

[Subject index](INDEX.md) · [Previous source section](changes-in-the-python-api.md) · [Next source section](bytecode-migration-changes.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](porting-to-python-3-7.md)
