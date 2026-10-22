# Python 3.6.0 alpha 1 / core and builtins / threads and concurrency

[bpo-25274](https://bugs.python.org/issue?@action=redirect&bpo=25274): sys.setrecursionlimit() now raises a RecursionError when the new recursion limit sits too low relative to the current recursion depth. The "lower-water mark" formula is also adjusted to stay monotonic. This mark governs the moment the overflowed flag on the thread state gets reset.

[bpo-26154](https://bugs.python.org/issue?@action=redirect&bpo=26154): Introduce a private _PyThreadState_UncheckedGet() function that fetches the current Python thread state but, unlike before, won't raise a fatal error when the result is NULL. Reach for this new function rather than touching the _PyThreadState_Current variable directly. That variable has been hidden since Python 3.5.1 so the precise implementation of atomic C types stays concealed, sidestepping compiler issues.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
