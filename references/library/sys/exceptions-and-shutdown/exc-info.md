# sys.exc_info

sys.exc_info()

This function gives back the old-style view of the handled exception. When an exception `e` is being handled right now (so `exception()` would give back `e`), `exc_info()` returns the tuple `(type(e), e, e.__traceback__)`. That is, a tuple holding the exception's type (a subclass of [`BaseException`](https://docs.python.org/3.14/library/exceptions.html#BaseException)), the exception itself, and a [traceback object](https://docs.python.org/3.14/reference/datamodel.html#traceback-objects) that normally captures the call stack at the spot where the exception was last raised.

When nothing anywhere on the stack is handling an exception, this function gives back a tuple containing three `None` values.

Changed in version 3.11: Both the `type` and `traceback` fields now come out of the `value` (that exception instance), which means any change made to an exception during handling shows up in whatever later `exc_info()` calls return.

[API family](INDEX.md) · [sys context index](../INDEX.md).
