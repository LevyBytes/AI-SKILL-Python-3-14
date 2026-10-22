# threading.Condition: `acquire()`, `release()`, `locked()`, `wait()`, `wait_for()`, `notify()`, `notify_all()`

acquire(**args*)

Take the underlying lock. This method invokes the matching method on the underlying lock; the return value is whatever that method gives back.

 release()

Free the underlying lock. This method invokes the matching method on the underlying lock; no value is returned.

 locked()

Hand back a boolean reporting whether this object is locked at the moment.

Added in version 3.14.

 wait(*timeout=None*)

Hold until notified or until a timeout arrives. Should the calling thread not have taken the lock when this method runs, a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) is raised.

This method frees the underlying lock, then blocks until a `notify()` or `notify_all()` call for the same condition variable in another thread rouses it, or until the optional timeout arrives. After being roused or timing out, it takes the lock again and returns.

When the *timeout* argument is supplied and is not `None`, it should be a floating-point number giving a timeout for the operation in seconds (or fractions of one).

When the underlying lock is an `RLock`, it does not get freed via its `release()` method, because that might not truly unlock the lock when it was taken several times recursively. Instead, an internal interface of the `RLock` class is used, which genuinely unlocks it even after several recursive acquisitions. A second internal interface afterward restores the recursion level once the lock is taken again.

The return value comes back as `True` unless the supplied *timeout* runs out, in which case it is `False`.

Changed in version 3.2: Previously, the method always returned `None`.

 wait_for(*predicate*, *timeout=None*)

Hold until a condition turns true. *predicate* should be a callable whose result is read as a boolean value. A *timeout* may be supplied giving the longest time to hold.

This convenience method may invoke `wait()` over and over until the predicate holds, or until a timeout arrives. The return value is the predicate's last return value and will read as `False` if the method timed out.

Setting aside the timeout feature, invoking this method roughly matches writing:

```python
while not predicate():
    cv.wait()

```

So the same rules apply as with `wait()`: you must hold the lock when calling it, and it is re-taken on return. The predicate is checked while the lock is held.

Added in version 3.2.

 notify(*n=1*)

By default, rouse one thread waiting on this condition, when any exist. Should the calling thread not have taken the lock when this method runs, a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) is raised.

This method rouses at most *n* of the threads waiting on the condition variable; it does nothing when no threads are waiting.

As currently built, it rouses exactly *n* threads, provided at least *n* threads are waiting. Even so, relying on that behavior is unsafe. A future, optimized build might now and then rouse more than *n* threads.

Note: a roused thread does not in fact return from its `wait()` call until it can take the lock again. Because `notify()` does not free the lock, the one calling it should.

 notify_all()

Rouse every thread waiting on this condition. This method behaves like `notify()`, but rouses all the waiting threads rather than one. Should the calling thread not have taken the lock when this method runs, a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) is raised.

The method `notifyAll` is a deprecated alias for this one.

[Subject index](INDEX.md) · [Previous](threading-condition-class.md) · [Continue](threading-semaphore-class.md) · [Owning module, declaration or section: threading](threading-thread-based-parallelism.md) · [Owning module, declaration or section: threading.Condition](threading-condition-class.md) · [Owning module, declaration or section: Condition objects](threading-condition-class.md)
