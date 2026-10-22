# asyncio.llapi.index: Event-loop lifecycle, scheduling and task-factory routes

### Event Loop Methods

You can also consult the principal documentation section covering the [Event loop methods](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio-event-loop-methods).

Lifecycle

| `loop.run_until_complete()` | Run a Future/Task/awaitable until complete. |
| --- | --- |
| `loop.run_forever()` | Run the event loop forever. |
| `loop.stop()` | Stop the event loop. |
| `loop.close()` | Close the event loop. |
| `loop.is_running()` | Return `True` if the event loop is running. |
| `loop.is_closed()` | Return `True` if the event loop is closed. |
| `await` `loop.shutdown_asyncgens()` | Close asynchronous generators. |

Debugging

| `loop.set_debug()` | Enable or disable the debug mode. |
| --- | --- |
| `loop.get_debug()` | Get the current debug mode. |

Scheduling Callbacks

| `loop.call_soon()` | Invoke a callback soon. |
| --- | --- |
| `loop.call_soon_threadsafe()` | A thread-safe variant of `loop.call_soon()`. |
| `loop.call_later()` | Invoke a callback *after* the given time. |
| `loop.call_at()` | Invoke a callback *at* the given time. |

Thread/Interpreter/Process Pool

| `await` `loop.run_in_executor()` | Run a CPU-bound or other blocking function in a `concurrent.futures` executor. |
| --- | --- |
| `loop.set_default_executor()` | Set the default executor for `loop.run_in_executor()`. |

Tasks and Futures

| `loop.create_future()` | Create a `Future` object. |
| --- | --- |
| `loop.create_task()` | Schedule coroutine as a `Task`. |
| `loop.set_task_factory()` | Set a factory used by `loop.create_task()` to create `Tasks`. |
| `loop.get_task_factory()` | Get the factory `loop.create_task()` uses to create `Tasks`. |

[Subject index](INDEX.md) · [Previous](obtaining-the-event-loop.md) · [Continue](event-loop-connection-and-handler-methods.md)
