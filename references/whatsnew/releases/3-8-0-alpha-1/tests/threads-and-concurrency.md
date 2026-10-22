# Python 3.8.0 alpha 1 / tests / threads and concurrency

[bpo-31731](https://bugs.python.org/issue?@action=redirect&bpo=31731): Resolve a race condition inside `check_interrupted_write()` of test_io: spawn the thread directly with the SIGALRM signal already blocked, instead of blocking that signal afterwards from within the thread. Earlier, the thread could receive the signal before it had been blocked.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
