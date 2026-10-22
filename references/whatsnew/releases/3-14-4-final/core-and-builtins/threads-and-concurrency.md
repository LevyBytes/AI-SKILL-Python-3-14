# Python 3.14.4 final / core and builtins / threads and concurrency

[gh-144438](https://github.com/python/cpython/issues/144438): Aligns the QSBR thread state array onto a 64-byte cache line boundary so as to prevent false sharing inside the [free-threaded build](https://docs.python.org/3.14/glossary.html#term-free-threaded-build).

[gh-144513](https://github.com/python/cpython/issues/144513): Corrects a possible deadlock arising from critical sections used amid stop-the-world pauses within the free-threaded build.

[gh-144446](https://github.com/python/cpython/issues/144446): Corrects data races inside the free-threaded build that appear when frame object attributes get read while a separate thread is executing the frame.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
