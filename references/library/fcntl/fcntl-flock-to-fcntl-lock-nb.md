# fcntl: `fcntl.flock()`, `fcntl.lockf()`, `fcntl.LOCK_UN`, `fcntl.LOCK_SH`, `fcntl.LOCK_EX`, `fcntl.LOCK_NB`

fcntl.flock(*fd*, *operation*, */*)

Carry out the lock operation *operation* against file descriptor *fd* (file objects that supply a [`fileno()`](https://docs.python.org/3.14/library/io.html#io.IOBase.fileno) method work too). The Unix manual *[flock(2)](https://manpages.debian.org/flock(2))* covers the details. (Certain systems emulate this function through `fcntl()`.)

Should the `flock()` call fail, an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) exception is raised.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `fcntl.flock` with arguments `fd`, `operation`.

 fcntl.lockf(*fd*, *cmd*, *len=0*, *start=0*, *whence=0*, */*)

In essence this wraps the `fcntl()` locking calls. *fd* names the file descriptor (file objects that supply a [`fileno()`](https://docs.python.org/3.14/library/io.html#io.IOBase.fileno) method work too) for the file you mean to lock or unlock, while *cmd* takes one of these values:

 fcntl.LOCK_UN

Release an existing lock.

 fcntl.LOCK_SH

Acquire a shared lock.

 fcntl.LOCK_EX

Acquire an exclusive lock.

 fcntl.LOCK_NB

Combine via bitwise OR with any one of the remaining three `LOCK_*` constants so the request becomes non-blocking.

When `LOCK_NB` is applied and the lock cannot be obtained, an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) gets raised, its *errno* attribute carrying [`EACCES`](https://docs.python.org/3.14/library/errno.html#errno.EACCES) or [`EAGAIN`](https://docs.python.org/3.14/library/errno.html#errno.EAGAIN) (which one depends on the operating system; for portability, test against both). On at least some systems, `LOCK_EX` works only when the file descriptor points at a file opened for writing.

*len* gives the count of bytes to lock, *start* gives the byte offset where the lock begins relative to *whence*, and *whence* follows [`io.IOBase.seek()`](https://docs.python.org/3.14/library/io.html#io.IOBase.seek), specifically:

- `0` – relative to the start of the file ([`os.SEEK_SET`](https://docs.python.org/3.14/library/os.html#os.SEEK_SET))

- `1` – relative to the current buffer position ([`os.SEEK_CUR`](https://docs.python.org/3.14/library/os.html#os.SEEK_CUR))

- `2` – relative to the end of the file ([`os.SEEK_END`](https://docs.python.org/3.14/library/os.html#os.SEEK_END))

The *start* default is 0, signifying the file's beginning. The *len* default is 0, signifying a lock running to the file's end. The *whence* default is likewise 0.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `fcntl.lockf` with arguments `fd`, `cmd`, `len`, `start`, `whence`.

Examples (all on a SVR4 compliant system):

```python
import struct, fcntl, os

f = open(...)
rv = fcntl.fcntl(f, fcntl.F_SETFL, os.O_NDELAY)

lockdata = struct.pack('hhllhh', fcntl.F_WRLCK, 0, 0, 0, 0, 0)
rv = fcntl.fcntl(f, fcntl.F_SETLKW, lockdata)

```

Observe that the return value variable *rv* carries an integer value in the first example, whereas in the second it carries a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object. Because the structure lay-out of the *lockdata* variable varies by system, the `flock()` call may serve you better.

See also

Module [`os`](https://docs.python.org/3.14/library/os.html#module-os)

When the locking flags [`O_SHLOCK`](https://docs.python.org/3.14/library/os.html#os.O_SHLOCK) and [`O_EXLOCK`](https://docs.python.org/3.14/library/os.html#os.O_EXLOCK) exist in the [`os`](https://docs.python.org/3.14/library/os.html#module-os) module (BSD only), the [`os.open()`](https://docs.python.org/3.14/library/os.html#os.open) function gives you an alternative to the `lockf()` and `flock()` functions.

[Subject index](INDEX.md) · [Previous](fcntl-fcntl-to-fcntl-ioctl.md) · [Owning module, declaration or section: fcntl](fcntl-fcntl-to-fcntl-ioctl.md)
