# Scheduling delayed callbacks

### Scheduling delayed callbacks

The event loop supplies ways to queue callback functions for execution at a later moment. To keep track of time, the event loop relies on monotonic clocks.

 loop.call_later(*delay*, *callback*, **args*, *context=None*)

Schedule *callback* so that it runs once the supplied *delay* count of seconds has elapsed (either an int or a float will do).

You get back an `asyncio.TimerHandle` instance that lets you cancel the callback.

*callback* runs exactly one time. Should two callbacks be queued for precisely the same instant, the sequence in which they run is undefined.

When the callback fires, the optional positional *args* are handed to it. Reach for [`functools.partial()`](https://docs.python.org/3.14/library/functools.html#functools.partial) when you need to deliver keyword arguments to *callback*.

Through an optional keyword-only *context* argument you can designate a custom [`contextvars.Context`](https://docs.python.org/3.14/library/contextvars.html#contextvars.Context) in which the *callback* runs. When none is supplied, the current context applies.

Note

For performance reasons, callbacks queued via `loop.call_later()` might fire as much as one clock-resolution ahead of schedule (see `time.get_clock_info('monotonic').resolution`).

Changed in version 3.7: Introduced the keyword-only *context* parameter. Consult [**PEP 567**](https://peps.python.org/pep-0567/) for further details.

Changed in version 3.8: Under the default event loop implementation on Python 3.7 and before, *delay* was capped at one day; Python 3.8 lifted that restriction.

 loop.call_at(*when*, *callback*, **args*, *context=None*)

Schedule *callback* so that it fires at the supplied absolute timestamp *when* (an int or a float), measured against the same clock as `loop.time()`.

The way this method behaves matches `call_later()`.

You get back an `asyncio.TimerHandle` instance that lets you cancel the callback.

Note

For performance reasons, callbacks queued via `loop.call_at()` might fire as much as one clock-resolution ahead of schedule (see `time.get_clock_info('monotonic').resolution`).

Changed in version 3.7: Introduced the keyword-only *context* parameter. Consult [**PEP 567**](https://peps.python.org/pep-0567/) for further details.

Changed in version 3.8: Under the default event loop implementation on Python 3.7 and before, the gap between *when* and the present time was capped at one day; Python 3.8 lifted that restriction.

 loop.time()

Give back the present time as a [`float`](https://docs.python.org/3.14/library/functions.html#float), measured by the monotonic clock that the event loop keeps internally.

Note

Changed in version 3.8: On Python 3.7 and before, timeouts (a relative *delay* or an absolute *when*) were not to run beyond one day; Python 3.8 lifted that restriction.

See also

The [`asyncio.sleep()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.sleep) function.

[Subject index](INDEX.md) · [Previous](loop-call-soon-to-loop-call-soon-threadsafe.md) · [Continue](loop-create-future-to-loop-get-task-factory.md)
