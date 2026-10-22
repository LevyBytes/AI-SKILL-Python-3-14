# Future completion, waiting and executor errors

Invoking this is reserved for `Executor` subclasses, which call it ahead of running the task tied to the `Future`, and for test code.

A `False` return value signals that the `Future` got cancelled — that is, someone invoked `Future.cancel()` and got back `True`. Whatever threads sit blocked on the `Future` reaching completion (for instance via `as_completed()` or `wait()`) get notified.

A `True` return value signals that no cancellation happened and the `Future` has now entered the running phase; from this point `Future.running()` reports `True`.

You may invoke this at most one time, and never once `Future.set_result()` or `Future.set_exception()` has already run.

`set_result(*result*)`

Records *result* as the outcome of the task tied to the `Future`.

Reserve this for `Executor` subclasses and for test code.

Changed in version 3.8: A `concurrent.futures.InvalidStateError` now gets thrown here whenever the `Future` has already finished.

`set_exception(*exception*)`

Records the [`Exception`](https://docs.python.org/3.14/library/exceptions.html#Exception) *exception* as the outcome of the task tied to the `Future`.

Reserve this for `Executor` subclasses and for test code.

Changed in version 3.8: A `concurrent.futures.InvalidStateError` now gets thrown here whenever the `Future` has already finished.

### Module Functions

`concurrent.futures.wait(*fs*, *timeout=None*, *return_when=ALL_COMPLETED*)`

Blocks until the `Future` objects passed as *fs* (which may originate from distinct `Executor` instances) have finished. Should *fs* contain repeated futures, the duplicates are dropped so each appears a single time in the output. The return is a named 2-tuple holding two sets. Its first member, `done`, gathers the futures that wrapped up (whether they finished or were cancelled) prior to the wait ending. Its second member, `not_done`, gathers those still outstanding (pending or running).

Supply *timeout* to cap how many seconds the call blocks before it gives up. An int or a float both work for *timeout*. Leaving *timeout* out, or passing `None`, removes any ceiling on the wait time.

The *return_when* argument selects the condition under which the call hands control back. Pick exactly one of these constants:

| Constant | Description |
| --- | --- |
| concurrent.futures.FIRST_COMPLETED | Hand control back as soon as one of the futures wraps up or gets cancelled. |
| concurrent.futures.FIRST_EXCEPTION | Hand control back the moment a future ends by throwing. Should none of them throw, the behaviour matches `ALL_COMPLETED`. |
| concurrent.futures.ALL_COMPLETED | Hold off returning until every future has either completed or been cancelled. |

`concurrent.futures.as_completed(*fs*, *timeout=None*)`

Hands back an iterator across the `Future` objects named by *fs* (which may come from separate `Executor` instances), surfacing each one at the point it wraps up (finished or cancelled). Repeated entries within *fs* surface a single time. Whichever futures had already wrapped up by the time `as_completed()` runs come out at the front. That iterator throws a [`TimeoutError`](https://docs.python.org/3.14/library/exceptions.html#TimeoutError) whenever [`__next__()`](https://docs.python.org/3.14/library/stdtypes.html#iterator.__next__) runs and, *timeout* seconds on from the initial `as_completed()` invocation, no result has surfaced yet. An int or a float both serve for *timeout*. Omitting *timeout* or handing it `None` lifts the cap on wait time.

See also

[**PEP 3148**](https://peps.python.org/pep-3148/) – futures - execute computations asynchronously

The write-up that put forward adding this capability to Python's standard library.

### Exception classes

`*exception *concurrent.futures.CancelledError`

Thrown once a future has been cancelled.

`*exception *concurrent.futures.TimeoutError`

A retired alias for `TimeoutError`; thrown once a future's operation runs past the timeout it was given.

Changed in version 3.11: This class was made an alias of `TimeoutError`.

`*exception *concurrent.futures.BrokenExecutor`

Subclasses [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError); thrown once an executor has broken somehow and can no longer accept or run further tasks.

Added in version 3.7.

`*exception *concurrent.futures.InvalidStateError`

Thrown once an action gets attempted on a future that its present state does not permit.

Added in version 3.8.

`*exception *concurrent.futures.thread.BrokenThreadPool`

Subclasses `BrokenExecutor`; thrown once a worker belonging to a `ThreadPoolExecutor` could not finish starting up.

Added in version 3.7.

`*exception *concurrent.futures.interpreter.BrokenInterpreterPool`

Subclasses `BrokenThreadPool`; thrown once a worker belonging to an `InterpreterPoolExecutor` could not finish starting up.

Added in version 3.14.

`*exception *concurrent.futures.process.BrokenProcessPool`

Subclasses `BrokenExecutor` (which earlier was [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError)); thrown once a worker belonging to a `ProcessPoolExecutor` has stopped in an unclean way — say, after being killed by something external.

Added in version 3.3.

[Subject index](INDEX.md)
