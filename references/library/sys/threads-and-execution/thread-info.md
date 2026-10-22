# sys.thread_info

sys.thread_info

A [named tuple](https://docs.python.org/3.14/glossary.html#term-named-tuple) carrying details about the thread implementation.

 thread_info.name

What the thread implementation is called:

- `"nt"`: Windows threads

- `"pthread"`: POSIX threads

- `"pthread-stubs"`: stubbed-out POSIX threads (used on WebAssembly platforms that lack threading support)

- `"solaris"`: Solaris threads

 thread_info.lock

What the lock implementation is called:

- `"semaphore"`: the lock is built on a semaphore

- `"mutex+cond"`: the lock is built on a mutex paired with a condition variable

- `None` if this information is unknown

 thread_info.version

The thread library’s name together with its version. This is a string, or `None` when the detail isn’t known.

Added in version 3.3.

[API family](INDEX.md) · [sys context index](../INDEX.md).
