# Python 3.8.0 alpha 1 / core and builtins / collections and iteration

[bpo-34320](https://bugs.python.org/issue?@action=redirect&bpo=34320): Correct `dict(od)` so it preserves the iteration order of an OrderedDict, which it previously failed to copy.

[bpo-34151](https://bugs.python.org/issue?@action=redirect&bpo=34151): The performance of list concatenation, repetition and slicing has been improved a little. Patch by Sergey Fedoseev.

[bpo-34751](https://bugs.python.org/issue?@action=redirect&bpo=34751): Tuple hashing now builds on xxHash, which yields better collision behavior across cases that were formerly pathological. On 64-bit platforms it also makes tuple hashes better overall. Patch by Jeroen Demeyer with substantial contributions by Tim Peters.

[bpo-34377](https://bugs.python.org/issue?@action=redirect&bpo=34377): Revise the valgrind suppression list so it references `_PyObject_Free`/`_PyObject_Realloc` rather than `PyObject_Free`/`PyObject_Realloc`.

[bpo-33234](https://bugs.python.org/issue?@action=redirect&bpo=33234): The list constructor now pre-sizes itself and avoids over-allocating whenever the input length is already known.

[bpo-33803](https://bugs.python.org/issue?@action=redirect&bpo=33803): Resolve a crash in hamt.c that was triggered by enabling GC tracking on an object whose fields had not all been set to NULL.

[bpo-32889](https://bugs.python.org/issue?@action=redirect&bpo=32889): Refreshed the Valgrind suppression list to reflect that `Py_ADDRESS_IN_RANG` was renamed to `address_in_range`.

[bpo-32836](https://bugs.python.org/issue?@action=redirect&bpo=32836): Stop relying on temporary variables when handling list, dict, and set comprehensions

[bpo-32117](https://bugs.python.org/issue?@action=redirect&bpo=32117): Yield and return statements now accept iterable unpacking without surrounding parentheses, for instance `yield 1, 2, 3, *rest`. The change came from David Cuthbert, with extra tests contributed by Jordan Chapman.

[bpo-35814](https://bugs.python.org/issue?@action=redirect&bpo=35814): Permit the same right hand side expressions in annotated assignments that normal ones allow. Specifically, `x: Tuple[int, int] = 1, 2` (with no parentheses on the right) is now permitted.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
