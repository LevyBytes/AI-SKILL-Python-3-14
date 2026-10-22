# Deadlock Avoidance

### Deadlock Avoidance

There are two distinct ways critical sections steer you clear of deadlock:

1.

When a thread reaches for a lock some other thread is already holding, it pauses each of its own live critical sections first, letting go of their locks for the time being

2.

Once that blocking call wraps up, the section sitting at the top of the stack is the only one re-locked to begin with

The upshot is that nesting critical sections to grab several objects together won't work, since an inner section can pause the ones wrapping it. Reach for [`Py_BEGIN_CRITICAL_SECTION2`](https://docs.python.org/3.14/c-api/synchronization.html#c.Py_BEGIN_CRITICAL_SECTION2) instead when you truly need two objects locked together.

Keep in mind that everything described above concerns locks backed by [`PyMutex`](https://docs.python.org/3.14/c-api/synchronization.html#c.PyMutex) alone. The critical-section machinery is oblivious to — and has no bearing on — any other locking scheme you might be running, POSIX mutexes for example. Be aware too that although blocking on any `PyMutex` does pause the critical sections, the only mutexes set free are the ones belonging to those sections. A `PyMutex` taken outside a critical section stays held, and so misses out on the very same deadlock avoidance.

[Subject index](INDEX.md) · [Previous source context](how-critical-sections-work.md) · [Following source context](important-considerations.md)
