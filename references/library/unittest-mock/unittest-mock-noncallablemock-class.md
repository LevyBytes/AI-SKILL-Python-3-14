# unittest.mock: `unittest.mock.NonCallableMock`

*class *unittest.mock.NonCallableMock(*spec=None*, *wraps=None*, *name=None*, *spec_set=None*, ***kwargs*)

A version of `Mock` that cannot be called. The constructor parameters carry the same meaning as for `Mock`, except for *return_value* and *side_effect*, which mean nothing on a non-callable mock.

Mock objects that adopt a class or an instance as their `spec` or `spec_set` are capable of clearing [`isinstance()`](https://docs.python.org/3.14/library/functions.html#isinstance) tests:

```python
>>> mock = Mock(spec=SomeClass)
>>> isinstance(mock, SomeClass)
True
>>> mock = Mock(spec_set=SomeClass())
>>> isinstance(mock, SomeClass)
True

```

The `Mock` classes come with support for mocking magic methods. See magic methods for every detail.

The mock classes along with the `patch()` decorators all accept arbitrary keyword arguments for setup. For the `patch()` decorators those keywords flow to the constructor of the mock being built. The keyword arguments serve to set up attributes of the mock:

```python
>>> m = MagicMock(attribute=3, other='fish')
>>> m.attribute
3
>>> m.other
'fish'

```

[Subject index](INDEX.md) · [Previous](mock-call-history.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md) · [Owning module, declaration or section: The Mock Class](unittest-mock-mock-class.md) · [Required continuation of the source contract](mock-patch-configuration-and-call-signatures.md)
