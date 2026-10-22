# Python 3.5.0 release candidate 3 / library / collections and iteration

[bpo-24635](https://bugs.python.org/issue?@action=redirect&bpo=24635): Squashed a typing.py bug where isinstance([], typing.Iterable) came back True the first time but False on every later call.

[bpo-24989](https://bugs.python.org/issue?@action=redirect&bpo=24989): Fixed a buffer overread in BytesIO.readline() that happened when a position was set past size. The fix is based on a patch from John Leitch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
