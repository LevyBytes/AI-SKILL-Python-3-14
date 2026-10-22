# Python 3.13.0 beta 1 / core and builtins / collections and iteration

[gh-117714](https://github.com/python/cpython/issues/117714): Adjust `async_generator.athrow().close()` together with `async_generator.asend().close()` so each shuts down its portion of the underlying async generator

[gh-118272](https://github.com/python/cpython/issues/118272): Repair a bug where `generator.close` failed to release the locals belonging to the generator's frame.

[gh-117881](https://github.com/python/cpython/issues/117881): block simultaneous access to an async generator through athrow().throw() or asend().throw()

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
