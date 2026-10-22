# threading.Event: `is_set()`, `set()`, `clear()`, `wait()`

is_set()

Hand back `True` exactly when the internal flag is true.

The method `isSet` is a deprecated alias for this one.

 set()

Turn the internal flag true. Every thread waiting on it to turn true is woken. Threads that invoke `wait()` while the flag is already true will not block in the slightest.

 clear()

Turn the internal flag back false. After that, threads invoking `wait()` will block until `set()` is invoked to turn the internal flag true once more.

 wait(*timeout=None*)

Block while the internal flag stays false and the timeout, if supplied, has not run out. The return value conveys why this blocking method returned; `True` when it returns because the internal flag was turned true, or `False` when a timeout is supplied and the internal flag stayed false through the given wait time.

When the timeout argument is supplied and is not `None`, it should be a floating-point number giving a timeout for the operation in seconds, or fractions of one.

Changed in version 3.1: Previously, the method always returned `None`.

[Subject index](INDEX.md) · [Previous](threading-event-class.md) · [Continue](threading-timer-class.md) · [Owning module, declaration or section: threading](threading-thread-based-parallelism.md) · [Owning module, declaration or section: threading.Event](threading-event-class.md) · [Owning module, declaration or section: Event objects](threading-event-class.md)
