# `concurrent.futures` ? Launching parallel tasks

### `concurrent.futures` - Launching parallel tasks

Added in version 3.2.

**Source code:** [Lib/concurrent/futures/thread.py](https://github.com/python/cpython/tree/3.14/Lib/concurrent/futures/thread.py), [Lib/concurrent/futures/process.py](https://github.com/python/cpython/tree/3.14/Lib/concurrent/futures/process.py), and [Lib/concurrent/futures/interpreter.py](https://github.com/python/cpython/tree/3.14/Lib/concurrent/futures/interpreter.py)

---

A high-level API for running callables asynchronously is what the `concurrent.futures` module offers.

You can carry out that asynchronous execution either on threads ? through `ThreadPoolExecutor` or `InterpreterPoolExecutor` ? or on distinct processes, through `ProcessPoolExecutor`. They all expose one shared interface, declared by the abstract `Executor` class.

Take care not to mix up `concurrent.futures.Future` with [`asyncio.Future`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.Future); the latter exists to support [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) tasks and coroutines. For a thorough side-by-side of the pair, consult the [asyncio's Future](https://docs.python.org/3.14/library/asyncio-future.html) documentation.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not WASI.

On WebAssembly this module is either non-functional or simply absent. Consult [WebAssembly platforms](https://docs.python.org/3.14/library/intro.html#wasm-availability) for additional detail.

[Subject index](INDEX.md) · [Continue](concurrent-futures-executor-class.md)
