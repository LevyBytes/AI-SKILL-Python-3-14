# Python 3.9.0 alpha 1 / macos / threads and concurrency

[bpo-18049](https://bugs.python.org/issue?@action=redirect&bpo=18049): Raise the default per-thread stack size on macOS from 5MB up to 16MB so it lines up with the main thread's stack size. Doing so prevents crashes when threads recurse deeply.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
