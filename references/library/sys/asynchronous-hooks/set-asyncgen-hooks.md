# sys.set_asyncgen_hooks

sys.set_asyncgen_hooks(*[firstiter] [, finalizer]*)

Accepts two optional keyword arguments that are callables taking an [asynchronous generator iterator](https://docs.python.org/3.14/glossary.html#term-asynchronous-generator-iterator) as an argument. The *firstiter* callable is invoked the first time an asynchronous generator is iterated. The *finalizer* is invoked when an asynchronous generator is about to be garbage collected.

Raises an auditing event `sys.set_asyncgen_hooks_firstiter` with no arguments.

Raises an auditing event `sys.set_asyncgen_hooks_finalizer` with no arguments.

Two auditing events are raised because the underlying API is made up of two calls, each of which must raise its own event.

Added in version 3.6: Consult [**PEP 525**](https://peps.python.org/pep-0525/) for further details; for a reference example of a *finalizer* method, look at how `asyncio.Loop.shutdown_asyncgens` is implemented within [Lib/asyncio/base_events.py](https://github.com/python/cpython/tree/3.14/Lib/asyncio/base_events.py)

Note

This function was added on a provisional basis (see [**PEP 411**](https://peps.python.org/pep-0411/) for details.)

[API family](INDEX.md) · [sys context index](../INDEX.md).
