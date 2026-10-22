# unittest.mock: `unittest.mock.PropertyMock`

*class *unittest.mock.PropertyMock(**args*, ***kwargs*)

A mock designed to serve as a [`property`](https://docs.python.org/3.14/library/functions.html#property), or another [descriptor](https://docs.python.org/3.14/glossary.html#term-descriptor), on a class. `PropertyMock` supplies [`__get__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__get__) and [`__set__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__set__) methods, letting you declare a return value for when it gets read.

Reading a `PropertyMock` instance off an object invokes the mock with no arguments. Assigning to it invokes the mock with the value being assigned.

```python
>>> class Foo:
...     @property
...     def foo(self):
...         return 'something'
...     @foo.setter
...     def foo(self, value):
...         pass
...
>>> with patch('__main__.Foo.foo', new_callable=PropertyMock) as mock_foo:
...     mock_foo.return_value = 'mockity-mock'
...     this_foo = Foo()
...     print(this_foo.foo)
...     this_foo.foo = 6
...
mockity-mock
>>> mock_foo.mock_calls
[call(), call(6)]

```

Owing to how mock attributes are kept, a `PropertyMock` can't be attached straight onto a mock object. The workaround is to attach it to the mock type object instead:

```python
>>> m = MagicMock()
>>> p = PropertyMock(return_value=3)
>>> type(m).foo = p
>>> m.foo
3
>>> p.assert_called_once_with()

```

Caution

Should `PropertyMock` raise an [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError), it is read as a descriptor that's absent, and [`__getattr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattr__) gets invoked on the parent mock:

```python
>>> m = MagicMock()
>>> no_attribute = PropertyMock(side_effect=AttributeError)
>>> type(m).my_property = no_attribute
>>> m.my_property
<MagicMock name='mock.my_property' id='140165240345424'>

```

Consult [`__getattr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattr__) for the specifics.

[Subject index](INDEX.md) · [Previous](mock-patch-configuration-and-call-signatures.md) · [Continue](unittest-mock-asyncmock-class.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md) · [Owning module, declaration or section: The Mock Class](unittest-mock-mock-class.md)
