# Barrier: `asyncio.BrokenBarrierError`

*exception *asyncio.BrokenBarrierError

This exception, which subclasses [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError), is raised once the `Barrier` object gets reset or broken.

---

Changed in version 3.9: Taking a lock by way of `await lock` or `yield from lock`, and/or through a [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement (`with await lock`, `with (yield from lock)`), was dropped. Reach for `async with lock` in its place.

[Subject index](INDEX.md) · [Previous](asyncio-barrier-wait-to-asyncio-barrier-abort.md) · [Owning module, declaration or section: Barrier](asyncio-barrier-class.md)
