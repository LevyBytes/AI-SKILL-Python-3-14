# Python 3.5.4 release candidate 1 / library / memory and lifetimes

[bpo-30243](https://bugs.python.org/issue?@action=redirect&bpo=30243): Dropped the __init__ methods belonging to _json's scanner and encoder. Misuse of them could trigger memory leaks or crashes. Scanner and encoder objects are now fully initialized within the __new__ methods.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
