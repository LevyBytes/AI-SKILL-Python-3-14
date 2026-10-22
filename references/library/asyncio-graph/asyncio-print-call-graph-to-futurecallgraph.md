# asyncio.graph: `asyncio.print_call_graph()`, `asyncio.format_call_graph()`, `asyncio.capture_call_graph()`, `FutureCallGraph()`

## Call Graph Introspection

### Call Graph Introspection

**Source code:** [Lib/asyncio/graph.py](https://github.com/python/cpython/tree/3.14/Lib/asyncio/graph.py)

---

asyncio ships capable runtime call-graph introspection tools that follow the full call graph of a *coroutine* or *task* in flight, or of a *future* that is parked. Both these tools and the machinery beneath them are callable from inside a Python program as well as by outside profilers and debuggers.

Added in version 3.14.

 asyncio.print_call_graph(*future=None*, */*, ***, *file=None*, *depth=1*, *limit=None*)

Emit the async call graph belonging to the current task, or to the [`Task`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task) or [`Future`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.Future) you hand it.

This function lists entries beginning at the topmost frame and proceeding downward toward the invocation point.

It accepts an optional *future* argument; leave it out and the task running right now is taken instead.

When the function runs against *the current task*, the optional keyword-only *depth* argument lets you drop the stated number of frames off the top of the stack.

Supplying the optional keyword-only *limit* argument trims every call stack in the produced graph down to no more than `abs(limit)` entries. A positive *limit* keeps the entries nearest the invocation point; a negative *limit* keeps the topmost ones; an omitted *limit* or one set to `None` keeps every entry; and a *limit* of `0` suppresses the call stack entirely, emitting only the “awaited by” details.

When *file* is left out or set to `None`, the function writes to [`sys.stdout`](https://docs.python.org/3.14/library/sys.html#sys.stdout).

**Example:**

The following Python code:

```python
import asyncio

async def test():
    asyncio.print_call_graph()

async def main():
    async with asyncio.TaskGroup() as g:
        g.create_task(test(), name='test')

asyncio.run(main())

```

will print:

```python
* Task(name='test', id=0x1039f0fe0)
+ Call stack:
|   File 't2.py', line 4, in async test()
+ Awaited by:
   * Task(name='Task-1', id=0x103a5e060)
      + Call stack:
      |   File 'taskgroups.py', line 107, in async TaskGroup.__aexit__()
      |   File 't2.py', line 7, in async main()

```

 asyncio.format_call_graph(*future=None*, */*, ***, *depth=1*, *limit=None*)

Behaves as `print_call_graph()` does, except it hands back a string. Where *future* is `None` and no current task exists, the function gives back an empty string.

 asyncio.capture_call_graph(*future=None*, */*, ***, *depth=1*, *limit=None*)

Grab the async call graph for the current task, or for the [`Task`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task) or [`Future`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.Future) you supply.

It accepts an optional *future* argument; leave it out and the task running right now is taken instead. Should no current task exist, the function gives back `None`.

When the function runs against *the current task*, the optional keyword-only *depth* argument lets you drop the stated number of frames off the top of the stack.

Gives back a `FutureCallGraph` data class object:

- `FutureCallGraph(future, call_stack, awaited_by)`

>

Here *future* points to a [`Future`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.Future) or a [`Task`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task) (or any of their subclasses.)

`call_stack` holds a tuple of `FrameCallGraphEntry` objects.

`awaited_by` holds a tuple of `FutureCallGraph` objects.

-

[Subject index](INDEX.md) · [Continue](framecallgraphentry.md)
