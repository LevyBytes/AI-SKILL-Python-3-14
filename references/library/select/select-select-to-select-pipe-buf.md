# select: `select.select()`, `select.PIPE_BUF`

select.select(*rlist*, *wlist*, *xlist*, *timeout=None*)

Here is a thin wrapper over the Unix `select()` system call. Its first three arguments are iterables of "waitable objects": either integers standing for file descriptors or objects carrying a no-argument method called [`fileno()`](https://docs.python.org/3.14/library/io.html#io.IOBase.fileno) that yields such an integer:

- *rlist*: wait until ready for reading

- *wlist*: wait until ready for writing

- *xlist*: wait for an "exceptional condition" (consult your manual page to learn which conditions your particular system treats this way)

Empty iterables may be passed, though whether three empty iterables are accepted varies by platform. (Unix is known to permit this, whereas Windows is not.) The optional *timeout* argument states a time-out, given as a floating-point number of seconds. With the *timeout* argument left out or set to `None`, the call blocks until a minimum of one file descriptor becomes ready. A time-out of zero means a poll and never blocks.

What comes back is a triple of lists of ready objects: subsets of the first three arguments. Should the time-out elapse before any file descriptor turns ready, the result is three empty lists.

The object types allowed within the iterables include Python [file objects](https://docs.python.org/3.14/glossary.html#term-file-object) (for example `sys.stdin`, or whatever [`open()`](https://docs.python.org/3.14/library/functions.html#open) or [`os.popen()`](https://docs.python.org/3.14/library/os.html#os.popen) returns), along with socket objects from [`socket.socket()`](https://docs.python.org/3.14/library/socket.html#socket.socket). Defining your own *wrapper* class is also fine, provided it carries a suitable [`fileno()`](https://docs.python.org/3.14/library/io.html#io.IOBase.fileno) method (one that genuinely returns a file descriptor, rather than some arbitrary integer).

Note

Under Windows, file objects are not allowed, but sockets are. On Windows the underlying `select()` function comes from the WinSock library and won't deal with file descriptors that did not come from WinSock.

Changed in version 3.5: Rather than raising [`InterruptedError`](https://docs.python.org/3.14/library/exceptions.html#InterruptedError), a signal that interrupts the call now causes it to be tried again with a freshly computed timeout — unless the signal handler itself throws an exception (the reasoning is laid out in [**PEP 475**](https://peps.python.org/pep-0475/)).

 select.PIPE_BUF

The fewest bytes you may write to a pipe without blocking once that pipe has been flagged ready for writing by `select()`, `poll()`, or some other interface in this module. It has no bearing on other sorts of file-like objects, sockets among them.

POSIX guarantees this value to be no less than 512.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix

Added in version 3.2.

[Subject index](INDEX.md) · [Previous](select-error-to-select-kevent.md) · [Continue](devpoll-close-to-devpoll-poll.md) · [Owning module, declaration or section: select](select-error-to-select-kevent.md)
