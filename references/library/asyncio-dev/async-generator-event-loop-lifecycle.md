# asyncio - Create asynchronous generators only when the event loop is running

### Create asynchronous generators only when the event loop is running

The advice is to hold off building [asynchronous generators](https://docs.python.org/3.14/glossary.html#term-asynchronous-generator-iterator) until the event loop itself exists.

So that asynchronous generators shut down dependably, the event loop registers callback functions through the [`sys.set_asyncgen_hooks()`](https://docs.python.org/3.14/library/sys.html#sys.set_asyncgen_hooks) function. Those callbacks revise the roster of running asynchronous generators, holding it in a consistent state.

A call to the [`loop.shutdown_asyncgens()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.shutdown_asyncgens) function brings the running generators to a graceful halt and empties the list.

On its very first iteration, the asynchronous generator fires the matching system hook. In that same moment the generator notes that the hook has fired and refrains from firing it a second time.

It follows that, if iteration kicks off before the event loop exists, the event loop can’t enroll the generator on its roster of active generators, since the hooks are installed only after the generator already tried to call them. As a result, the event loop has no way to shut that generator down should it need to.

Take the following example:

```python
import asyncio

async def agenfn():
    try:
        yield 10
    finally:
        await asyncio.sleep(0)

with asyncio.Runner() as runner:
    agen = agenfn()
    print(runner.run(anext(agen)))
    del agen

```

Output:

```python
10
Exception ignored while closing generator <async_generator object agenfn at 0x000002F71CD10D70>:
Traceback (most recent call last):
  File "example.py", line 13, in <module>
    del agen
        ^^^^
RuntimeError: async generator ignored GeneratorExit

```

Here is how to put this example right:

```python
import asyncio

async def agenfn():
    try:
        yield 10
    finally:
        await asyncio.sleep(0)

async def main():
    agen = agenfn()
    print(await anext(agen))
    del agen

asyncio.run(main())

```

[Subject index](INDEX.md) · [Previous](close-asynchronous-generators-explicitly.md) · [Continue](avoid-concurrent-iteration-and-closure-of-the-same-generator.md)
