# OS exceptions

### OS exceptions

The exceptions below are subclasses of `OSError`; which one gets thrown depends on the system error code.

 *exception *BlockingIOError

Thrown when an operation would block on an object (a socket, say) configured for non-blocking operation. Maps to `errno` [`EAGAIN`](https://docs.python.org/3.14/library/errno.html#errno.EAGAIN), [`EALREADY`](https://docs.python.org/3.14/library/errno.html#errno.EALREADY), [`EWOULDBLOCK`](https://docs.python.org/3.14/library/errno.html#errno.EWOULDBLOCK) and [`EINPROGRESS`](https://docs.python.org/3.14/library/errno.html#errno.EINPROGRESS).

Beyond what `OSError` provides, `BlockingIOError` can carry one further attribute:

 characters_written

An integer holding how many **bytes** reached the stream before it blocked. This attribute is present when you use the buffered I/O classes out of the [`io`](https://docs.python.org/3.14/library/io.html#module-io) module.

 *exception *ChildProcessError

Thrown when an operation on a child process did not succeed. Maps to `errno` [`ECHILD`](https://docs.python.org/3.14/library/errno.html#errno.ECHILD).

 *exception *ConnectionError

A base class covering connection-related troubles.

Its subclasses are `BrokenPipeError`, `ConnectionAbortedError`, `ConnectionRefusedError` and `ConnectionResetError`.

 *exception *BrokenPipeError

A subclass of `ConnectionError`, thrown when you try to write to a pipe whose far end has been closed, or to write to a socket that has been shut down for writing. Maps to `errno` [`EPIPE`](https://docs.python.org/3.14/library/errno.html#errno.EPIPE) and [`ESHUTDOWN`](https://docs.python.org/3.14/library/errno.html#errno.ESHUTDOWN).

 *exception *ConnectionAbortedError

A subclass of `ConnectionError`, thrown when the peer aborts a connection attempt. Maps to `errno` [`ECONNABORTED`](https://docs.python.org/3.14/library/errno.html#errno.ECONNABORTED).

 *exception *ConnectionRefusedError

A subclass of `ConnectionError`, thrown when the peer refuses a connection attempt. Maps to `errno` [`ECONNREFUSED`](https://docs.python.org/3.14/library/errno.html#errno.ECONNREFUSED).

 *exception *ConnectionResetError

A subclass of `ConnectionError`, thrown when the peer resets a connection. Maps to `errno` [`ECONNRESET`](https://docs.python.org/3.14/library/errno.html#errno.ECONNRESET).

 *exception *FileExistsError

Thrown when you try to create a file or directory that is already present. Maps to `errno` [`EEXIST`](https://docs.python.org/3.14/library/errno.html#errno.EEXIST).

 *exception *FileNotFoundError

Thrown when a file or directory is asked for but is not there. Maps to `errno` [`ENOENT`](https://docs.python.org/3.14/library/errno.html#errno.ENOENT).

 *exception *InterruptedError

Thrown when an incoming signal interrupts a system call. Maps to `errno` [`EINTR`](https://docs.python.org/3.14/library/errno.html#errno.EINTR).

Changed in version 3.5: rather than throwing `InterruptedError`, Python now retries a system call interrupted by a signal, unless the signal handler itself raises an exception (consult [**PEP 475**](https://peps.python.org/pep-0475/) for the reasoning).

 *exception *IsADirectoryError

Thrown when a file operation (for instance [`os.remove()`](https://docs.python.org/3.14/library/os.html#os.remove)) is asked for against a directory. Maps to `errno` [`EISDIR`](https://docs.python.org/3.14/library/errno.html#errno.EISDIR).

 *exception *NotADirectoryError

Thrown when a directory operation (for instance [`os.listdir()`](https://docs.python.org/3.14/library/os.html#os.listdir)) is asked for against something that is not a directory. On the majority of POSIX platforms, it may likewise be thrown when an operation tries to open or walk a non-directory file as though it were a directory. Maps to `errno` [`ENOTDIR`](https://docs.python.org/3.14/library/errno.html#errno.ENOTDIR).

 *exception *PermissionError

Thrown when you try to perform an operation without sufficient access rights — filesystem permissions, for example. Maps to `errno` [`EACCES`](https://docs.python.org/3.14/library/errno.html#errno.EACCES), [`EPERM`](https://docs.python.org/3.14/library/errno.html#errno.EPERM), and [`ENOTCAPABLE`](https://docs.python.org/3.14/library/errno.html#errno.ENOTCAPABLE).

Changed in version 3.11.1: WASI’s [`ENOTCAPABLE`](https://docs.python.org/3.14/library/errno.html#errno.ENOTCAPABLE) is now mapped to `PermissionError`.

 *exception *ProcessLookupError

Thrown when a specified process does not exist. Maps to `errno` [`ESRCH`](https://docs.python.org/3.14/library/errno.html#errno.ESRCH).

 *exception *TimeoutError

Thrown when a system function reaches a timeout at the system level. Maps to `errno` [`ETIMEDOUT`](https://docs.python.org/3.14/library/errno.html#errno.ETIMEDOUT).

Added in version 3.3: All the above `OSError` subclasses were added.

See also

[**PEP 3151**](https://peps.python.org/pep-3151/) - Reworking the OS and IO exception hierarchy

[Subject index](INDEX.md) · [Previous](unboundlocalerror-to-windowserror.md) · [Continue](warning-to-resourcewarning.md)
