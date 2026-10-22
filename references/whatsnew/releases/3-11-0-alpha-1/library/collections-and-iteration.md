# Python 3.11.0 alpha 1 / library / collections and iteration

[bpo-44566](https://bugs.python.org/issue?@action=redirect&bpo=44566): handle StopIteration subclass raised from @contextlib.contextmanager generator

[bpo-27827](https://bugs.python.org/issue?@action=redirect&bpo=27827): `pathlib.PureWindowsPath.is_reserved()` now recognizes a wider set of reserved filenames, among them ones bearing trailing spaces or colons.

[bpo-41322](https://bugs.python.org/issue?@action=redirect&bpo=41322): Introduced a `DeprecationWarning` covering tests and async tests whose return value is `!=None` (which can signal a badly authored test, such as one accidentally written as a generator function).

[bpo-44704](https://bugs.python.org/issue?@action=redirect&bpo=44704): The `collections.abc.Set._hash()` implementation now lines up with that of `frozenset.__hash__()`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
