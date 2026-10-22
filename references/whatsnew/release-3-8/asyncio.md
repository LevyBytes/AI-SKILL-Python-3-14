# What’s New In Python 3.8 / asyncio — asyncio-eventloop, asyncio-exceptions, asyncio-runner, asyncio-task, concurrent.futures

> (Contributed by Guido van Rossum in [bpo-35766](https://bugs.python.org/issue?@action=redirect&bpo=35766).)

### asyncio

The [`asyncio.run()`](https://docs.python.org/3.14/library/asyncio-runner.html#asyncio.run) call has moved out of provisional status into the stable API. You can lean on it to drive a [coroutine](https://docs.python.org/3.14/glossary.html#term-coroutine) and hand back its result while the event loop gets managed for you automatically. As one illustration:

```python
import asyncio

async def main():
    await asyncio.sleep(0)
    return 42

asyncio.run(main())

```

That stands *roughly* on par with:

```python
import asyncio

async def main():
    await asyncio.sleep(0)
    return 42

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
try:
    loop.run_until_complete(main())
finally:
    asyncio.set_event_loop(None)
    loop.close()

```

Under the hood the real code is considerably more involved. For that reason, [`asyncio.run()`](https://docs.python.org/3.14/library/asyncio-runner.html#asyncio.run) ought to be how you favor launching asyncio programs.

> (Contributed by Yury Selivanov in [bpo-32314](https://bugs.python.org/issue?@action=redirect&bpo=32314).)

Invoking `python -m asyncio` brings up a REPL that is async by nature. That lets you experiment quickly with snippets carrying a top-level [`await`](https://docs.python.org/3.14/reference/expressions.html#await). You no longer have to invoke `asyncio.run()` yourself, which used to stand up a brand-new event loop on each call:

```none
$ python -m asyncio
asyncio REPL 3.8.0
Use "await" directly instead of "asyncio.run()".
Type "help", "copyright", "credits" or "license" for more information.
>>> import asyncio
>>> await asyncio.sleep(10, result='hello')
hello

```

> (Contributed by Yury Selivanov in [bpo-37028](https://bugs.python.org/issue?@action=redirect&bpo=37028).)

The [`asyncio.CancelledError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.CancelledError) exception now descends from [`BaseException`](https://docs.python.org/3.14/library/exceptions.html#BaseException) instead of [`Exception`](https://docs.python.org/3.14/library/exceptions.html#Exception), and it has stopped descending from [`concurrent.futures.CancelledError`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.CancelledError).
> (Contributed by Yury Selivanov in [bpo-32528](https://bugs.python.org/issue?@action=redirect&bpo=32528).)

Under Windows, [`ProactorEventLoop`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.ProactorEventLoop) now serves as the default event loop.
> (Contributed by Victor Stinner in [bpo-34687](https://bugs.python.org/issue?@action=redirect&bpo=34687).)

UDP is now handled as well by [`ProactorEventLoop`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.ProactorEventLoop).
> (Contributed by Adam Meily and Andrew Svetlov in [bpo-29883](https://bugs.python.org/issue?@action=redirect&bpo=29883).)

A [`KeyboardInterrupt`](https://docs.python.org/3.14/library/exceptions.html#KeyboardInterrupt) ("CTRL+C") may now break into [`ProactorEventLoop`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.ProactorEventLoop).
> (Contributed by Vladimir Matveev in [bpo-23057](https://bugs.python.org/issue?@action=redirect&bpo=23057).)

A new [`asyncio.Task.get_coro()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task.get_coro) lets you fetch the coroutine wrapped inside an [`asyncio.Task`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task).
> (Contributed by Alex Grönholm in [bpo-36999](https://bugs.python.org/issue?@action=redirect&bpo=36999).)

You may now hand asyncio tasks a name: supply the `name` keyword to either [`asyncio.create_task()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.create_task) or the event loop's [`create_task()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_task) method, or invoke [`set_name()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task.set_name) on the task itself. That name shows up in the `repr()` rendering of an [`asyncio.Task`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task) and is fetchable through the [`get_name()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task.get_name) method too.
> (Contributed by Alex Grönholm in [bpo-34270](https://bugs.python.org/issue?@action=redirect&bpo=34270).)

[Happy Eyeballs](https://en.wikipedia.org/wiki/Happy_Eyeballs) backing is now wired into [`asyncio.loop.create_connection()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_connection). Two fresh parameters let you tune the behavior: *happy_eyeballs_delay* alongside *interleave*. By trying both stacks at once, the Happy Eyeballs algorithm sharpens responsiveness for apps that run over IPv4 and IPv6.

[Subject index](INDEX.md) · [Previous source section](ast.md) · [Next source section](builtins.md) · [Release/subject declaration](assignment-expressions.md)
