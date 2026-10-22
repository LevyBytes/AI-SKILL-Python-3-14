# unittest.mock — Mocking asynchronous iterators

### Mocking asynchronous iterators

Starting with Python 3.8, `AsyncMock` and `MagicMock` can mock [Asynchronous Iterators](https://docs.python.org/3.14/reference/datamodel.html#async-iterators) by way of `__aiter__`. You can set the [`return_value`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock.return_value) attribute of `__aiter__` to define which values the iteration yields.

```python
>>> mock = MagicMock()  # AsyncMock also works here
>>> mock.__aiter__.return_value = [1, 2, 3]
>>> async def main():
...     return [i async for i in mock]
...
>>> asyncio.run(main())
[1, 2, 3]

```

[Subject index](INDEX.md) · [Previous](side-effect-functions-and-iterables.md) · [Continue](mocking-asynchronous-context-manager.md) · [Owning module, declaration or section: unittest.mock](mock-patching-methods.md)
