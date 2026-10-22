# concurrent.futures: `submit()`, `map()`, `shutdown()`

submit(*fn*, */*, **args*, ***kwargs*)

Queues the callable *fn* to run as `fn(*args, **kwargs)`, handing back a `Future` object that stands in for that callable's execution.

```python
with ThreadPoolExecutor(max_workers=1) as executor:
    future = executor.submit(pow, 323, 1235)
    print(future.result())

```

 map(*fn*, **iterables*, *timeout=None*, *chunksize=1*, *buffersize=None*)

Behaves much like [`map(fn, *iterables)`](https://docs.python.org/3.14/library/functions.html#map), with these distinctions:

- Rather than lazily, the *iterables* get gathered right away ? unless you pass a *buffersize* to cap how many submitted tasks may have outstanding, not-yet-yielded results. Once that buffer fills up, looping over the *iterables* halts until the buffer surrenders a result.

- The callable *fn* runs asynchronously, and multiple invocations of *fn* might proceed at the same time.

The iterator that comes back raises a [`TimeoutError`](https://docs.python.org/3.14/library/exceptions.html#TimeoutError) when [`__next__()`](https://docs.python.org/3.14/library/stdtypes.html#iterator.__next__) is invoked and no result has surfaced within *timeout* seconds measured from the initial `Executor.map()` call. You may give *timeout* as an int or a float. Leave *timeout* out or set it to `None`, and the wait is unbounded.

Should one of the *fn* invocations throw an exception, that exception surfaces at the moment its corresponding value is pulled from the iterator.

Under `ProcessPoolExecutor`, this method splits *iterables* into several chunks, each handed to the pool as its own task. You control the rough size of those chunks by giving *chunksize* a positive integer. When iterables are extremely long, a high *chunksize* can boost throughput noticeably over the default of 1. For `ThreadPoolExecutor` and `InterpreterPoolExecutor`, *chunksize* makes no difference.

Changed in version 3.5: Added the *chunksize* parameter.

Changed in version 3.14: Added the *buffersize* parameter.

 shutdown(*wait=True*, ***, *cancel_futures=False*)

Tell the executor to release whatever resources it holds once the futures still pending have finished. After shutdown, any `Executor.submit()` and `Executor.map()` invocation will raise [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError).

When *wait* is `True`, this call holds off returning until every pending future has finished and the executor's resources have been released. When *wait* is `False`, the call comes back at once, and the executor's resources are released only after all pending futures finish. No matter what *wait* is, the whole Python program stays alive until every pending future has run to completion.

When *cancel_futures* is `True`, this call cancels each pending future the executor hasn't yet begun executing. Futures already done or in progress stay untouched, no matter what *cancel_futures* is set to.

When *cancel_futures* and *wait* are both `True`, every future the executor has already begun executing finishes before this call returns. Whatever futures remain get cancelled.

Calling this method by hand becomes unnecessary if you treat the executor as a [context manager](https://docs.python.org/3.14/glossary.html#term-context-manager) through the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement, which shuts down the `Executor` (waiting just as though `Executor.shutdown()` had run with *wait* equal to `True`):

```python
import shutil
with ThreadPoolExecutor(max_workers=4) as e:
    e.submit(shutil.copy, 'src1.txt', 'dest1.txt')
    e.submit(shutil.copy, 'src2.txt', 'dest2.txt')
    e.submit(shutil.copy, 'src3.txt', 'dest3.txt')
    e.submit(shutil.copy, 'src4.txt', 'dest4.txt')

```

Changed in version 3.9: Added *cancel_futures*.

[Subject index](INDEX.md) · [Previous](concurrent-futures-executor-class.md) · [Continue](concurrent-futures-threadpoolexecutor-class.md) · [Owning module, declaration or section: concurrent.futures.Executor](concurrent-futures-executor-class.md) · [Owning module, declaration or section: Executor Objects](concurrent-futures-executor-class.md)
