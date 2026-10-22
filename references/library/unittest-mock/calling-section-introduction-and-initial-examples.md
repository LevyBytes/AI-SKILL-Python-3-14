# unittest.mock — Calling — Section introduction and initial examples

### Calling

Mock objects can be called. A call yields whatever is held in the `return_value` attribute. By default that return value is a brand-new Mock object, created the first time the return value gets accessed (whether directly or by calling the Mock) - though it's retained, and the identical one comes back every time.

Each call against the object gets logged in attributes such as `call_args` and `call_args_list`.

When `side_effect` is configured, it runs after the call has been logged, so even if `side_effect` throws an exception the call is still on record.

The easiest route to having a mock throw an exception on a call is to set `side_effect` to an exception class or instance:

```python
>>> m = MagicMock(side_effect=IndexError)
>>> m(1, 2, 3)
Traceback (most recent call last):
  ...
IndexError
>>> m.mock_calls
[call(1, 2, 3)]
>>> m.side_effect = KeyError('Bang!')
>>> m('two', 'three', 'four')
Traceback (most recent call last):
  ...
KeyError: 'Bang!'
>>> m.mock_calls
[call(1, 2, 3), call('two', 'three', 'four')]

```

When `side_effect` is a function, whatever it returns becomes the result of calls to the mock. That `side_effect` function receives the very same arguments as the mock. This lets you adjust the call's return value on the fly according to the input:

```python
>>> def side_effect(value):
...     return value + 1
...
>>> m = MagicMock(side_effect=side_effect)
>>> m(1)
2
>>> m(2)
3
>>> m.mock_calls
[call(1), call(2)]

```

Should you still want the mock to hand back its default return value (a fresh mock), or whatever return value you assigned, there are two routes. Either hand back `return_value` from within `side_effect`, or hand back `DEFAULT`:

```python
>>> m = MagicMock()
>>> def side_effect(*args, **kwargs):
...     return m.return_value
...
>>> m.side_effect = side_effect
>>> m.return_value = 3
>>> m()
3
>>> def side_effect(*args, **kwargs):
...     return DEFAULT
...
>>> m.side_effect = side_effect
>>> m()
3

```

To clear a `side_effect` and go back to the default behaviour, assign `None` to the `side_effect`:

```python
>>> m = MagicMock(return_value=6)
>>> def side_effect(*args, **kwargs):
...     return 3
...
>>> m.side_effect = side_effect
>>> m()
3
>>> m.side_effect = None
>>> m()
6

```

A `side_effect` may equally be any iterable object. Successive calls to the mock then return the iterable's values one by one (until it is depleted and a [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration) is raised):

[Subject index](INDEX.md) · [Previous](threading-mock-waiting-for-calls.md) · [Continue](calling-code-example-m-magicmock-side-effect-1-2-3.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md)
