# sys._current_frames

sys._current_frames()

Hand back a dictionary that maps each thread's identifier to the topmost stack frame that was active in that thread when the function was called. Bear in mind that functions in the [`traceback`](https://docs.python.org/3.14/library/traceback.html#module-traceback) module can reconstruct the call stack from such a frame.

This proves most valuable for diagnosing deadlock: the function asks nothing of the deadlocked threads, and the call stacks of those threads stay frozen for the entire time they remain deadlocked. For a thread that is not deadlocked, the returned frame may have nothing to do with that thread's current activity by the time the calling code looks at it.

Treat this function as reserved for internal and specialized use only.

Raises an auditing event `sys._current_frames` with no arguments.

[API family](INDEX.md) · [sys context index](../INDEX.md).
