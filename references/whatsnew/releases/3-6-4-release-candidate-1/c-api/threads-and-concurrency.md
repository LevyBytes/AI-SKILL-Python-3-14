# Python 3.6.4 release candidate 1 / c api / threads and concurrency

[bpo-20891](https://bugs.python.org/issue?@action=redirect&bpo=20891): Repair PyGILState_Ensure(). Whenever PyGILState_Ensure() runs in a non-Python thread ahead of PyEval_InitThreads(), defer the PyEval_InitThreads() call until after PyThreadState_New() runs, which avoids a crash.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
