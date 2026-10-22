# Python 3.13.0 alpha 3 / windows / multiprocessing

[gh-113009](https://github.com/python/cpython/issues/113009): [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing): A Windows race in `Process.terminate()` is repaired: the `returncode` attribute is no longer set so that `Process.wait()` always invokes `WaitForSingleObject()`. Formerly the process could keep running after `TerminateProcess()` even though `GetExitCodeProcess()` was not `STILL_ACTIVE`. Victor Stinner authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
