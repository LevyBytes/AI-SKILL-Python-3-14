# Python 3.9.0 alpha 5 / tools demos / python

[bpo-36184](https://bugs.python.org/issue?@action=redirect&bpo=36184): Bring python-gdb.py to FreeBSD. To decide whether a frame is trying to grab the GIL, python-gdb.py now looks for the "take_gil" function name rather than "pthread_cond_timedwait", which is Linux-specific and may signal a condition other than the GIL.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
