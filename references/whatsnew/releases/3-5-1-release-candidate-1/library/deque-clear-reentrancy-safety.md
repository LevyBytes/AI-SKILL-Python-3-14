# Python 3.5.1 release candidate 1 / library / deque clear safer because deque drained before being cleared reduces

[bpo-25135](https://bugs.python.org/issue?@action=redirect&bpo=25135): deque_clear() is now safer because the deque is drained before being cleared, which reduces the chance of reentrancy trouble.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
