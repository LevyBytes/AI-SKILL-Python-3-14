# unittest.mock.AsyncMock: `assert_any_await()`, `assert_has_awaits()`, `assert_not_awaited()`, `reset_mock()`

assert_any_await(**args*, ***kwargs*)

Assert the mock was awaited at some point with the given arguments.

```python
>>> mock = AsyncMock()
>>> async def main(*args, **kwargs):
...     await mock(*args, **kwargs)
...
>>> asyncio.run(main('foo', bar='bar'))
>>> asyncio.run(main('hello'))
>>> mock.assert_any_await('foo', bar='bar')
>>> mock.assert_any_await('other')
Traceback (most recent call last):
...
AssertionError: mock('other') await not found

```

 assert_has_awaits(*calls*, *any_order=False*)

Assert the mock was awaited with the given calls. The awaits are verified against the `await_args_list` list.

When *any_order* is false, the awaits have to be sequential. Extra calls may occur before or after the given awaits.

When *any_order* is true, the awaits may come in any sequence, yet every one of them has to be present in `await_args_list`.

```python
>>> mock = AsyncMock()
>>> async def main(*args, **kwargs):
...     await mock(*args, **kwargs)
...
>>> calls = [call("foo"), call("bar")]
>>> mock.assert_has_awaits(calls)
Traceback (most recent call last):
...
AssertionError: Awaits not found.
Expected: [call('foo'), call('bar')]
Actual: []
>>> asyncio.run(main('foo'))
>>> asyncio.run(main('bar'))
>>> mock.assert_has_awaits(calls)

```

 assert_not_awaited()

Assert that the mock was not awaited at any time.

```python
>>> mock = AsyncMock()
>>> mock.assert_not_awaited()

```

 reset_mock(**args*, ***kwargs*)

Refer to `Mock.reset_mock()`. It additionally resets `await_count` to 0 and `await_args` to None, and empties the `await_args_list`.

 await_count

An integer that tracks the number of times the mock object has been awaited.

```python
>>> mock = AsyncMock()
>>> async def main():
...     await mock()
...
>>> asyncio.run(main())
>>> mock.await_count
1
>>> asyncio.run(main())
>>> mock.await_count
2

```

[Subject index](INDEX.md) · [Previous](async-mock-await-count-and-argument-assertions.md) · [Continue](the-mock-class.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md) · [Owning module, declaration or section: unittest.mock.AsyncMock](unittest-mock-asyncmock-class.md) · [Owning module, declaration or section: The Mock Class](unittest-mock-mock-class.md)
