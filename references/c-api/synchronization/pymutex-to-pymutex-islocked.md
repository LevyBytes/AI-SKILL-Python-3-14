# synchronization C API: `PyMutex`, `PyMutex_Lock()`, `PyMutex_Unlock()`, `PyMutex_IsLocked()`

type PyMutex

A mutual exclusion lock. To stand for the unlocked state, a `PyMutex` ought to be set to zero at initialization. As an illustration:

```c
PyMutex mutex = {0};

```

You should never copy or relocate a `PyMutex` instance. A `PyMutex` carries significance in both its contents and its address, so it has to stay put at one fixed, writable spot in memory.

Note

At present a `PyMutex` takes up a single byte, though you should treat that size as subject to change. Later Python releases may alter it with no deprecation period beforehand.

Added in version 3.13.

 void PyMutex_Lock(PyMutex *m)

* Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

Lock mutex *m*. Should a different thread already hold it locked, the calling thread blocks until the mutex frees up. For the duration of that block, the thread briefly detaches its [thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state), if one is present.

Added in version 3.13.

 void PyMutex_Unlock(PyMutex *m)

* Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

Unlock mutex *m*. It has to already be locked; if it is not, the function raises a fatal error.

Added in version 3.13.

 int PyMutex_IsLocked(PyMutex *m)

* Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

Yields a non-zero value when mutex *m* is locked at the moment, and zero if it is not.

Note

Reserve this function for assertions and debugging alone; do not base concurrency-control decisions on it, since the lock state can flip the instant after you check it.

Added in version 3.14.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](synchronization-primitives.md) · [Following source contract](py-begin-critical-section-to-py-end-critical-section.md)
