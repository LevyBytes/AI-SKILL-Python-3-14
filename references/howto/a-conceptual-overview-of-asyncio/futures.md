# Futures

### Futures

A [future](https://docs.python.org/3.14/library/asyncio-future.html#asyncio-future-obj) is an object whose purpose is to stand for the status and result of a computation. The name alludes to the notion of something yet to arrive or not yet occurred, and the object provides a means to keep tabs on that something.

A future carries a handful of important attributes. One of them is its state, which may be ?pending?, ?cancelled?, or ?done?. Another is its result, assigned once the state moves to done. In contrast to a coroutine, a future does not embody the computation itself; rather, it embodies the status and result of that computation, somewhat like an indicator or a status light (red, yellow, or green).

[`asyncio.Task`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task) extends [`asyncio.Future`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.Future) so as to acquire these various abilities. In the earlier section we said tasks hold a list of callbacks, which was not strictly correct. The logic is really implemented by the `Future` class, and `Task` inherits it.

Futures can be employed on their own as well (not only by way of tasks). A task flags itself as done once its coroutine completes. Futures are far more adaptable and become marked as done whenever you decide. In that sense, they are the flexible interface that lets you define your own rules for waiting and resuming.

[Subject index](INDEX.md) · [Previous source context](the-inner-workings-of-coroutines.md) · [Following source context](a-homemade-asyncio-sleep.md)
