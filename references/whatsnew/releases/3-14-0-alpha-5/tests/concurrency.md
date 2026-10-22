# Python 3.14.0 alpha 5 / tests / concurrency

[gh-128003](https://github.com/python/cpython/issues/128003): The regression test runner gained a `--parallel-threads=N` option that runs an individual test across several threads in parallel to surface concurrency bugs. Be aware that the bulk of the test suite has yet to be vetted for thread-safety or marked with `@thread_unsafe` where appropriate.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
