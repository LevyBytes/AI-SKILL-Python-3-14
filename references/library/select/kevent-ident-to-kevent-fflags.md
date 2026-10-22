# select: `kevent.ident`, `kevent.filter`, `kevent.flags`, `kevent.fflags`

### Kevent objects

[https://man.freebsd.org/cgi/man.cgi?query=kqueue&sektion=2](https://man.freebsd.org/cgi/man.cgi?query=kqueue&sektion=2)

 kevent.ident

Value used to pick out the event. How it is read depends on the filter, but it is usually the file descriptor. In the constructor ident may be either an int or an object carrying a [`fileno()`](https://docs.python.org/3.14/library/io.html#io.IOBase.fileno) method. kevent keeps the integer internally.

 kevent.filter

Name of the kernel filter.

| Constant | Meaning |
| --- | --- |
| `KQ_FILTER_READ` | Takes a descriptor and returns whenever there is data available to read. |
| `KQ_FILTER_WRITE` | Takes a descriptor and returns whenever there is data available to write. |
| `KQ_FILTER_AIO` | AIO requests. |
| `KQ_FILTER_VNODE` | Comes back as soon as any of the events being watched in *fflag* takes place. |
| `KQ_FILTER_PROC` | Watch for events on a process ID. |
| `KQ_FILTER_NETDEV` | Watch for events on a network device (not available on macOS). |
| `KQ_FILTER_SIGNAL` | Returns whenever the watched signal is delivered to the process. |
| `KQ_FILTER_TIMER` | Establishes an arbitrary timer. |

 kevent.flags

Filter action.

| Constant | Meaning |
| --- | --- |
| `KQ_EV_ADD` | Adds or modifies an event. |
| `KQ_EV_DELETE` | Removes an event from the queue. |
| `KQ_EV_ENABLE` | Permits control() to return the event. |
| `KQ_EV_DISABLE` | Disables event. |
| `KQ_EV_ONESHOT` | Removes event after first occurrence. |
| `KQ_EV_CLEAR` | Reset the state after an event is retrieved. |
| `KQ_EV_SYSFLAGS` | Internal event. |
| `KQ_EV_FLAG1` | Internal event. |
| `KQ_EV_EOF` | Filter-specific EOF condition. |
| `KQ_EV_ERROR` | See return values. |

 kevent.fflags

Filter-specific flags.

`KQ_FILTER_READ` and `KQ_FILTER_WRITE` filter flags:

| Constant | Meaning |
| --- | --- |
| `KQ_NOTE_LOWAT` | Low water mark of a socket buffer. |

`KQ_FILTER_VNODE` filter flags:

| Constant | Meaning |
| --- | --- |
| `KQ_NOTE_DELETE` | *unlink()* was called. |
| `KQ_NOTE_WRITE` | A write occurred. |
| `KQ_NOTE_EXTEND` | The file was extended. |
| `KQ_NOTE_ATTRIB` | An attribute was changed. |
| `KQ_NOTE_LINK` | The link count has changed. |
| `KQ_NOTE_RENAME` | The file was renamed. |
| `KQ_NOTE_REVOKE` | Access to the file was revoked. |

`KQ_FILTER_PROC` filter flags:

| Constant | Meaning |
| --- | --- |
| `KQ_NOTE_EXIT` | The process has exited. |
| `KQ_NOTE_FORK` | The process has called *fork()*. |
| `KQ_NOTE_EXEC` | The process has executed a new process. |
| `KQ_NOTE_PCTRLMASK` | Internal filter flag. |
| `KQ_NOTE_PDATAMASK` | Internal filter flag. |
| `KQ_NOTE_TRACK` | Follow a process across *fork()*. |
| `KQ_NOTE_CHILD` | Returned on the child process for *NOTE_TRACK*. |
| `KQ_NOTE_TRACKERR` | Unable to attach to a child. |

`KQ_FILTER_NETDEV` filter flags (not available on macOS):

| Constant | Meaning |
| --- | --- |
| `KQ_NOTE_LINKUP` | Link is up. |
| `KQ_NOTE_LINKDOWN` | Link is down. |
| `KQ_NOTE_LINKINV` | Link state is invalid. |

[Subject index](INDEX.md) · [Previous](kqueue-close-to-kqueue-fromfd.md) · [Continue](kevent-data-to-kevent-udata.md) · [Owning module, declaration or section: select](select-error-to-select-kevent.md)
