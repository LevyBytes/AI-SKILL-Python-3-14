# unittest.mock / The Mock Class: `unittest.mock.ThreadingMock`, `wait_until_called()`, `wait_until_any_call_with()`

*class *unittest.mock.ThreadingMock(*spec=None*, *side_effect=None*, *return_value=DEFAULT*, *wraps=None*, *name=None*, *spec_set=None*, *unsafe=False*, ***, *timeout=UNSET*, ***kwargs*)

A flavor of `MagicMock` aimed at multithreading tests. A `ThreadingMock` object adds methods for waiting on a call to occur, instead of asserting on it on the spot.

The default timeout comes from the `timeout` argument, or when that's unset from the `ThreadingMock.DEFAULT_TIMEOUT` attribute, whose default is to block (`None`).

The global default timeout can be set by assigning to `ThreadingMock.DEFAULT_TIMEOUT`.

 wait_until_called(***, *timeout=UNSET*)

Blocks until the mock gets called.

When a timeout was given at the mock's creation, or when a timeout argument is handed to this function, it raises an [`AssertionError`](https://docs.python.org/3.14/library/exceptions.html#AssertionError) if the call doesn't happen within that window.

```python
>>> mock = ThreadingMock()
>>> thread = threading.Thread(target=mock)
>>> thread.start()
>>> mock.wait_until_called(timeout=1)
>>> thread.join()

```

 wait_until_any_call_with(**args*, ***kwargs*)

Blocks until the mock gets called with the given arguments.

When a timeout was given at the mock's creation, the function raises an [`AssertionError`](https://docs.python.org/3.14/library/exceptions.html#AssertionError) if the call doesn't happen within that window.

```python
>>> mock = ThreadingMock()
>>> thread = threading.Thread(target=mock, args=("arg1", "arg2",), kwargs={"arg": "thing"})
>>> thread.start()
>>> mock.wait_until_any_call_with("arg1", "arg2", arg="thing")
>>> thread.join()

```

 DEFAULT_TIMEOUT

Global default timeout, in seconds, for building `ThreadingMock` instances.

Added in version 3.13.

[Subject index](INDEX.md) · [Previous](the-mock-class.md) · [Continue](calling-section-introduction-and-initial-examples.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md) · [Owning module, declaration or section: The Mock Class](unittest-mock-mock-class.md)
