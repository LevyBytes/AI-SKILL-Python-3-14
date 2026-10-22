# unittest.mock: Mock callable, iterable and exception side effects

side_effect

Permitted values here are a function fired when the mock gets called, an iterable, or else an exception (class or instance) meant to be raised.

When you hand in a function, it gets invoked with the same arguments as the mock, and as long as the function does not return the `DEFAULT` singleton, the call to the mock then returns whatever that function returns. Should the function return `DEFAULT`, the mock returns its usual value (taken from the `return_value`).

When you hand in an iterable, it serves to obtain an iterator that has to yield a value on each call. That value may be either an exception instance to throw or a value to return from the call to the mock (`DEFAULT` is treated exactly as in the function case).

Here is a mock that throws an exception (to exercise an API’s exception handling):

```python
>>> mock = Mock()
>>> mock.side_effect = Exception('Boom!')
>>> mock()
Traceback (most recent call last):
  ...
Exception: Boom!

```

Applying `side_effect` to hand back a series of values:

```python
>>> mock = Mock()
>>> mock.side_effect = [3, 2, 1]
>>> mock(), mock(), mock()
(3, 2, 1)

```

Using a callable:

```python
>>> mock = Mock(return_value=3)
>>> def side_effect(*args, **kwargs):
...     return DEFAULT
...
>>> mock.side_effect = side_effect
>>> mock()
3

```

You can assign `side_effect` in the constructor. The following example adds one to whatever value the mock is called with and hands it back:

```python
>>> side_effect = lambda value: value + 1
>>> mock = Mock(side_effect=side_effect)
>>> mock(3)
4
>>> mock(-8)
-7

```

Assigning `side_effect` to `None` clears it:

```python
>>> m = Mock(side_effect=KeyError, return_value=3)
>>> m()
Traceback (most recent call last):
 ...
KeyError
>>> m.side_effect = None
>>> m()
3

```

[Subject index](INDEX.md) · [Previous](mock-return-value.md) · [Continue](mock-call-arguments.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md) · [Owning module, declaration or section: unittest.mock.Mock](unittest-mock-mock-class.md) · [Owning module, declaration or section: The Mock Class](unittest-mock-mock-class.md)
