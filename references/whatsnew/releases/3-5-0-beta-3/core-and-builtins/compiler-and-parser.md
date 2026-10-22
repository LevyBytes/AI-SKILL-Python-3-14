# Python 3.5.0 beta 3 / core and builtins / compiler and parser

[bpo-24400](https://bugs.python.org/issue?@action=redirect&bpo=24400): Bring in a separate type for [**PEP 492**](https://peps.python.org/pep-0492/) coroutines; add types.CoroutineType, inspect.getcoroutinestate, inspect.getcoroutinelocals; the CO_GENERATOR flag is dropped from coroutines; sys.set_coroutine_wrapper applies only to "async def" coroutines; inspect.iscoroutine drops its reliance on collections.abc.Coroutine and is meant only to detect pure "async def" coroutines; add a new opcode GET_YIELD_FROM_ITER; the generator wrapper produced by types.coroutine is corrected so that collections.abc.Generator counts it as an instance; for spotting generator-based coroutines, collections.abc.Awaitable along with collections.abc.Coroutine will no longer do the job — reach for inspect.isawaitable instead.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
