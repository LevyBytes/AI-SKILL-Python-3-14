# sys.monitoring — The STOP_ITERATION event

### The STOP_ITERATION event

[**PEP 380**](https://peps.python.org/pep-0380/#use-of-stopiteration-to-return-values) lays down that a [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration) exception gets raised on returning a value out of a generator or coroutine. That said, this is a deeply inefficient way to return a value, so certain Python implementations — CPython 3.12+ in particular — skip raising an exception unless other code would see it.

So that tools can watch for genuine exceptions while leaving generators and coroutines unhindered, the `STOP_ITERATION` event is supplied. Unlike `RAISE`, `STOP_ITERATION` can be switched off locally.

Be aware that the `STOP_ITERATION` event and the `RAISE` event for a [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration) exception amount to the same thing and are handled interchangeably when events are produced. For performance reasons implementations will lean toward `STOP_ITERATION`, though they may emit a `RAISE` event carrying a `StopIteration`.

[Subject index](INDEX.md) · [Previous](other-events.md) · [Continue](turning-events-on-and-off.md) · [Owning module, declaration or section: sys.monitoring](sys-monitoring-execution-event-monitoring.md)
