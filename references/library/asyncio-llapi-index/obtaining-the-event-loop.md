# Obtaining the Event Loop

### Obtaining the Event Loop

| `asyncio.get_running_loop()` | The **preferred** function to get the running event loop. |
| --- | --- |
| `asyncio.get_event_loop()` | Get an event loop instance (running or current via the current policy). |
| `asyncio.set_event_loop()` | Set the event loop as current via the current policy. |
| `asyncio.new_event_loop()` | Create a new event loop. |

Examples

- [Using asyncio.get_running_loop()](https://docs.python.org/3.14/library/asyncio-future.html#asyncio-example-future).

[Subject index](INDEX.md) · [Previous](low-level-api-index.md) · [Continue](event-loop-methods-loop-stop-to-loop-get-task-factory.md)
