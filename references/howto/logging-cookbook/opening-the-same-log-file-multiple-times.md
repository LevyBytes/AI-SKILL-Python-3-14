# Opening the same log file multiple times

### Opening the same log file multiple times

Under Windows you typically cannot open one file several times, since doing so triggers a “file is in use by another process” error. On POSIX platforms, by contrast, opening the same file repeatedly raises no errors. It can happen by accident, for instance through:

- Registering a file handler more than once that points at the same file (via a copy/paste/forget-to-change slip, say).

- Opening two files that seem distinct because their names differ, yet are identical since one is a symbolic link to the other.

- Forking a process, after which both the parent and the child hold a reference to the same file. This can arise through use of the [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) module, as one example.

Opening one file repeatedly may *seem* to work much of the time, yet real-world usage can produce several problems:

- Logging output may come out garbled when several threads or processes attempt to write into the same file. Logging does protect a single handler instance against concurrent use by multiple threads, but it offers no such safeguard when two different threads write concurrently through two separate handler instances that happen to target the same file.

- A bid to delete a file (during file rotation, say) fails quietly because another reference still points at it. The result is confusion and squandered debugging time - log entries surface in unexpected spots or vanish entirely. Or a file meant to be moved stays put and swells unexpectedly even though size-based rotation is supposedly active.

Apply the methods described in Logging to a single file from multiple processes to sidestep such troubles.

[Subject index](INDEX.md) · [Previous source context](patterns-to-avoid.md) · [Following source context](logger-attributes-and-parameter-misuse.md)
