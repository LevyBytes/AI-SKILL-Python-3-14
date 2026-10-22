# Python 3.11.0 beta 1 / core and builtins / collections and iteration

[bpo-26579](https://bugs.python.org/issue?@action=redirect&bpo=26579): A new `object.__getstate__` was added, supplying the `__getstate__()` method's default implementation.

A range of builtin types is covered here: bytearray, set, frozenset, collections.OrderedDict, collections.deque, weakref.WeakSet, plus datetime.tzinfo. For instances belonging to subclasses of those types, copying and pickling now carries along instance attributes that were implemented through slots.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
