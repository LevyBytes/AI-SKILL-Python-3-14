# select — `/dev/poll` polling objects

### `/dev/poll` polling objects

`/dev/poll` exists on Solaris and its derivatives. The cost of `/dev/poll` is *O*(*active file descriptors*), in contrast to `poll()`, whose cost is *O*(*number of file descriptors*), and `select()`, whose cost is *O*(*highest file descriptor*).

The way `/dev/poll` behaves is very near that of the standard `poll()` object.

 devpoll.close()

Close the file descriptor of the polling object.

Added in version 3.4.

 devpoll.closed

`True` if the polling object is closed.

Added in version 3.4.

 devpoll.fileno()

Return the file descriptor number of the polling object.

Added in version 3.4.

 devpoll.register(*fd*[, *eventmask*])

Enroll a file descriptor with the polling object. Subsequent invocations of the `poll()` method will then test whether that file descriptor has any outstanding I/O events. *fd* may be an integer, or it may be an object whose [`fileno()`](https://docs.python.org/3.14/library/io.html#io.IOBase.fileno) method returns an integer. Since file objects implement `fileno()`, they too serve as the argument.

*eventmask* is an optional bitmask spelling out which kinds of events you wish to test for. Its constants match those of the `poll()` object. The default value combines the constants `POLLIN`, `POLLPRI`, and `POLLOUT`.

Warning

Re-registering a file descriptor that is already registered is not an error, yet the outcome is undefined. The right move is to unregister or modify it beforehand. This marks an important difference from `poll()`.

 devpoll.modify(*fd*[, *eventmask*])

Internally this method performs an `unregister()` and then a `register()`. Doing it this way is (slightly) more efficient than spelling out both steps yourself.

 devpoll.unregister(*fd*)

Drop a file descriptor that a polling object is tracking. As with the `register()` method, *fd* may be an integer or an object whose [`fileno()`](https://docs.python.org/3.14/library/io.html#io.IOBase.fileno) method returns an integer.

Trying to drop a file descriptor that was never registered is quietly ignored.

 devpoll.poll([*timeout*])

Polls the collection of registered file descriptors and yields a list (possibly empty) of `(fd, event)` 2-tuples covering each descriptor with something to report, whether events or errors. Here *fd* names the file descriptor, while *event* is a bitmask carrying a set bit per event reported against that descriptor — for example `POLLIN` when input is pending, `POLLOUT` when the descriptor will accept a write, and similar. An empty list signals that the call timed out with no file descriptors having any events to report. When *timeout* is supplied, it sets the span of time in milliseconds the system will wait for events before it returns. When *timeout* is left out, set to -1, or [`None`](https://docs.python.org/3.14/library/constants.html#None), the call blocks until an event arrives for this poll object.

Changed in version 3.5: Rather than raising [`InterruptedError`](https://docs.python.org/3.14/library/exceptions.html#InterruptedError), a signal that interrupts the call now causes it to be tried again with a freshly computed timeout — unless the signal handler itself throws an exception (the reasoning is laid out in [**PEP 475**](https://peps.python.org/pep-0475/)).

[Subject index](INDEX.md) · [Previous](select-select-to-select-pipe-buf.md) · [Continue](epoll-close-to-epoll-poll.md) · [Owning module, declaration or section: select](select-error-to-select-kevent.md)
