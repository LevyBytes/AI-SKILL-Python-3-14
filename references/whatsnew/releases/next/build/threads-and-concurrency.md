# Python next / build / threads and concurrency

[gh-148260](https://github.com/python/cpython/issues/148260): Under Linux, where Python links against the musl C library, adopt a thread stack size no smaller than 1 MiB rather than the musl default of 128 kiB. Victor Stinner authored the change.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
