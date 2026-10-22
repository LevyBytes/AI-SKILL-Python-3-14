# threading.Barrier: `wait()`, `reset()`, `abort()`

wait(*timeout=None*)

Clear the barrier. Once every thread party to the barrier has invoked this function, they are all freed at once. When a *timeout* is supplied, it takes priority over any that was given to the class constructor.

The return value is an integer between 0 and *parties* – 1, distinct for each thread. You can use this to single out a thread for some special housekeeping, for example:

```python
i = barrier.wait()
if i == 0:
    # Only one thread needs to print this
    print("passed the barrier")

```

When an *action* was supplied to the constructor, one of the threads will have invoked it ahead of being freed. Should that call raise an error, the barrier enters the broken state.

Should the call time out, the barrier enters the broken state.

This method may raise a `BrokenBarrierError` exception if the barrier breaks or resets while a thread waits.

 reset()

Put the barrier back into its default, empty condition. Whichever threads are waiting on it will get the `BrokenBarrierError` exception.

Be aware that using this function may call for some external coordination if there are other threads whose state you do not know. When a barrier is broken, leaving it alone and building a fresh one may be the better course.

 abort()

Drive the barrier into a broken state. This makes any present or future calls to `wait()` fail with the `BrokenBarrierError`. Use it, for instance, when one of the threads has to abort, so the application avoids deadlock.

Building the barrier with a sensible *timeout* value to guard automatically against one of the threads going wrong may be the better choice.

 parties

The count of threads needed to clear the barrier.

 n_waiting

The count of threads waiting in the barrier at the moment.

 broken

A boolean that is `True` when the barrier sits in the broken state.

[Subject index](INDEX.md) · [Previous](threading-barrier-class.md) · [Continue](threading-brokenbarriererror.md) · [Owning module, declaration or section: threading](threading-thread-based-parallelism.md) · [Owning module, declaration or section: threading.Barrier](threading-barrier-class.md) · [Owning module, declaration or section: Barrier objects](threading-barrier-class.md)
