# Python 3.14.0 beta 1 / library / fcntl

[gh-132915](https://github.com/python/cpython/issues/132915): [`fcntl.fcntl()`](https://docs.python.org/3.14/library/fcntl.html#fcntl.fcntl) and [`fcntl.ioctl()`](https://docs.python.org/3.14/library/fcntl.html#fcntl.ioctl) are now able to spot a buffer overflow and raise [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError). Because the stack and memory may be corrupted when this happens, the error is treated as fatal.

[gh-132742](https://github.com/python/cpython/issues/132742): [`fcntl.fcntl()`](https://docs.python.org/3.14/library/fcntl.html#fcntl.fcntl) now works with any [bytes-like objects](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) rather than just [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes). [`fcntl.ioctl()`](https://docs.python.org/3.14/library/fcntl.html#fcntl.ioctl) now retries on its own when system calls fail with EINTR and drops the GIL throughout a system call, including for a large bytes-like object.

[gh-127385](https://github.com/python/cpython/issues/127385): The `F_DUPFD_QUERY` constant is now part of the [`fcntl`](https://docs.python.org/3.14/library/fcntl.html#module-fcntl) module.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
