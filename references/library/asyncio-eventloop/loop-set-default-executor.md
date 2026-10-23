# Executing code in thread or process pools

### Executing code in thread or process pools

 *awaitable *loop.run_in_executor(*executor*, *func*, **args*)

Schedule *func* to execute inside the given executor, forwarding *args* to it as positional arguments.

You pass an [`concurrent.futures.Executor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.Executor) instance through the *executor* parameter. When *executor* is `None`, the default executor takes over. That default may be assigned through `loop.set_default_executor()`; failing that, a [`concurrent.futures.ThreadPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor) is created on demand and reused by `run_in_executor()` whenever required.

Example:

The complete program is in the [upstream source](https://docs.python.org/3.14/library/asyncio-eventloop.html#executing-code-in-thread-or-process-pools).

Option 3 needs the entry point guard (`if __name__ == '__main__'`) because of the quirks of [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing), the machinery underlying [`ProcessPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor). Consult [Safe importing of main module](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing-safe-main-import).

The call hands back a [`asyncio.Future`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.Future) object.

Apply [`functools.partial()`](https://docs.python.org/3.14/library/functools.html#functools.partial) when *func* needs keyword arguments supplied to it.

Changed in version 3.5.3: `loop.run_in_executor()` stopped setting `max_workers` on the thread pool executor it builds; choosing that default is now left entirely to the thread pool executor ([`ThreadPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor)) itself.

 loop.set_default_executor(*executor*)

Register *executor* as the default that `run_in_executor()` will rely on. The supplied *executor* has to be a [`ThreadPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor) instance, a category that also covers [`InterpreterPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.InterpreterPoolExecutor).

Changed in version 3.11: *executor* must be an instance of [`ThreadPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor).

[Subject index](INDEX.md) · [Previous](loop-remove-signal-handler.md) · [Continue](loop-set-exception-handler-to-loop-call-exception-handler.md)
