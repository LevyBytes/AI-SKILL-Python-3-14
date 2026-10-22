# unittest.mock — Mocking asynchronous context manager

### Mocking asynchronous context manager

Starting with Python 3.8, `AsyncMock` and `MagicMock` can mock [Asynchronous Context Managers](https://docs.python.org/3.14/reference/datamodel.html#async-context-managers) by way of `__aenter__` and `__aexit__`. Out of the box, `__aenter__` and `__aexit__` are `AsyncMock` instances that hand back an async function.

```python
>>> class AsyncContextManager:
...     async def __aenter__(self):
...         return self
...     async def __aexit__(self, exc_type, exc, tb):
...         pass
...
>>> mock_instance = MagicMock(AsyncContextManager())  # AsyncMock also works here
>>> async def main():
...     async with mock_instance as result:
...         pass
...
>>> asyncio.run(main())
>>> mock_instance.__aenter__.assert_awaited_once()
>>> mock_instance.__aexit__.assert_awaited_once()

```

[Subject index](INDEX.md) · [Previous](mocking-asynchronous-iterators.md) · [Continue](creating-a-mock-from-an-existing-object.md) · [Owning module, declaration or section: unittest.mock](mock-patching-methods.md)
