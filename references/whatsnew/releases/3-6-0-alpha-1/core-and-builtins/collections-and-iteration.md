# Python 3.6.0 alpha 1 / core and builtins / collections and iteration

[bpo-22995](https://bugs.python.org/issue?@action=redirect&bpo=22995): Extension-type instances carrying state, when they aren't subclasses of list or dict and have implemented none of the pickle-related methods (__reduce__, __reduce_ex__, __getnewargs__, __getnewargs_ex__, or __getstate__), can no longer be pickled. memoryview is included in this.

[bpo-9232](https://bugs.python.org/issue?@action=redirect&bpo=9232): Adjust Python's grammar so a trailing comma is allowed in a function declaration's argument list. As an example, "def f(*, a = 3,): pass" has become legal. The patch came from Mark Dickinson.

[bpo-20041](https://bugs.python.org/issue?@action=redirect&bpo=20041): Repair the TypeError that arose when frame.f_trace was set to None. Xavier de Gaye wrote the patch.

[bpo-26811](https://bugs.python.org/issue?@action=redirect&bpo=26811): A broken tuple holding a NULL pointer no longer shows up in gc.get_objects().

[bpo-26802](https://bugs.python.org/issue?@action=redirect&bpo=26802): Speed up calls that rely solely on unpacking, such as `func(*tuple)` with no further positional argument and no keyword, by skipping the tuple copy. Joe Jevnik wrote the patch.

[bpo-25339](https://bugs.python.org/issue?@action=redirect&bpo=25339): When the error handler for stdin and stdout is being set, PYTHONIOENCODING now outranks the locale.

[bpo-26494](https://bugs.python.org/issue?@action=redirect&bpo=26494): Repair the crash that happened while iterating exhausting iterators. The classes touched by this include generic sequence iterators, the iterators belonging to str, bytes, bytearray, list, tuple, set, frozenset, dict, and OrderedDict, plus their matching views and the os.scandir() iterator.

[bpo-26136](https://bugs.python.org/issue?@action=redirect&bpo=26136): Promote the warning that fires when a generator raises StopIteration, moving it from PendingDeprecationWarning up to DeprecationWarning. Anish Shah wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
