# Condition: `acquire()`, `notify()`, `locked()`, `notify_all()`, `release()`, `wait()`, `wait_for()`

*async *acquire()

Take hold of the underlying lock.

This method holds off until the underlying lock sits *unlocked*, flips it to *locked*, and hands back `True`.

 notify(*n=1*)

Rouse *n* tasks (1 unless stated otherwise) that are waiting on this condition. Where fewer than *n* tasks happen to be waiting, all of them are roused.

You must hold the lock before this method runs and let it go soon afterward. Invoking it while the lock is *unlocked* triggers a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) error.

 locked()

Hand back `True` whenever the underlying lock has been acquired.

 notify_all()

Rouse every task waiting on this condition.

This method behaves like `notify()`, except it rouses all of the waiting tasks.

You must hold the lock before this method runs and let it go soon afterward. Invoking it while the lock is *unlocked* triggers a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) error.

 release()

Let go of the underlying lock.

Calling this against a lock that is unlocked raises a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError).

 *async *wait()

Hold off until notified.

If the task making the call does not already hold the lock at the moment this method runs, a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) is raised.

This method gives up the underlying lock and then stays blocked until a `notify()` or `notify_all()` call rouses it. After being roused, the Condition takes its lock back and the method hands back `True`.

Keep in mind that a task *may* come back from this call without cause, so the caller should always re-examine the state and stand ready to invoke `wait()` again. On that account, you might rather turn to `wait_for()`.

 *async *wait_for(*predicate*)

Hold off until a predicate turns *true*.

The predicate has to be a callable whose result is read as a boolean. The method keeps invoking `wait()` over and over until the predicate comes out *true*. That last result is what gets returned.

[Subject index](INDEX.md) · [Previous](asyncio-condition-class.md) · [Continue](asyncio-semaphore-class.md) · [Owning module, declaration or section: asyncio.Condition](asyncio-condition-class.md) · [Owning module, declaration or section: Condition](asyncio-condition-class.md)
