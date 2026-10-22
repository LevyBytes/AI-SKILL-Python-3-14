# Python 3.12.0 beta 1 / library / collections and iteration

[gh-97696](https://github.com/python/cpython/issues/97696): Built an eager task factory into asyncio. Set as an event loop's task factory, it runs coroutines eagerly. Any coroutine capable of finishing synchronously (returning or raising without blocking) comes straight back as a completed task and never reaches the event loop's schedule. Should the coroutine block, its still-pending task is scheduled and then returned.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
