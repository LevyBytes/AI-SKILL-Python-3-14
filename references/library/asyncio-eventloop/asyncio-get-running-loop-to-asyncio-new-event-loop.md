# Event loop

### Event loop

**Source code:** [Lib/asyncio/events.py](https://github.com/python/cpython/tree/3.14/Lib/asyncio/events.py), [Lib/asyncio/base_events.py](https://github.com/python/cpython/tree/3.14/Lib/asyncio/base_events.py)

---

Preface

Every asyncio application is built around an event loop at its center. These loops drive asynchronous callbacks and tasks, carry out network IO, and launch subprocesses.

Most application authors will rely on the high-level asyncio entry points, like [`asyncio.run()`](https://docs.python.org/3.14/library/asyncio-runner.html#asyncio.run), and will seldom have a reason to touch the loop object directly or invoke its methods. The material here is aimed primarily at people writing lower-level code, libraries, and frameworks who require tighter control over how the loop behaves.

Obtaining the Event Loop

To get, set, or create an event loop, the low-level helpers below are available:

 asyncio.get_running_loop()

Return the running event loop in the current OS thread.

Raise a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) if there is no running event loop.

Only a coroutine or a callback may invoke this function.

Added in version 3.7.

 asyncio.get_event_loop()

Get the current event loop.

Invoked from within a coroutine or a callback (for instance one queued through call_soon or a comparable API), this function always hands back the running event loop.

When no running event loop has been set, the function instead returns whatever the `get_event_loop_policy().get_event_loop()` call yields.

Given that this function carries fairly intricate semantics (most notably when custom event loop policies are active), prefer the `get_running_loop()` function over `get_event_loop()` inside coroutines and callbacks.

Per the earlier remark, lean on the higher-level [`asyncio.run()`](https://docs.python.org/3.14/library/asyncio-runner.html#asyncio.run) function rather than wiring up and tearing down an event loop by hand with these lower level helpers.

Changed in version 3.14: Now raises a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) whenever no current event loop exists.

Note

Scheduled for removal in Python 3.16, the `asyncio` policy system is now deprecated; once that happens, this function will hand back the currently running event loop when one exists, otherwise the loop registered via `set_event_loop()`.

 asyncio.set_event_loop(*loop*)

Set *loop* as the current event loop for the current OS thread.

 asyncio.new_event_loop()

Create and return a new event loop object.

Keep in mind that how the `get_event_loop()`, `set_event_loop()`, and `new_event_loop()` functions behave can be changed by [setting a custom event loop policy](https://docs.python.org/3.14/library/asyncio-policy.html#asyncio-policies).

Contents

The sections that make up this documentation page are:

- The Event Loop Methods section serves as the reference documentation for the event loop APIs;

- The Callback Handles section covers the `Handle` and `TimerHandle` instances handed back by scheduling methods such as `loop.call_soon()` and `loop.call_later()`;

- The Server Objects section covers the types handed back by event loop methods like `loop.create_server()`;

- The Event Loop Implementations section covers the `SelectorEventLoop` and `ProactorEventLoop` classes;

- The Examples section demonstrates how several event loop APIs are used.

[Subject index](INDEX.md) · [Continue](event-loop-methods.md)
