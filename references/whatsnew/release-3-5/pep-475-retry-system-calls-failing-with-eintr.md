# What’s New In Python 3.5 / PEP 475: Retry system calls failing with EINTR — errno, faulthandler, io, os, select, signal, socket, time

### PEP 475: Retry system calls failing with EINTR

Whenever a system call that is blocked waiting on I/O gets interrupted by a signal, an [`errno.EINTR`](https://docs.python.org/3.14/library/errno.html#errno.EINTR) error code comes back. In earlier versions, Python would raise [`InterruptedError`](https://docs.python.org/3.14/library/exceptions.html#InterruptedError) under those conditions. That left a developer building a Python application with two possible routes:

1.

Ignore the `InterruptedError`.

2.

Catch the `InterruptedError` and try restarting the interrupted system call wherever it gets invoked.

Going with the first route causes an application to fail now and then. Choosing the second piles on so much boilerplate that the code turns almost impossible to read. Compare:

```python
print("Hello World")

```

and:

```python
while True:
    try:
        print("Hello World")
        break
    except InterruptedError:
        continue

```

[**PEP 475**](https://peps.python.org/pep-0475/) puts in place automatic retrying of system calls upon `EINTR`. That lifts the chore of coping with `EINTR` or [`InterruptedError`](https://docs.python.org/3.14/library/exceptions.html#InterruptedError) out of user code for most scenarios and renders Python programs, the standard library included, more robust. Take note that the retry of a system call happens only when the signal handler does not raise an exception.

Here is the roster of functions that are now retried after a signal interrupts them:

- [`open()`](https://docs.python.org/3.14/library/functions.html#open) and [`io.open()`](https://docs.python.org/3.14/library/io.html#io.open);

- functions of the [`faulthandler`](https://docs.python.org/3.14/library/faulthandler.html#module-faulthandler) module;

- [`os`](https://docs.python.org/3.14/library/os.html#module-os) functions: [`fchdir()`](https://docs.python.org/3.14/library/os.html#os.fchdir), [`fchmod()`](https://docs.python.org/3.14/library/os.html#os.fchmod), [`fchown()`](https://docs.python.org/3.14/library/os.html#os.fchown), [`fdatasync()`](https://docs.python.org/3.14/library/os.html#os.fdatasync), [`fstat()`](https://docs.python.org/3.14/library/os.html#os.fstat), [`fstatvfs()`](https://docs.python.org/3.14/library/os.html#os.fstatvfs), [`fsync()`](https://docs.python.org/3.14/library/os.html#os.fsync), [`ftruncate()`](https://docs.python.org/3.14/library/os.html#os.ftruncate), [`mkfifo()`](https://docs.python.org/3.14/library/os.html#os.mkfifo), [`mknod()`](https://docs.python.org/3.14/library/os.html#os.mknod), [`open()`](https://docs.python.org/3.14/library/os.html#os.open), [`posix_fadvise()`](https://docs.python.org/3.14/library/os.html#os.posix_fadvise), [`posix_fallocate()`](https://docs.python.org/3.14/library/os.html#os.posix_fallocate), [`pread()`](https://docs.python.org/3.14/library/os.html#os.pread), [`pwrite()`](https://docs.python.org/3.14/library/os.html#os.pwrite), [`read()`](https://docs.python.org/3.14/library/os.html#os.read), [`readv()`](https://docs.python.org/3.14/library/os.html#os.readv), [`sendfile()`](https://docs.python.org/3.14/library/os.html#os.sendfile), [`wait3()`](https://docs.python.org/3.14/library/os.html#os.wait3), [`wait4()`](https://docs.python.org/3.14/library/os.html#os.wait4), [`wait()`](https://docs.python.org/3.14/library/os.html#os.wait), [`waitid()`](https://docs.python.org/3.14/library/os.html#os.waitid), [`waitpid()`](https://docs.python.org/3.14/library/os.html#os.waitpid), [`write()`](https://docs.python.org/3.14/library/os.html#os.write), [`writev()`](https://docs.python.org/3.14/library/os.html#os.writev);

- exceptional handling: [`os.close()`](https://docs.python.org/3.14/library/os.html#os.close) plus [`os.dup2()`](https://docs.python.org/3.14/library/os.html#os.dup2) now disregard [`EINTR`](https://docs.python.org/3.14/library/errno.html#errno.EINTR) errors, and their syscall stays un-retried (the PEP spells out why);

- [`select`](https://docs.python.org/3.14/library/select.html#module-select) functions: [`devpoll.poll()`](https://docs.python.org/3.14/library/select.html#select.devpoll.poll), [`epoll.poll()`](https://docs.python.org/3.14/library/select.html#select.epoll.poll), [`kqueue.control()`](https://docs.python.org/3.14/library/select.html#select.kqueue.control), [`poll.poll()`](https://docs.python.org/3.14/library/select.html#select.poll.poll), [`select()`](https://docs.python.org/3.14/library/select.html#select.select);

- methods of the [`socket`](https://docs.python.org/3.14/library/socket.html#socket.socket) class: [`accept()`](https://docs.python.org/3.14/library/socket.html#socket.socket.accept), [`connect()`](https://docs.python.org/3.14/library/socket.html#socket.socket.connect) (except for non-blocking sockets), [`recv()`](https://docs.python.org/3.14/library/socket.html#socket.socket.recv), [`recvfrom()`](https://docs.python.org/3.14/library/socket.html#socket.socket.recvfrom), [`recvmsg()`](https://docs.python.org/3.14/library/socket.html#socket.socket.recvmsg), [`send()`](https://docs.python.org/3.14/library/socket.html#socket.socket.send), [`sendall()`](https://docs.python.org/3.14/library/socket.html#socket.socket.sendall), [`sendmsg()`](https://docs.python.org/3.14/library/socket.html#socket.socket.sendmsg), [`sendto()`](https://docs.python.org/3.14/library/socket.html#socket.socket.sendto);

- [`signal.sigtimedwait()`](https://docs.python.org/3.14/library/signal.html#signal.sigtimedwait) and [`signal.sigwaitinfo()`](https://docs.python.org/3.14/library/signal.html#signal.sigwaitinfo);

- [`time.sleep()`](https://docs.python.org/3.14/library/time.html#time.sleep).

See also

[**PEP 475**](https://peps.python.org/pep-0475/) – Retry system calls failing with EINTR

The PEP and its code were authored by Charles-François Natali and Victor Stinner, aided by Antoine Pitrou (the French connection).

[Subject index](INDEX.md) · [Previous source section](pep471-scandir-directory-iteration.md) · [Next source section](pep-479-change-stopiteration-handling-inside-generators.md) · [Release/subject declaration](summary-release-highlights.md)
