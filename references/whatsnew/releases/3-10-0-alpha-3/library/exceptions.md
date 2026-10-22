# Python 3.10.0 alpha 3 / library / exceptions

[bpo-17735](https://bugs.python.org/issue?@action=redirect&bpo=17735): `inspect.findsource()` now raises [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) instead of [`IndexError`](https://docs.python.org/3.14/library/exceptions.html#IndexError) once a code object's `co_lineno` exceeds the file length. Such a mismatch may arise, say, after a file is edited subsequent to import. Irit Katriel sent the PR.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
