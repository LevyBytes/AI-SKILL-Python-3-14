# asyncio - Running Blocking Code

### Running Blocking Code

Don’t invoke blocking, CPU-bound code straight away. Picture a function grinding through a CPU-heavy computation for 1 second: every concurrent asyncio Task and IO operation would be held up by that same 1 second.

You can hand a task to an executor so it runs on a different thread — even a different interpreter, or a whole separate process — and thereby keep the OS thread carrying the event loop free. Look to the [`loop.run_in_executor()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.run_in_executor) method for the finer points.

[Subject index](INDEX.md) · [Previous](concurrency-and-multithreading.md) · [Continue](logging.md)
