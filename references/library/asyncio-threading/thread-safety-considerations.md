# Thread safety considerations

### Thread safety considerations

Although asyncio is built to be thread-safe under free-threaded Python, a few points still deserve attention whenever you mix asyncio with threads:

1.

**Event loop**: Give every thread an event loop of its own and never share one between threads. Keeping them separate lets each event loop look after its own tasks and callbacks without other threads getting in the way.

2.

**Task management**: A task or future made in one thread must not be awaited or touched from a different thread.

3.

**Thread-safe APIs**: Whenever you reach asyncio from several threads, lean on the thread-safe APIs that asyncio offers — for instance [`asyncio.run_coroutine_threadsafe()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.run_coroutine_threadsafe) to hand a coroutine to an event loop from another thread. Should you need to fire a callback from a different thread, [`loop.call_soon_threadsafe()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.call_soon_threadsafe) schedules it safely.

4.

**Synchronization**: asyncio's own synchronization primitives (such as [`asyncio.Lock`](https://docs.python.org/3.14/library/asyncio-sync.html#asyncio.Lock) and [`asyncio.Event`](https://docs.python.org/3.14/library/asyncio-sync.html#asyncio.Event)) were never meant to span threads. When coordination across threads is required, turn instead to the synchronization primitives in the [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) module.

[Subject index](INDEX.md) · [Previous](asyncio-and-free-threaded-python.md) · [Continue](using-asyncio-with-threads.md)
