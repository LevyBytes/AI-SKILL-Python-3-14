# threading.RLock: Reentrant RLock acquisition, release and state

acquire(*blocking=True*, *timeout=-1*)

Take a lock, either blocking or non-blocking.

See also

Using RLock as a context manager

Preferred over manual `acquire()` and `release()` calls wherever feasible.

When called with the *blocking* argument equal to `True` (the default):

>
- When no thread owns the lock, take the lock and return at once.

- When a different thread owns the lock, wait until we manage to take the lock, or until *timeout*, if it was set to a positive float value.

- When the calling thread already owns the lock, take it once more and return at once. Here lies the contrast between `Lock` and `RLock`; `Lock` treats this case like the prior one, blocking until the lock can be taken.

When called with the *blocking* argument equal to `False`:

>
- When no thread owns the lock, take the lock and return at once.

- When a different thread owns the lock, return at once.

- When the calling thread already owns the lock, take it once more and return at once.

Across every case, if the thread managed to take the lock, hand back `True`. If the thread could not take the lock (that is, if it was non-blocking or the timeout was hit) hand back `False`.

When called repeatedly, neglecting to call `release()` the same number of times can lead to deadlock. Think about using `RLock` as a context manager in place of calling acquire/release by hand.

Changed in version 3.2: The *timeout* parameter is new.

 release()

Free a lock, lowering the recursion level by one. If the level reaches zero after that decrement, return the lock to unlocked (owned by no thread), and should any other threads be blocked awaiting the lock turning unlocked, let precisely one of them advance. If the recursion level remains nonzero after the decrement, the lock stays locked and owned by the calling thread.

Invoke this method only when the calling thread owns the lock. Calling it when the lock is not held produces a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError).

No value is returned.

 locked()

Hand back a boolean reporting whether this object is locked at the moment.

Added in version 3.14.

[Subject index](INDEX.md) · [Previous](threading-rlock-class.md) · [Continue](threading-condition-class.md) · [Owning module, declaration or section: threading](threading-thread-based-parallelism.md) · [Owning module, declaration or section: threading.RLock](threading-rlock-class.md) · [Owning module, declaration or section: RLock objects](threading-rlock-class.md)
