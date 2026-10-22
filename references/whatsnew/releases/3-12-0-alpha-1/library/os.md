# Python 3.12.0 alpha 1 / library / os

[gh-93899](https://github.com/python/cpython/issues/93899): The existence check covering [`os.EFD_CLOEXEC`](https://docs.python.org/3.14/library/os.html#os.EFD_CLOEXEC), [`os.EFD_NONBLOCK`](https://docs.python.org/3.14/library/os.html#os.EFD_NONBLOCK), and [`os.EFD_SEMAPHORE`](https://docs.python.org/3.14/library/os.html#os.EFD_SEMAPHORE) is fixed for older kernels that lack these flags. Kumar Aditya wrote the patch.

[gh-95023](https://github.com/python/cpython/issues/95023): Implement [`os.setns()`](https://docs.python.org/3.14/library/os.html#os.setns) and [`os.unshare()`](https://docs.python.org/3.14/library/os.html#os.unshare) on Linux. Noam Cohen wrote the patch.

[gh-98393](https://github.com/python/cpython/issues/98393): The [`os`](https://docs.python.org/3.14/library/os.html#module-os) module stops accepting bytes-like paths such as [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) and [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) types: for bytes strings only the precise [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) type is taken. Victor Stinner wrote the patch.

[gh-87901](https://github.com/python/cpython/issues/87901): Dropped the `encoding` argument from [`os.popen()`](https://docs.python.org/3.14/library/os.html#os.popen) that had landed in 3.11b1.

[gh-93312](https://github.com/python/cpython/issues/93312): Introduce the [`os.PIDFD_NONBLOCK`](https://docs.python.org/3.14/library/os.html#os.PIDFD_NONBLOCK) flag, which opens a process file descriptor via [`os.pidfd_open()`](https://docs.python.org/3.14/library/os.html#os.pidfd_open) in non-blocking mode. Kumar Aditya supplied the patch.

[gh-96078](https://github.com/python/cpython/issues/96078): [`os.sched_yield()`](https://docs.python.org/3.14/library/os.html#os.sched_yield) now lets go of the GIL during its sched_yield(2) call. Donghee Na wrote the patch.

[gh-94199](https://github.com/python/cpython/issues/94199): The `ssl.RAND_pseudo_bytes()` function (which had been deprecated back in Python 3.6) is now gone; reach for [`os.urandom()`](https://docs.python.org/3.14/library/os.html#os.urandom) or [`ssl.RAND_bytes()`](https://docs.python.org/3.14/library/ssl.html#ssl.RAND_bytes) as a replacement. Victor Stinner supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
