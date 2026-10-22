# BoundedSemaphore

### BoundedSemaphore

 *class *asyncio.BoundedSemaphore(*value=1*)

A bounded semaphore object. Carries no thread safety.

Bounded Semaphore is a flavor of `Semaphore` that raises a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) from `release()` should it push the internal counter past the starting *value*.

Changed in version 3.10: Removed the *loop* parameter.

[Subject index](INDEX.md) · [Previous](asyncio-semaphore-acquire-to-asyncio-semaphore-release.md) · [Continue](asyncio-barrier-class.md)
