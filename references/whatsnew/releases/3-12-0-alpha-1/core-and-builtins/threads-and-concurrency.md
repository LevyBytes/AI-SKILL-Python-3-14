# Python 3.12.0 alpha 1 / core and builtins / threads and concurrency

[gh-96387](https://github.com/python/cpython/issues/96387): During Python exit, a thread that still holds the GIL can occasionally wait endlessly for another thread (typically a daemon thread) that asked to drop the GIL but has already terminated. The fix for this race makes the thread requesting the GIL drop clear its request before it exits. Mingliang ZHAO found and analyzed the issue. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
