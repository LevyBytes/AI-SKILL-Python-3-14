# select - Edge and level trigger polling (epoll) objects

### Edge and level trigger polling (epoll) objects

>

[https://linux.die.net/man/4/epoll](https://linux.die.net/man/4/epoll)

The *eventmask* is a bit mask using the following constants:

| Constant | Meaning |
| --- | --- |
| `EPOLLIN` | Available for read. |
| `EPOLLOUT` | Available for write. |
| `EPOLLPRI` | Urgent data for read. |
| `EPOLLERR` | Error condition happened on the associated fd. |
| `EPOLLHUP` | Hang up happened on the associated fd. |
| `EPOLLET` | Set Edge Trigger behavior, the default is Level Trigger behavior. |
| `EPOLLONESHOT` | Turn on one-shot mode: once a single event has been retrieved, the fd gets disabled internally. |
| `EPOLLEXCLUSIVE` | When an event arrives on the associated fd, rouse just a single epoll object. Leaving this flag unset (the default) instead rouses every epoll object that polls on that fd. |
| `EPOLLRDHUP` | Stream socket peer closed connection or shut down writing half of connection. |
| `EPOLLRDNORM` | Equivalent to `EPOLLIN` |
| `EPOLLRDBAND` | Priority data band can be read. |
| `EPOLLWRNORM` | Equivalent to `EPOLLOUT`. |
| `EPOLLWRBAND` | Priority data may be written. |
| `EPOLLMSG` | Ignored. |
| `EPOLLWAKEUP` | Prevents sleep during event waiting. |

Added in version 3.6: Introduced `EPOLLEXCLUSIVE`, which requires Linux Kernel 4.5 or newer to function.

Added in version 3.14: Introduced `EPOLLWAKEUP`, which requires Linux Kernel 3.5 or newer to function.

 epoll.close()

Close the control file descriptor of the epoll object.

 epoll.closed

`True` if the epoll object is closed.

 epoll.fileno()

Return the file descriptor number of the control fd.

 epoll.fromfd(*fd*)

Create an epoll object from a given file descriptor.

 epoll.register(*fd*[, *eventmask*])

Register a file descriptor *fd* with the epoll object.

 epoll.modify(*fd*, *eventmask*)

Modify a registered file descriptor *fd*.

 epoll.unregister(*fd*)

Remove a registered file descriptor from the epoll object.

Changed in version 3.9: The method no longer ignores the [`EBADF`](https://docs.python.org/3.14/library/errno.html#errno.EBADF) error.

 epoll.poll(*timeout=None*, *maxevents=-1*)

Wait for events. timeout in seconds (float)

Changed in version 3.5: Rather than raising [`InterruptedError`](https://docs.python.org/3.14/library/exceptions.html#InterruptedError), a signal that interrupts the call now causes it to be tried again with a freshly computed timeout — unless the signal handler itself throws an exception (the reasoning is laid out in [**PEP 475**](https://peps.python.org/pep-0475/)).

[Subject index](INDEX.md) · [Previous](devpoll-close-to-devpoll-poll.md) · [Continue](poll-register-to-poll-poll.md) · [Owning module, declaration or section: select](select-error-to-select-kevent.md)
