# What's New In Python 3.7 / Deprecated functions and types of the C API

### Deprecated functions and types of the C API

The [`PySlice_GetIndicesEx()`](https://docs.python.org/3.14/c-api/slice.html#c.PySlice_GetIndicesEx) function is now deprecated and gets swapped for a macro whenever `Py_LIMITED_API` is left unset, or holds a value falling between `0x03050400` and `0x03060000` (exclusive of the upper bound), or equals `0x03060100` or anything greater. (Contributed by Serhiy Storchaka in [bpo-27867](https://bugs.python.org/issue?@action=redirect&bpo=27867).)

The [`PyOS_AfterFork()`](https://docs.python.org/3.14/c-api/sys.html#c.PyOS_AfterFork) function is now deprecated. Use [`PyOS_BeforeFork()`](https://docs.python.org/3.14/c-api/sys.html#c.PyOS_BeforeFork), [`PyOS_AfterFork_Parent()`](https://docs.python.org/3.14/c-api/sys.html#c.PyOS_AfterFork_Parent) or [`PyOS_AfterFork_Child()`](https://docs.python.org/3.14/c-api/sys.html#c.PyOS_AfterFork_Child) instead. (Contributed by Antoine Pitrou in [bpo-16500](https://bugs.python.org/issue?@action=redirect&bpo=16500).)

[Subject index](INDEX.md) · [Previous source section](wave.md) · [Next source section](platform-support-removals.md) · [Release/subject declaration](summary-release-highlights.md)
