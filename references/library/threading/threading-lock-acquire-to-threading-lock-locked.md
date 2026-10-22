# threading.Lock: Primitive Lock acquisition, release and state

acquire(*blocking=True*, *timeout=-1*)

Take a lock, either blocking or non-blocking.

When called with the *blocking* argument equal to `True` (the default), wait until the lock becomes unlocked, then flip it to locked and hand back `True`.

When called with the *blocking* argument equal to `False`, never wait. Should a call with *blocking* equal to `True` have blocked, immediately hand back `False`; otherwise flip the lock to locked and hand back `True`.

When called with the floating-point *timeout* argument set to a positive number, wait no longer than that many seconds while the lock stays unavailable. Setting the *timeout* argument to `-1` means wait without limit. Supplying a *timeout* together with *blocking* equal to `False` is not allowed.

The return value comes back as `True` when the lock is taken successfully and `False` when it is not (such as when the *timeout* runs out).

Changed in version 3.2: The *timeout* parameter is new.

Changed in version 3.2: On POSIX, signals can now interrupt lock acquisition, provided the underlying threading implementation allows it.

Changed in version 3.14: On Windows, signals can now interrupt lock acquisition.

 release()

Free a lock. Any thread can perform this, not just the one that took the lock.

While the lock is locked, flip it back to unlocked and return. Should any other threads be blocked awaiting the lock turning unlocked, let precisely one of them advance.

Calling this on an unlocked lock produces a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError).

No value is returned.

 locked()

Hand back `True` when the lock is held.

[Subject index](INDEX.md) · [Previous](threading-lock-class.md) · [Continue](threading-rlock-class.md) · [Owning module, declaration or section: threading](threading-thread-based-parallelism.md) · [Owning module, declaration or section: threading.Lock](threading-lock-class.md) · [Owning module, declaration or section: Lock objects](threading-lock-class.md)
