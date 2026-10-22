# Python 3.13.0 alpha 3 / core and builtins / inspect

[gh-111058](https://github.com/python/cpython/issues/111058): Make coro.cr_frame/gen.gi_frame yield `None` once the coroutine/generator has closed. That corrects a defect under which [`getcoroutinestate()`](https://docs.python.org/3.14/library/inspect.html#inspect.getcoroutinestate) and [`getgeneratorstate()`](https://docs.python.org/3.14/library/inspect.html#inspect.getgeneratorstate) hand back the wrong state on a closed coroutine/generator.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
