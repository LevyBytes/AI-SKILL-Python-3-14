# Policies

## Policies

### Policies

Warning

Policies have been deprecated and are scheduled for removal in Python 3.16. We recommend reaching for the [`asyncio.run()`](https://docs.python.org/3.14/library/asyncio-runner.html#asyncio.run) function, or [`asyncio.Runner`](https://docs.python.org/3.14/library/asyncio-runner.html#asyncio.Runner) together with *loop_factory*, to select the loop implementation you want.

An event loop policy is a global object that handles getting and setting the current [event loop](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio-event-loop) and also creating fresh event loops. You can swap the default policy for built-in alternatives that bring in different event loop implementations, or replace it with a custom policy that overrides these behaviors.

For each *context*, the policy object gets and sets its own separate event loop. By default that means per-thread, although a custom policy might define *context* in some other way.

Custom event loop policies are able to govern how [`get_event_loop()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.get_event_loop), [`set_event_loop()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.set_event_loop), and [`new_event_loop()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.new_event_loop) behave.

The APIs declared in the `AbstractEventLoopPolicy` abstract base class are what policy objects ought to implement.

[Subject index](INDEX.md) · [Continue](global-event-loop-policy-access.md)
