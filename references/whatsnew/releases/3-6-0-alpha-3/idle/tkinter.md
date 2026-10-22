# Python 3.6.0 alpha 3 / idle / tkinter

[bpo-24137](https://bugs.python.org/issue?@action=redirect&bpo=24137): Run IDLE, test_idle, and htest with the tkinter default root turned off. Repaired code and tests that break under that restriction. Fixed the htests so they avoid spawning a second, redundant root and mainloop.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
