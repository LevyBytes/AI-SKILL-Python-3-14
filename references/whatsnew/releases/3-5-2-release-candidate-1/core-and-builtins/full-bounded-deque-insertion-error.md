# Python 3.5.2 release candidate 1 / core and builtins / bounded deques already their maximum length deque insert used produce

[bpo-26194](https://bugs.python.org/issue?@action=redirect&bpo=26194): For bounded deques already at their maximum length, Deque.insert() used to produce strange behavior. An IndexError is now raised whenever an insertion into a full deque is attempted.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
