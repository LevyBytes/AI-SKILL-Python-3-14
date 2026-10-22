# unittest.mock — Patch decorators — Code example: >>> class MyTest(unittest.TestCase):

```python
>>> class MyTest(unittest.TestCase):
...     @patch('package.module.ClassName1')
...     @patch('package.module.ClassName2')
...     def test_something(self, MockClass2, MockClass1):
...         self.assertIs(package.module.ClassName1, MockClass1)
...         self.assertIs(package.module.ClassName2, MockClass2)
...
>>> MyTest('test_something').test_something()

```

With nested patch decorators, the mocks arrive at the decorated function in the order they were applied (the usual *Python* order for applying decorators). That order runs from the bottom up, so above the mock for `test_module.ClassName2` arrives first.

There's also [`patch.dict()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.patch.dict) for assigning values within a dictionary only for the span of a scope, then putting the dictionary back to its original state once the test concludes:

```python
>>> foo = {'key': 'value'}
>>> original = foo.copy()
>>> with patch.dict(foo, {'newkey': 'newvalue'}, clear=True):
...     assert foo == {'newkey': 'newvalue'}
...
>>> assert foo == original

```

Every one of `patch`, `patch.object` and `patch.dict` works as a context manager too.

Wherever you let [`patch()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.patch) build a mock for you, the "as" form of the with statement gives you a handle on that mock:

```python
>>> class ProductionClass:
...     def method(self):
...         pass
...
>>> with patch.object(ProductionClass, 'method') as mock_method:
...     mock_method.return_value = None
...     real = ProductionClass()
...     real.method(1, 2, 3)
...
>>> mock_method.assert_called_with(1, 2, 3)

```

Alternatively, `patch`, `patch.object` and `patch.dict` can serve as class decorators. Applied this way, the effect matches decorating each method whose name begins with "test" on its own.

[Subject index](INDEX.md) · [Previous](patch-decorators-section-introduction-and-initial-examples.md) · [Continue](further-examples.md) · [Owning module, declaration or section: unittest.mock](mock-patching-methods.md)
