# Event Loop Policies

### Event Loop Policies

A low-level mechanism for changing how functions such as [`asyncio.get_event_loop()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.get_event_loop) behave is what Policies provide. For more, you can also look at the primary [policies section](https://docs.python.org/3.14/library/asyncio-policy.html#asyncio-policies).

Accessing Policies

| `asyncio.get_event_loop_policy()` | Return the current process-wide policy. |
| --- | --- |
| `asyncio.set_event_loop_policy()` | Set a new process-wide policy. |
| `AbstractEventLoopPolicy` | Base class for policy objects. |

[Subject index](INDEX.md) · [Previous](protocols.md) · [Continue](../asyncio-platforms/platform-support.md)
