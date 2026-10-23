# What's New In Python 3.13 / asyncio - asyncio-eventloop, asyncio-exceptions, asyncio-protocol, asyncio-queue, asyncio-stream, asyncio-task

### asyncio

- [`asyncio.as_completed()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.as_completed) henceforth hands back an object serving simultaneously as an [asynchronous iterator](https://docs.python.org/3.14/glossary.html#term-asynchronous-iterator) and an ordinary [iterator](https://docs.python.org/3.14/glossary.html#term-iterator) over [awaitables](https://docs.python.org/3.14/glossary.html#term-awaitable). Each awaitable produced during asynchronous iteration carries the very task or future object you passed in, so pairing a result with its completing task becomes simpler. (Contributed by Justin Arthur in [gh-77714](https://github.com/python/cpython/issues/77714).)

- [`asyncio.loop.create_unix_server()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_unix_server) henceforth deletes the Unix socket on its own once the server shuts down. (Contributed by Pierre Ossman in [gh-111246](https://github.com/python/cpython/issues/111246).)

- [`DatagramTransport.sendto()`](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio.DatagramTransport.sendto) henceforth dispatches zero-length datagrams whenever invoked with an empty bytes object. Buffer-size computation in the transport flow control now also factors in the datagram header. (Contributed by Jamie Phan in [gh-115199](https://github.com/python/cpython/issues/115199).)

- Add [`Queue.shutdown`](https://docs.python.org/3.14/library/asyncio-queue.html#asyncio.Queue.shutdown) plus [`QueueShutDown`](https://docs.python.org/3.14/library/asyncio-queue.html#asyncio.QueueShutDown) for handling queue termination. (Contributed by Laurie Opperman and Yves Duprat in [gh-104228](https://github.com/python/cpython/issues/104228).)

- Add the [`Server.close_clients()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.Server.close_clients) plus [`Server.abort_clients()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.Server.abort_clients) methods, both of which shut down an asyncio server more aggressively. (Contributed by Pierre Ossman in [gh-113538](https://github.com/python/cpython/issues/113538).)

- Accept a tuple of separators inside [`StreamReader.readuntil()`](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio.StreamReader.readuntil), halting as soon as any single one of them shows up. (Contributed by Bruce Merry in [gh-81322](https://github.com/python/cpython/issues/81322).)

- Improve how [`TaskGroup`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.TaskGroup) behaves whenever an outside cancellation runs into an inside cancellation. As one example, with two task groups nested together and a child task raising an exception within each at the same moment, the outer task group could end up hanging, since the inner task group had absorbed its internal cancellation.

When a task group is cancelled from outside and additionally has to raise an [`ExceptionGroup`](https://docs.python.org/3.14/library/exceptions.html#ExceptionGroup), it henceforth invokes the parent task's [`cancel()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task.cancel) method. Doing so guarantees a [`CancelledError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.CancelledError) gets raised at the following [`await`](https://docs.python.org/3.14/reference/expressions.html#await), keeping the cancellation from being dropped.

A further upside of this work is that task groups henceforth keep the cancellation count intact ([`cancelling()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task.cancelling)).

So that a few edge cases get covered, [`uncancel()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task.uncancel) may henceforth clear the undocumented `_must_cancel` flag once the cancellation count drops to zero.

(Inspired by an issue reported by Arthur Tacca in [gh-116720](https://github.com/python/cpython/issues/116720).)

- Whenever [`TaskGroup.create_task()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.TaskGroup.create_task) runs against a [`TaskGroup`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.TaskGroup) that is inactive, the supplied coroutine gets closed, thereby avoiding a [`RuntimeWarning`](https://docs.python.org/3.14/library/exceptions.html#RuntimeWarning) complaining the coroutine was never awaited. (Contributed by Arthur Tacca and Jason Zhang in [gh-115957](https://github.com/python/cpython/issues/115957).)

- The function plus methods called `create_task` have gained a fresh `**kwargs` argument forwarded straight to the task constructor. That addition slipped in accidentally during 3.13.3 and broke the API contract for custom task factories. A number of third-party task factories shipped workarounds to cope. Starting with 3.13.4 the prior factory contract is respected once more (right up until 3.14). So those workarounds keep functioning, the extra `**kwargs` argument continues to permit forwarding more keyword arguments to [`Task`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task) along with custom task factories.

The affected function and methods are these: [`asyncio.create_task()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.create_task), [`asyncio.loop.create_task()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_task), [`asyncio.TaskGroup.create_task()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.TaskGroup.create_task). (Contributed by Thomas Grainger in [gh-128307](https://github.com/python/cpython/issues/128307).)

[Subject index](INDEX.md) · [Previous source section](ast.md) · [Next source section](base64.md) · [Release/subject declaration](summary-release-highlights.md)
