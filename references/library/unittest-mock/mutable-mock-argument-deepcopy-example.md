# unittest.mock - Coping with mutable arguments - Code example: >>> from copy import deepcopy

```python
>>> from copy import deepcopy
>>> class CopyingMock(MagicMock):
...     def __call__(self, /, *args, **kwargs):
...         args = deepcopy(args)
...         kwargs = deepcopy(kwargs)
...         return super().__call__(*args, **kwargs)
...
>>> c = CopyingMock(return_value=None)
>>> arg = set()
>>> c(arg)
>>> arg.add(1)
>>> c.assert_called_with(set())
>>> c.assert_called_with(arg)
Traceback (most recent call last):
    ...
AssertionError: expected call not found.
Expected: mock({1})
Actual: mock(set())
>>> c.foo
<CopyingMock name='mock.foo' id='...'>

```

Subclassing `Mock` or `MagicMock` causes every attribute generated on the fly, along with the `return_value`, to adopt your subclass on its own. The upshot is that every child of a `CopyingMock` is itself a `CopyingMock`.

[Subject index](INDEX.md) · [Previous](mutable-mock-argument-overview.md) · [Continue](nesting-patches.md) · [Owning module, declaration or section: unittest.mock](mock-patching-methods.md)
