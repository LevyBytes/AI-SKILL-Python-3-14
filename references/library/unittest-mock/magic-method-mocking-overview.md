# unittest.mock - Mocking Magic Methods - Section introduction and initial examples

### MagicMock and magic method support

### Mocking Magic Methods

`Mock` is able to mock the Python protocol methods, otherwise called [“magic methods”](https://docs.python.org/3.14/glossary.html#term-magic-method). This lets mock objects stand in for containers or other objects that implement Python protocols.

Since magic methods get looked up in a manner unlike ordinary methods [2], this capability had to be built specially. Consequently only certain magic methods are handled. The handled set covers *almost* every one of them. Should any you require be absent, do let us know.

To mock a magic method, set the one you care about to a function or a mock instance. With a function, it *must* accept `self` as its first argument [3].

```python
>>> def __str__(self):
...     return 'fooble'
...
>>> mock = Mock()
>>> mock.__str__ = __str__
>>> str(mock)
'fooble'

```

```python
>>> mock = Mock()
>>> mock.__str__ = Mock()
>>> mock.__str__.return_value = 'fooble'
>>> str(mock)
'fooble'

```

```python
>>> mock = Mock()
>>> mock.__iter__ = Mock(return_value=iter([]))
>>> list(mock)
[]

```

A scenario where this helps is mocking objects employed as context managers within a [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement:

```python
>>> mock = Mock()
>>> mock.__enter__ = Mock(return_value='foo')
>>> mock.__exit__ = Mock(return_value=False)
>>> with mock as m:
...     assert m == 'foo'
...
>>> mock.__enter__.assert_called_with()
>>> mock.__exit__.assert_called_with(None, None, None)

```

Magic method calls don't show up in `method_calls`, though they are logged in `mock_calls`.

Note

When you build a mock with the *spec* keyword argument, trying to assign a magic method absent from the spec will raise an [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError).

Here is the complete list of supported magic methods:

- `__hash__`, `__sizeof__`, `__repr__` and `__str__`

- `__dir__`, `__format__` and `__subclasses__`

- `__round__`, `__floor__`, `__trunc__` and `__ceil__`

- Comparisons: `__lt__`, `__gt__`, `__le__`, `__ge__`, `__eq__` and `__ne__`

- Container methods: `__getitem__`, `__setitem__`, `__delitem__`, `__contains__`, `__len__`, `__iter__`, `__reversed__` and `__missing__`

- Context manager: `__enter__`, `__exit__`, `__aenter__` and `__aexit__`

-

[Subject index](INDEX.md) · [Continue](mock-unary-numeric-magic-methods.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md)
