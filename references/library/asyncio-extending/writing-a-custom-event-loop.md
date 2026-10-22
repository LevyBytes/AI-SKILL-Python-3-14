# Writing a Custom Event Loop

### Writing a Custom Event Loop

[`asyncio.AbstractEventLoop`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.AbstractEventLoop) exposes a great many methods, and coding every one of them yourself is tedious work.

By subclassing `asyncio.BaseEventLoop`, a loop inherits ready-made implementations of many of the common methods at no cost.

The subclass, for its part, still needs to fill in a set of *private* methods that `asyncio.BaseEventLoop` declares yet leaves unimplemented.

To illustrate, `loop.create_connection()` validates its arguments, performs DNS resolution, and then invokes `loop._make_socket_transport()`, which the deriving class is expected to provide. That `_make_socket_transport()` method carries no documentation and counts as an *internal* API.

[Subject index](INDEX.md) · [Previous](extending.md) · [Continue](future-init-to-task-init.md)
