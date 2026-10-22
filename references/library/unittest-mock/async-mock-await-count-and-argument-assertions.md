# unittest.mock.AsyncMock: `assert_awaited()`, `assert_awaited_once()`, `assert_awaited_with()`, `assert_awaited_once_with()`

assert_awaited()

Assert that the mock has been awaited one or more times. Keep in mind that this differs from the object simply having been called; the `await` keyword has to be used:

```python
>>> mock = AsyncMock()
>>> async def main(coroutine_mock):
...     await coroutine_mock
...
>>> coroutine_mock = mock()
>>> mock.called
True
>>> mock.assert_awaited()
Traceback (most recent call last):
...
AssertionError: Expected mock to have been awaited.
>>> asyncio.run(main(coroutine_mock))
>>> mock.assert_awaited()

```

 assert_awaited_once()

Assert that the mock was awaited precisely one time.

```python
>>> mock = AsyncMock()
>>> async def main():
...     await mock()
...
>>> asyncio.run(main())
>>> mock.assert_awaited_once()
>>> asyncio.run(main())
>>> mock.assert_awaited_once()
Traceback (most recent call last):
...
AssertionError: Expected mock to have been awaited once. Awaited 2 times.

```

 assert_awaited_with(**args*, ***kwargs*)

Assert that the most recent await used the given arguments.

```python
>>> mock = AsyncMock()
>>> async def main(*args, **kwargs):
...     await mock(*args, **kwargs)
...
>>> asyncio.run(main('foo', bar='bar'))
>>> mock.assert_awaited_with('foo', bar='bar')
>>> mock.assert_awaited_with('other')
Traceback (most recent call last):
...
AssertionError: expected await not found.
Expected: mock('other')
Actual: mock('foo', bar='bar')

```

 assert_awaited_once_with(**args*, ***kwargs*)

Assert that the mock was awaited just once and with the given arguments.

```python
>>> mock = AsyncMock()
>>> async def main(*args, **kwargs):
...     await mock(*args, **kwargs)
...
>>> asyncio.run(main('foo', bar='bar'))
>>> mock.assert_awaited_once_with('foo', bar='bar')
>>> asyncio.run(main('foo', bar='bar'))
>>> mock.assert_awaited_once_with('foo', bar='bar')
Traceback (most recent call last):
...
AssertionError: Expected mock to have been awaited once. Awaited 2 times.

```

[Subject index](INDEX.md) · [Previous](unittest-mock-asyncmock-class.md) · [Continue](async-mock-await-history-and-reset.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md) · [Owning module, declaration or section: unittest.mock.AsyncMock](unittest-mock-asyncmock-class.md) · [Owning module, declaration or section: The Mock Class](unittest-mock-mock-class.md)
