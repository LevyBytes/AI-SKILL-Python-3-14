# select — Kqueue objects

### Kqueue objects

 kqueue.close()

Close the control file descriptor of the kqueue object.

 kqueue.closed

`True` if the kqueue object is closed.

 kqueue.fileno()

Return the file descriptor number of the control fd.

 kqueue.fromfd(*fd*)

Create a kqueue object from a given file descriptor.

 kqueue.control(*changelist*, *max_events*[, *timeout*]) — eventlist

Low level interface to kevent

- changelist must be an iterable of kevent objects or `None`

- max_events must be 0 or a positive integer

- timeout in seconds (floats possible); the default is `None`, to wait forever

Changed in version 3.5: Rather than raising [`InterruptedError`](https://docs.python.org/3.14/library/exceptions.html#InterruptedError), a signal that interrupts the call now causes it to be tried again with a freshly computed timeout — unless the signal handler itself throws an exception (the reasoning is laid out in [**PEP 475**](https://peps.python.org/pep-0475/)).

[Subject index](INDEX.md) · [Previous](poll-register-to-poll-poll.md) · [Continue](kevent-ident-to-kevent-fflags.md) · [Owning module, declaration or section: select](select-error-to-select-kevent.md)
