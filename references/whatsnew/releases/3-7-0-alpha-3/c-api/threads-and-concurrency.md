# Python 3.7.0 alpha 3 / c api / threads and concurrency

[bpo-20891](https://bugs.python.org/issue?@action=redirect&bpo=20891): Repair PyGILState_Ensure(). Whenever PyGILState_Ensure() runs on a non-Python thread ahead of PyEval_InitThreads(), invoke PyEval_InitThreads() only once PyThreadState_New() has run, to avoid a crash.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
