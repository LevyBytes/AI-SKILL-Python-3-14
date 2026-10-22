# Python 3.6.2 release candidate 1 / library / memory and lifetimes

[bpo-30243](https://bugs.python.org/issue?@action=redirect&bpo=30243): Dropped the __init__ methods belonging to _json's scanner and encoder. Misuse of them risked crashes or memory leaks. The scanner and encoder objects now finish their entire setup inside the __new__ methods.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
