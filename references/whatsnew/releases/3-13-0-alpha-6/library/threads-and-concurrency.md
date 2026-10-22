# Python 3.13.0 alpha 6 / library / threads and concurrency

[gh-114271](https://github.com/python/cpython/issues/114271): Repair a race within `threading.Thread.join()`.

`threading._MainThread` now stands for the main thread of the main interpreter at all times.

`PyThreadState.on_delete` along with `PyThreadState.on_delete_data` have been dropped.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
