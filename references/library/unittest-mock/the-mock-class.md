# unittest.mock: AsyncMock await arguments and await history

await_args

This is either `None` (when the mock has not yet been awaited) or the arguments supplied to the most recent await. Behaves just like `Mock.call_args`.

```python
>>> mock = AsyncMock()
>>> async def main(*args):
...     await mock(*args)
...
>>> mock.await_args
>>> asyncio.run(main('foo'))
>>> mock.await_args
call('foo')
>>> asyncio.run(main('bar'))
>>> mock.await_args
call('bar')

```

 await_args_list

This holds every await directed at the mock object in order (so its length equals how many times the mock has been awaited). It starts as an empty list until the first await occurs.

```python
>>> mock = AsyncMock()
>>> async def main(*args):
...     await mock(*args)
...
>>> mock.await_args_list
[]
>>> asyncio.run(main('foo'))
>>> mock.await_args_list
[call('foo')]
>>> asyncio.run(main('bar'))
>>> mock.await_args_list
[call('foo'), call('bar')]

```

[Subject index](INDEX.md) · [Previous](async-mock-await-history-and-reset.md) · [Continue](threading-mock-waiting-for-calls.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md) · [Owning module, declaration or section: unittest.mock.AsyncMock](unittest-mock-asyncmock-class.md) · [Owning module, declaration or section: The Mock Class](unittest-mock-mock-class.md)
