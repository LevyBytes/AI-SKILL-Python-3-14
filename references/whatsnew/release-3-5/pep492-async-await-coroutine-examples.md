# What’s New In Python 3.5 / PEP 492 - Coroutines with async and await syntax — asyncio-eventloop

### New Features

### PEP 492 - Coroutines with async and await syntax

[**PEP 492**](https://peps.python.org/pep-0492/) substantially strengthens Python's facilities for writing asynchronous code by introducing [awaitable objects](https://docs.python.org/3.14/glossary.html#term-awaitable), [coroutine functions](https://docs.python.org/3.14/glossary.html#term-coroutine-function), [asynchronous iteration](https://docs.python.org/3.14/glossary.html#term-asynchronous-iterable), and [asynchronous context managers](https://docs.python.org/3.14/glossary.html#term-asynchronous-context-manager).

You declare coroutine functions with the new [`async def`](https://docs.python.org/3.14/reference/compound_stmts.html#async-def) syntax:

```python
>>> async def coro():
...     return 'spam'

```

Within a coroutine function, the fresh [`await`](https://docs.python.org/3.14/reference/expressions.html#await) expression lets you pause coroutine execution until a result becomes ready. Anything can be *awaited*, provided it satisfies the [awaitable](https://docs.python.org/3.14/glossary.html#term-awaitable) protocol through a definition of the [`__await__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__await__) method.

PEP 492 additionally introduces the [`async for`](https://docs.python.org/3.14/reference/compound_stmts.html#async-for) statement to make looping across asynchronous iterables convenient.

Here is a bare-bones HTTP client coded with the new syntax:

```python
import asyncio

async def http_get(domain):
    reader, writer = await asyncio.open_connection(domain, 80)

    writer.write(b'\r\n'.join([
        b'GET / HTTP/1.1',
        b'Host: %b' % domain.encode('latin-1'),
        b'Connection: close',
        b'', b''
    ]))

    async for line in reader:
        print('>>>', line)

    writer.close()

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(http_get('example.com'))
finally:
    loop.close()

```

In parallel with asynchronous iteration, a new syntax exists for asynchronous context managers as well. This script:

```python
import asyncio

async def coro(name, lock):
    print('coro {}: waiting for lock'.format(name))
    async with lock:
        print('coro {}: holding the lock'.format(name))
        await asyncio.sleep(1)
        print('coro {}: releasing the lock'.format(name))

loop = asyncio.get_event_loop()
lock = asyncio.Lock()
coros = asyncio.gather(coro(1, lock), coro(2, lock))
try:
    loop.run_until_complete(coros)
finally:
    loop.close()

```

will output:

```python
coro 2: waiting for lock
coro 2: holding the lock
coro 1: waiting for lock
coro 2: releasing the lock
coro 1: holding the lock
coro 1: releasing the lock

```

Bear in mind that [`async for`](https://docs.python.org/3.14/reference/compound_stmts.html#async-for) along with [`async with`](https://docs.python.org/3.14/reference/compound_stmts.html#async-with) are valid solely within a coroutine function that was declared using [`async def`](https://docs.python.org/3.14/reference/compound_stmts.html#async-def).

Coroutine functions are meant to execute inside a suitable event loop, for instance the [asyncio loop](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio-event-loop).

[Subject index](INDEX.md) · [Previous source section](summary-release-highlights.md) · [Next source section](pep-492-coroutines-with-async-and-await-syntax-note.md) · [Release/subject declaration](summary-release-highlights.md)
