# Python 3.9.0 alpha 2 / core and builtins / multiprocessing

[bpo-38707](https://bugs.python.org/issue?@action=redirect&bpo=38707): When a child process is spawned through [`multiprocessing.Process`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.Process), `MainThread.native_id` now resets correctly rather than carrying over the parent's value.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
