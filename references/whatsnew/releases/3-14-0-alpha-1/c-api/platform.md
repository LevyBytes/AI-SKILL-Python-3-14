# Python 3.14.0 alpha 1 / c api / platform

[gh-87135](https://github.com/python/cpython/issues/87135): When a thread tries to take the GIL once runtime finalization has already started elsewhere, that thread will now block forever instead of being terminated. This guards against crashes or memory corruption that could otherwise arise from killing a thread whose code was never built to tolerate termination. Usually the resulting block does no harm, because the process is about to exit regardless.

The `PyThread_exit_thread` function has now been marked deprecated. Because its semantics differ from one platform to the next, the only situation where it is truly safe is the rare one where every routine throughout the whole call stack was written to cope with the platform's particular termination mechanism. Anyone relying on it should rework their design so that terminating a thread is no longer required. For the rare scenario where killing a thread is both necessary and provably safe, callers can switch to platform-specific entry points such as `pthread_exit` (POSIX) or `_endthreadex` (Windows) called directly.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
