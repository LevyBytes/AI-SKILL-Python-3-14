# Tasks

### Tasks

Broadly put, [tasks](https://docs.python.org/3.14/library/asyncio-task.html#asyncio-task-obj) are coroutines (not coroutine functions) bound to an event loop. On top of that, a task keeps a list of callback functions, the significance of which will become apparent shortly once we get to [`await`](https://docs.python.org/3.14/reference/expressions.html#await). Tasks are best created through [`asyncio.create_task()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.create_task).

Building a task schedules it for execution on its own (by placing a callback that runs it into the event loop's to-do list, that is, its collection of jobs).

On your behalf, `asyncio` ties tasks to the event loop automatically. That automatic linkage was a deliberate design choice in `asyncio` to keep things simple. Lacking it, you would need to hold onto the event loop object and forward it to every coroutine function that wishes to spawn tasks, piling needless clutter onto your code.

```python
coroutine = loudmouth_penguin(magic_number=5)
# This creates a Task object and schedules its execution via the event loop.
task = asyncio.create_task(coroutine)

```

Up above, we set up the event loop by hand and told it to run forever. Out in the real world, the advised (and frequently encountered) approach is [`asyncio.run()`](https://docs.python.org/3.14/library/asyncio-runner.html#asyncio.run), which handles the event loop for you and makes sure the supplied coroutine completes before moving on. As an illustration, plenty of async programs use this layout:

```python
import asyncio

async def main():
    # Perform all sorts of wacky, wild asynchronous things...
    ...

if __name__ == "__main__":
    asyncio.run(main())
    # The program will not reach the following print statement until the
    # coroutine main() finishes.
    print("coroutine main() is done!")

```

Keep in mind that the task itself never gets added to the event loop ? only a callback pointing to the task does. That detail matters when the task object you made happens to be garbage collected before the event loop ever calls it. As an example, look at this program:

```python
 1async def hello():
 2    print("hello!")
 3
 4async def main():
 5    asyncio.create_task(hello())
 6    # Other asynchronous instructions which run for a while
 7    # and cede control to the event loop...
 8    ...
 9
10asyncio.run(main())

```

Since nothing holds a reference to the task object made on line 5, it *might* get garbage collected before the event loop runs it. Subsequent instructions inside the coroutine `main()` give control back to the event loop so that it can run other jobs. By the time the event loop finally goes to run the task, it could fail and find that the task object is gone! The same can occur even when a coroutine does retain a reference to a task yet wraps up before that task is finished. As the coroutine exits, its local variables fall out of scope and can become candidates for garbage collection. Realistically, `asyncio` along with Python's garbage collector put in a fair amount of effort to keep this from happening. Still, that is no excuse to be careless!

[Subject index](INDEX.md) · [Previous source context](asynchronous-functions-and-coroutines.md) · [Following source context](await.md)
