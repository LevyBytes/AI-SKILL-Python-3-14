# asyncio — Tasks

### Tasks

Helpers for launching asyncio programs, spawning Tasks, and awaiting several things at once under timeouts.

| `run()` | Create event loop, run a coroutine, close the loop. |
| --- | --- |
| `Runner` | A context manager that eases making several async function calls. |
| `Task` | Task object. |
| `TaskGroup` | A context manager wrapping a group of tasks. It gives you a handy, dependable way to block until every task it holds has finished. |
| `create_task()` | Kick off an asyncio Task and hand it back. |
| `current_task()` | Return the current Task. |
| `all_tasks()` | Give back every task tied to an event loop that hasn’t completed yet. |
| `await` `sleep()` | Sleep for a number of seconds. |
| `await` `gather()` | Schedule and wait for things concurrently. |
| `await` `wait_for()` | Run with a timeout. |
| `await` `shield()` | Shield from cancellation. |
| `await` `wait()` | Monitor for completion. |
| `timeout()` | Run under a timeout. Handy for the situations where `wait_for` doesn’t fit. |
| `to_thread()` | Run a function asynchronously over on its own OS thread. |
| `run_coroutine_threadsafe()` | Schedule a coroutine from another OS thread. |
| `for in` `as_completed()` | Track completion through a `for` loop. |

Examples

- [Using asyncio.gather() to run things in parallel](https://docs.python.org/3.14/library/asyncio-task.html#asyncio-example-gather).

- [Using asyncio.wait_for() to enforce a timeout](https://docs.python.org/3.14/library/asyncio-task.html#asyncio-example-waitfor).

- [Cancellation](https://docs.python.org/3.14/library/asyncio-task.html#asyncio-example-task-cancel).

- [Using asyncio.sleep()](https://docs.python.org/3.14/library/asyncio-task.html#asyncio-example-sleep).

- See also the main [Tasks documentation page](https://docs.python.org/3.14/library/asyncio-task.html#coroutine).

[Subject index](INDEX.md) · [Previous](high-level-api-index.md) · [Continue](queues.md)
