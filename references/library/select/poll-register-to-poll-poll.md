# select - Polling objects

### Polling objects

The `poll()` system call, backed by most Unix systems, scales better for network servers handling very many simultaneous clients. The reason `poll()` scales better is that the system call merely needs the file descriptors of interest listed, whereas `select()` constructs a bitmap, switches on bits for the fds in question, and then has to linearly rescan the entire bitmap afterward. In complexity terms, `poll()` runs at *O*(*number of file descriptors*), whereas `select()` runs at *O*(*highest file descriptor*).

 poll.register(*fd*[, *eventmask*])

Enroll a file descriptor with the polling object. Subsequent invocations of the `poll()` method will then test whether that file descriptor has any outstanding I/O events. *fd* may be an integer, or it may be an object whose [`fileno()`](https://docs.python.org/3.14/library/io.html#io.IOBase.fileno) method returns an integer. Since file objects implement `fileno()`, they too serve as the argument.

*eventmask* is an optional bitmask spelling out which kinds of events you wish to test for, and may combine the constants `POLLIN`, `POLLPRI`, and `POLLOUT` that the table below describes. Left unspecified, the default value tests for all 3 event types.

| Constant | Meaning |
| --- | --- |
| `POLLIN` | There is data to read. |
| `POLLPRI` | There is urgent data to read. |
| `POLLOUT` | Ready for output: writing will not block. |
| `POLLERR` | Error condition of some sort. |
| `POLLHUP` | Hung up. |
| `POLLRDHUP` | Stream socket peer closed connection, or shut down writing half of connection. |
| `POLLNVAL` | Invalid request: descriptor not open. |

Re-registering a file descriptor that is already registered is not an error and produces the same result as registering that descriptor a single time.

 poll.modify(*fd*, *eventmask*)

Adjusts an fd that is already registered. The effect matches that of `register(fd, eventmask)`. Trying to modify a file descriptor that was never registered triggers an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) exception carrying errno `ENOENT`.

 poll.unregister(*fd*)

Drop a file descriptor that a polling object is tracking. As with the `register()` method, *fd* may be an integer or an object whose [`fileno()`](https://docs.python.org/3.14/library/io.html#io.IOBase.fileno) method returns an integer.

Trying to drop a file descriptor that was never registered triggers a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) exception.

 poll.poll([*timeout*])

Polls the collection of registered file descriptors and yields a list (possibly empty) of `(fd, event)` 2-tuples covering each descriptor with something to report, whether events or errors. Here *fd* names the file descriptor, while *event* is a bitmask carrying a set bit per event reported against that descriptor — for example `POLLIN` when input is pending, `POLLOUT` when the descriptor will accept a write, and similar. An empty list signals that the call timed out with no file descriptors having any events to report. When *timeout* is supplied, it sets the span of time in milliseconds the system will wait for events before it returns. When *timeout* is left out, negative, or [`None`](https://docs.python.org/3.14/library/constants.html#None), the call blocks until an event arrives for this poll object.

Changed in version 3.5: Rather than raising [`InterruptedError`](https://docs.python.org/3.14/library/exceptions.html#InterruptedError), a signal that interrupts the call now causes it to be tried again with a freshly computed timeout — unless the signal handler itself throws an exception (the reasoning is laid out in [**PEP 475**](https://peps.python.org/pep-0475/)).

[Subject index](INDEX.md) · [Previous](epoll-close-to-epoll-poll.md) · [Continue](kqueue-close-to-kqueue-fromfd.md) · [Owning module, declaration or section: select](select-error-to-select-kevent.md)
