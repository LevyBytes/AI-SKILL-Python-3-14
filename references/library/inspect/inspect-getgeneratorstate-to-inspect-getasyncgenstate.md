# inspect: `inspect.getgeneratorstate()`, `inspect.getcoroutinestate()`, `inspect.getasyncgenstate()`

### Current State of Generators, Coroutines, and Asynchronous Generators

When you are building coroutine schedulers, or otherwise pushing generators into advanced territory, it helps to know whether a generator is running right now, is paused awaiting its start or resumption, or has finished for good. `getgeneratorstate()` makes pinning down a generator’s present state straightforward.

 inspect.getgeneratorstate(*generator*)

Report the present state of a generator-iterator.

Possible states are:

- GEN_CREATED: Waiting to start execution.

- GEN_RUNNING: The interpreter is running it at present.

- GEN_SUSPENDED: Paused for now at a yield expression.

- GEN_CLOSED: Execution has completed.

Added in version 3.2.

 inspect.getcoroutinestate(*coroutine*)

Report the present state of a coroutine object. While the function is meant for coroutine objects produced by [`async def`](https://docs.python.org/3.14/reference/compound_stmts.html#async-def) functions, it will take any coroutine-like object exposing `cr_running` and `cr_frame` attributes.

Possible states are:

- CORO_CREATED: Waiting to start execution.

- CORO_RUNNING: The interpreter is actively executing it.

- CORO_SUSPENDED: Paused for the moment at an await expression.

- CORO_CLOSED: Execution has completed.

Added in version 3.5.

 inspect.getasyncgenstate(*agen*)

Report the present state of an asynchronous generator object. The function targets asynchronous iterator objects produced by [`async def`](https://docs.python.org/3.14/reference/compound_stmts.html#async-def) functions that employ the [`yield`](https://docs.python.org/3.14/reference/simple_stmts.html#yield) statement, yet it will take any asynchronous generator-like object exposing `ag_running` and `ag_frame` attributes.

Possible states are:

- AGEN_CREATED: Waiting to start execution.

- AGEN_RUNNING: Right now the interpreter is executing it.

- AGEN_SUSPENDED: Held in suspension at a yield expression.

- AGEN_CLOSED: Execution has completed.

Added in version 3.12.

You can likewise inspect the generator’s present internal state. That mainly comes in handy during testing, when you want to confirm the internal state is being refreshed the way it should be:

[Subject index](INDEX.md) · [Previous](inspect-getattr-static.md) · [Continue](inspect-getgeneratorlocals-to-inspect-getasyncgenlocals.md) · [Owning module, declaration or section: inspect](inspect-inspect-live-objects.md)
