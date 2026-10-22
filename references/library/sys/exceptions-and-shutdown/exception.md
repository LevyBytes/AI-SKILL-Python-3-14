# sys.exception

sys.exception()

Called while an exception handler is running (an `except` or `except*` clause, say), this function returns the exception instance that the handler caught. With exception handlers nested inside one another, only the exception belonging to the innermost handler is reachable.

When no exception handler is running, this function returns `None`.

Added in version 3.11.

[API family](INDEX.md) · [sys context index](../INDEX.md).
