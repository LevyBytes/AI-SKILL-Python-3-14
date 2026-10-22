# sys._current_exceptions

sys._current_exceptions()

Hand back a dictionary that maps each thread's identifier to the topmost exception that was active in that thread when the function was called. A thread that is not currently handling an exception is left out of the resulting dictionary.

This proves most valuable for statistical profiling.

Treat this function as reserved for internal and specialized use only.

Raises an auditing event `sys._current_exceptions` with no arguments.

Changed in version 3.12: Every dictionary value is now one exception instance on its own, no longer the 3-tuple that `sys.exc_info()` produces.

[API family](INDEX.md) · [sys context index](../INDEX.md).
