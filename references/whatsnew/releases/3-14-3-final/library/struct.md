# Python 3.14.3 final / library / struct

[gh-78724](https://github.com/python/cpython/issues/78724): Calling methods on a half-initialized [`Struct`](https://docs.python.org/3.14/library/struct.html#struct.Struct) object — say one built via `Struct.__new__(Struct)` — now raises [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError). Sergey B Kirpichev supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
