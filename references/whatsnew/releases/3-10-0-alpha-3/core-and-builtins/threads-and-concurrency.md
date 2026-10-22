# Python 3.10.0 alpha 3 / core and builtins / threads and concurrency

[bpo-42296](https://bugs.python.org/issue?@action=redirect&bpo=42296): Under Windows, repair a signal-handling regression that blocked interrupting a program with CTRL+C. A signal handler may execute on a thread other than the Python thread, and in that situation the check determining whether the thread is allowed to process signals was incorrect.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
