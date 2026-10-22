# synchronization C API: `PyLockStatus`, `PyThread_allocate_lock()`, `PyThread_free_lock()`, `PyThread_acquire_lock_timed()`, `PyThread_acquire_lock()`, `PyThread_release_lock()`

type PyLockStatus

What you get back when a lock is acquired under a timeout.

 enumerator PY_LOCK_FAILURE

The lock could not be obtained.

 enumerator PY_LOCK_ACQUIRED

The lock was obtained without trouble.

 enumerator PY_LOCK_INTR

A signal cut the lock attempt short.

 PyThread_type_lock PyThread_allocate_lock(void)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Create a fresh lock.

When it succeeds, the function hands back a lock; when it fails, it hands back `0` and leaves no exception set.

There is no requirement for the caller to hold an [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state).

 void PyThread_free_lock(PyThread_type_lock lock)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Destroy *lock*. No thread should still be holding the lock at the time you call this.

There is no requirement for the caller to hold an [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state).

 PyLockStatus PyThread_acquire_lock_timed(PyThread_type_lock lock, long long microseconds, int intr_flag)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Grab *lock* subject to a timeout.

For up to *microseconds* microseconds this waits in an effort to take the lock. Once the timeout runs out, the function gives back `PY_LOCK_FAILURE`. A *microseconds* value of `-1` makes it wait without limit until the lock is freed.

With *intr_flag* set to `1`, a signal may break off the attempt to take the lock, and then the function gives back `PY_LOCK_INTR`. After such an interruption, the caller is normally expected to invoke [`Py_MakePendingCalls()`](https://docs.python.org/3.14/c-api/threads.html#c.Py_MakePendingCalls) so that an exception reaches Python code.

Should the lock be taken without issue, the function gives back `PY_LOCK_ACQUIRED`.

There is no requirement for the caller to hold an [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state).

 int PyThread_acquire_lock(PyThread_type_lock lock, int waitflag)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Grab *lock*.

When *waitflag* is `1` and some other thread is holding the lock at that moment, the function holds off until the lock becomes available and invariably gives back `1`.

When *waitflag* is `0` and a different thread holds the lock, the function skips waiting and just gives back `0`. If no other thread is holding the lock, it takes the lock and gives back `1`.

In contrast to `PyThread_acquire_lock_timed()`, no signal can break off the attempt to take this lock.

There is no requirement for the caller to hold an [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state).

 int PyThread_release_lock(PyThread_type_lock lock)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Release *lock*. Where *lock* is not currently held, the function raises a fatal error.

There is no requirement for the caller to hold an [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state).

[Subject index](INDEX.md) · [Owning C API section and shared conditions](legacy-locking-apis.md) · [Previous source contract](pythread-type-lock.md)
