# Python 3.5.2 release candidate 1 / core and builtins / collections and iteration

[bpo-26494](https://bugs.python.org/issue?@action=redirect&bpo=26494): A crash that struck when an already-exhausted iterator was iterated again is now resolved. The fix covers generic sequence iterators, the iterators for str, bytes, bytearray, list, tuple, set, frozenset, dict, OrderedDict, their matching views, and the os.scandir() iterator.

[bpo-22995](https://bugs.python.org/issue?@action=redirect&bpo=22995): Extension-type instances that carry state, are not subclasses of list or dict, and define none of the pickle-related hooks (__reduce__, __reduce_ex__, __getnewargs__, __getnewargs_ex__, or __getstate__) can no longer be pickled. This applies to memoryview as well.

[bpo-20041](https://bugs.python.org/issue?@action=redirect&bpo=20041): Resolved a TypeError that struck once frame.f_trace was set to None. Xavier de Gaye supplied the patch.

[bpo-26811](https://bugs.python.org/issue?@action=redirect&bpo=26811): gc.get_objects() will no longer hold a broken tuple carrying a NULL pointer.

[bpo-27243](https://bugs.python.org/issue?@action=redirect&bpo=27243): Revise the __aiter__ protocol so that the asynchronous iterator is handed back directly rather than returning an awaitable that resolves to one. Continuing to use the old style now emits a PendingDeprecationWarning.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
