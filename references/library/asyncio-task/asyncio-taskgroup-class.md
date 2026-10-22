# asyncio.task: `asyncio.TaskGroup`

### Task groups

A task group brings together an interface for creating tasks alongside a dependable, convenient mechanism for awaiting the completion of every task in that group.

 *class *asyncio.TaskGroup

An [asynchronous context manager](https://docs.python.org/3.14/reference/datamodel.html#async-context-managers) that keeps a collection of tasks. Use `create_task()` to put tasks into the group. Upon the context manager's exit, every task is awaited.

Added in version 3.11.

[Subject index](INDEX.md) · [Previous](task-cancellation.md) · [Continue](asyncio-taskgroup-create-task.md)
