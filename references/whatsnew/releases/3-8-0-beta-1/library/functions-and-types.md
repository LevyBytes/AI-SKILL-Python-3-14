# Python 3.8.0 beta 1 / library / functions and types

[bpo-23896](https://bugs.python.org/issue?@action=redirect&bpo=23896): Supplies lib2to3.pygram with a grammar treating exec as a callable function rather than a statement.

[bpo-36895](https://bugs.python.org/issue?@action=redirect&bpo=36895): Marked deprecated back in 3.3 with `time.perf_counter()` as the suggested replacement and slated to disappear in 3.8, the `time.clock()` function is now gone.

[bpo-36772](https://bugs.python.org/issue?@action=redirect&bpo=36772): Beyond its prior role as a function yielding a decorator, functools.lru_cache() may now also be applied directly as a decorator on its own.

[bpo-36542](https://bugs.python.org/issue?@action=redirect&bpo=36542): A Python function's signature can now be replaced by setting the `__text_signature__` attribute on it.

[bpo-35252](https://bugs.python.org/issue?@action=redirect&bpo=35252): Raises a TypeError rather than an AssertionError whenever singledispatch receives an invalid type annotation.

[bpo-35900](https://bugs.python.org/issue?@action=redirect&bpo=35900): Adds registration of a custom reduction callback for functions and classes inside _pickle.c by way of the Pickler's fresh `reducer_override` attribute

[bpo-36999](https://bugs.python.org/issue?@action=redirect&bpo=36999): Supplies the `asyncio.Task.get_coro()` method, exposing the tasks’s coroutine object publicly.

[bpo-36933](https://bugs.python.org/issue?@action=redirect&bpo=36933): The `sys.set_coroutine_wrapper` and `sys.get_coroutine_wrapper` functions, deprecated and slated for removal back in 3.8, are now gone.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
