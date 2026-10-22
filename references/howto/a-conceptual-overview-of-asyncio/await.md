# await

### await

[`await`](https://docs.python.org/3.14/reference/expressions.html#await) is a Python keyword typically employed in one of two distinct ways:

```python
await task
await coroutine

```

In one essential respect, what `await` does hinges on the kind of object you await.

When you await a task, control is yielded from the current task or coroutine over to the event loop. While giving up control, a couple of noteworthy things take place. The following code sample will help us walk through it:

```python
async def plant_a_tree():
    dig_the_hole_task = asyncio.create_task(dig_the_hole())
    await dig_the_hole_task

    # Other instructions associated with planting a tree.
    ...

```

For this example, picture the event loop having handed control to the beginning of the coroutine `plant_a_tree()`. As shown above, the coroutine builds a task and then awaits it. That `await dig_the_hole_task` instruction appends a callback (one that will resume `plant_a_tree()`) onto the `dig_the_hole_task` object's list of callbacks. After that, the instruction yields control to the event loop. At some later point, the event loop hands control to `dig_the_hole_task`, and the task carries out whatever it must. When the task wraps up, it puts its assorted callbacks onto the event loop ? here, a call to resume `plant_a_tree()`.

In general terms, once the awaited task (`dig_the_hole_task`) finishes, the original task or coroutine (`plant_a_tree()`) gets placed back onto the event loop's to-do list so it can be resumed.

This serves as a simple yet dependable mental model. Realistically, the control handoffs are a touch more intricate, though not dramatically so. Part 2 will take you through the specifics that make it work.

**In contrast to tasks, when you await a coroutine no control is handed back to the event loop!** If you first wrap a coroutine in a task and then await that, control would be yielded. As it happens, `await coroutine` behaves essentially like calling an ordinary, synchronous Python function. Take this program:

```python
import asyncio

async def coro_a():
   print("I am coro_a(). Hi!")

async def coro_b():
   print("I am coro_b(). I sure hope no one hogs the event loop...")

async def main():
   task_b = asyncio.create_task(coro_b())
   num_repeats = 3
   for _ in range(num_repeats):
      await coro_a()
   await task_b

asyncio.run(main())

```

The opening statement of the coroutine `main()` builds `task_b` and queues it for execution via the event loop. After that, `coro_a()` gets awaited over and over. Control is never yielded to the event loop, and that is the reason we observe the output from all three `coro_a()` calls ahead of `coro_b()`?s output:

```none
I am coro_a(). Hi!
I am coro_a(). Hi!
I am coro_a(). Hi!
I am coro_b(). I sure hope no one hogs the event loop...

```

Should we swap `await coro_a()` for `await asyncio.create_task(coro_a())`, the behavior shifts. With that statement, the coroutine `main()` yields control to the event loop. The event loop then works through its backlog of work, running `task_b` followed by the task wrapping `coro_a()`, and only afterward resumes the coroutine `main()`.

```none
I am coro_b(). I sure hope no one hogs the event loop...
I am coro_a(). Hi!
I am coro_a(). Hi!
I am coro_a(). Hi!

```

The behavior of `await coroutine` can catch quite a few people off guard! That example shows how relying solely on `await coroutine` might accidentally seize control away from other tasks and end up stalling the event loop. [`asyncio.run()`](https://docs.python.org/3.14/library/asyncio-runner.html#asyncio.run) can assist you in spotting cases like this through the `debug=True` flag, which turns on [debug mode](https://docs.python.org/3.14/library/asyncio-dev.html#asyncio-debug-mode). Among its other behaviors, it will log any coroutines that keep execution to themselves for 100ms or more.

By design, this deliberately gives up a bit of conceptual tidiness in how `await` is used in exchange for better performance. Whenever a task is awaited, control has to travel the full length of the call stack up to the event loop. That may seem trivial, yet within a sizable program holding many `await` statements and a deep call stack, that cost can accumulate into a noticeable performance hit.

[Subject index](INDEX.md) · [Previous source context](tasks.md) · [Following source context](a-conceptual-overview-part-2-the-nuts-and-bolts.md)
