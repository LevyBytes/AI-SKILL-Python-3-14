# asyncio — Avoid concurrent iteration and closure of the same generator

### Avoid concurrent iteration and closure of the same generator

An async generator can be re-entered even as another [`__anext__()`](https://docs.python.org/3.14/reference/expressions.html#agen.__anext__) / [`athrow()`](https://docs.python.org/3.14/reference/expressions.html#agen.athrow) / [`aclose()`](https://docs.python.org/3.14/reference/expressions.html#agen.aclose) call has yet to finish. Doing so can throw the async generator into an inconsistent state and bring on errors.

Let’s walk through the example below:

```python
import asyncio

async def consumer():
    for idx in range(100):
        await asyncio.sleep(0)
        message = yield idx
        print('received', message)

async def amain():
    agenerator = consumer()
    await agenerator.asend(None)

    fa = asyncio.create_task(agenerator.asend('A'))
    fb = asyncio.create_task(agenerator.asend('B'))
    await fa
    await fb

asyncio.run(amain())

```

Output:

```python
received A
Traceback (most recent call last):
  File "test.py", line 38, in <module>
    asyncio.run(amain())
    ~~~~~~~~~~~^^^^^^^^^
  File "Lib/asyncio/runners.py", line 204, in run
    return runner.run(main)
           ~~~~~~~~~~^^^^^^
  File "Lib/asyncio/runners.py", line 127, in run
    return self._loop.run_until_complete(task)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^
  File "Lib/asyncio/base_events.py", line 719, in run_until_complete
    return future.result()
           ~~~~~~~~~~~~~^^
  File "test.py", line 36, in amain
    await fb
RuntimeError: anext(): asynchronous generator is already running

```

Given all that, the guidance is to steer clear of running asynchronous generators inside parallel tasks or spanning more than one event loop.

[Subject index](INDEX.md) · [Previous](async-generator-event-loop-lifecycle.md)
