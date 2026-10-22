# unittest.mock — Side effect functions and iterables

### Side effect functions and iterables

You may equally assign `side_effect` a function or an iterable. The reason to make `side_effect` an iterable is that your mock will be called multiple times and you want a distinct value back from each call. Once `side_effect` holds an iterable, every call to the mock yields the next item from that iterable:

```python
>>> mock = MagicMock(side_effect=[4, 5, 6])
>>> mock()
4
>>> mock()
5
>>> mock()
6

```

In trickier situations - say, varying the returned values on the fly based on how the mock was called - `side_effect` may be a function. That function receives the very same arguments the mock got. Whatever it returns becomes the call's result:

```python
>>> vals = {(1, 2): 1, (2, 3): 2}
>>> def side_effect(*args):
...     return vals[args]
...
>>> mock = MagicMock(side_effect=side_effect)
>>> mock(1, 2)
1
>>> mock(2, 3)
2

```

[Subject index](INDEX.md) · [Previous](raising-exceptions-with-mocks.md) · [Continue](mocking-asynchronous-iterators.md) · [Owning module, declaration or section: unittest.mock](mock-patching-methods.md)
