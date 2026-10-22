# unittest.mock: `unittest.mock.AsyncMock`

*class *unittest.mock.AsyncMock(*spec=None*, *side_effect=None*, *return_value=DEFAULT*, *wraps=None*, *name=None*, *spec_set=None*, *unsafe=False*, ***kwargs*)

An async counterpart to `MagicMock`. An `AsyncMock` object behaves such that it is identified as an async function, and calling it yields an awaitable.

```python
>>> mock = AsyncMock()
>>> inspect.iscoroutinefunction(mock)
True
>>> inspect.isawaitable(mock())
True

```

Calling `mock()` produces an async function whose value, once awaited, comes from `side_effect` or `return_value`:

- when `side_effect` is a function, the async function yields whatever that function produces,

- when `side_effect` is an exception, the async function raises that exception,

- when `side_effect` is an iterable, the async function yields the iterable's next value, though once the series of results runs out, `StopAsyncIteration` is raised right away,

- when `side_effect` is left undefined, the async function yields the value given by `return_value`, so by default the async function yields a fresh `AsyncMock` object.

Assigning the *spec* of a `Mock` or `MagicMock` to an async function makes calling it produce a coroutine object.

```python
>>> async def async_func(): pass
...
>>> mock = MagicMock(async_func)
>>> mock
<MagicMock spec='function' id='...'>
>>> mock()
<coroutine object AsyncMockMixin._mock_call at ...>

```

Assigning the *spec* of a `Mock`, `MagicMock`, or `AsyncMock` to a class that mixes async and sync functions makes the sync functions get detected automatically and registered as `MagicMock` (when the parent mock is `AsyncMock` or `MagicMock`) or `Mock` (when the parent mock is `Mock`). Every async function becomes an `AsyncMock`.

```python
>>> class ExampleClass:
...     def sync_foo():
...         pass
...     async def async_foo():
...         pass
...
>>> a_mock = AsyncMock(ExampleClass)
>>> a_mock.sync_foo
<MagicMock name='mock.sync_foo' id='...'>
>>> a_mock.async_foo
<AsyncMock name='mock.async_foo' id='...'>
>>> mock = Mock(ExampleClass)
>>> mock.sync_foo
<Mock name='mock.sync_foo' id='...'>
>>> mock.async_foo
<AsyncMock name='mock.async_foo' id='...'>

```

Added in version 3.8.

[Subject index](INDEX.md) · [Previous](unittest-mock-propertymock-class.md) · [Continue](async-mock-await-count-and-argument-assertions.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md) · [Owning module, declaration or section: The Mock Class](unittest-mock-mock-class.md)
