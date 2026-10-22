# Python 3.14.0 beta 2 / library / multiprocessing

[gh-80334](https://github.com/python/cpython/issues/80334): [`multiprocessing.freeze_support()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.freeze_support) now looks for work across every "spawn" start method platform instead of restricting that check to Windows.

[gh-132124](https://github.com/python/cpython/issues/132124): On POSIX-compliant systems, `multiprocessing.util.get_temp_dir()` now disregards `TMPDIR` (and comparable environment variables) whenever the path length of `AF_UNIX` socket files runs past the platform-specific maximum while the [forkserver](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing-start-method-forkserver) start method is in use. Patch by Bénédikt Tran.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
