# Python 3.9.0 alpha 2 / library / collections and iteration

[bpo-38688](https://bugs.python.org/issue?@action=redirect&bpo=38688): Using func:`shutil.copytree` to copy a directory tree into a subdirectory of itself produced an unending loop together with a RecursionError. The remedy drains an iterator and assembles the list of entries that need copying, so freshly created directories no longer cause the recursion. Bruno P. Kinoshita supplied the fix.

[bpo-38857](https://bugs.python.org/issue?@action=redirect&bpo=38857): A fix for AsyncMock covering return values whose type is awaitable. The same applies to side_effect iterable values that turn out to be awaitable, plus callables that yield an awaitable type. Previously such awaitables were awaited rather than handed back unchanged.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
