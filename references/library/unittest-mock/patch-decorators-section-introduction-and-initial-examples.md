# unittest.mock - Patch decorators - Section introduction and initial examples

### Patch decorators

Note

When using [`patch()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.patch), the key is to patch objects in the namespace where they get looked up. Usually this is simple, but for a fast walkthrough see [where to patch](https://docs.python.org/3.14/library/unittest.mock.html#where-to-patch).

Tests often need to patch a class attribute or a module attribute - for instance patching a builtin, or patching a class within a module to confirm it gets instantiated. Since modules and classes act as globals, any patch on them must be reversed once the test finishes, or the patch lingers into later tests and produces problems that are hard to track down.

For this, mock offers three handy decorators: [`patch()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.patch), [`patch.object()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.patch.object) and [`patch.dict()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.patch.dict). `patch` accepts a lone string shaped like `package.module.Class.attribute` to name the attribute under patch. Optionally it also accepts a value to put in place of the attribute (or class or whatever). 'patch.object' accepts an object together with the name of the attribute you wish to patch, and optionally the value to patch it with.

`patch.object`:

```python
>>> original = SomeClass.attribute
>>> @patch.object(SomeClass, 'attribute', sentinel.attribute)
... def test():
...     assert SomeClass.attribute == sentinel.attribute
...
>>> test()
>>> assert SomeClass.attribute == original

>>> @patch('package.module.attribute', sentinel.attribute)
... def test():
...     from package.module import attribute
...     assert attribute is sentinel.attribute
...
>>> test()

```

When patching a module (the [`builtins`](https://docs.python.org/3.14/library/builtins.html#module-builtins) module included), reach for [`patch()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.patch) rather than [`patch.object()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.patch.object):

```python
>>> mock = MagicMock(return_value=sentinel.file_handle)
>>> with patch('builtins.open', mock):
...     handle = open('filename', 'r')
...
>>> mock.assert_called_with('filename', 'r')
>>> assert handle == sentinel.file_handle, "incorrect file handle returned"

```

If required, the module name can be 'dotted', shaped as `package.module`:

```python
>>> @patch('package.module.ClassName.attribute', sentinel.attribute)
... def test():
...     from package.module import ClassName
...     assert ClassName.attribute == sentinel.attribute
...
>>> test()

```

One pleasant approach is decorating the test methods directly:

```python
>>> class MyTest(unittest.TestCase):
...     @patch.object(SomeClass, 'attribute', sentinel.attribute)
...     def test_something(self):
...         self.assertEqual(SomeClass.attribute, sentinel.attribute)
...
>>> original = SomeClass.attribute
>>> MyTest('test_something').test_something()
>>> assert SomeClass.attribute == original

```

To patch with a Mock, call [`patch()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.patch) with just one argument (or [`patch.object()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.patch.object) with two). The mock gets built for you and handed into the test function or method:

```python
>>> class MyTest(unittest.TestCase):
...     @patch.object(SomeClass, 'static_method')
...     def test_something(self, mock_method):
...         SomeClass.static_method()
...         mock_method.assert_called_with()
...
>>> MyTest('test_something').test_something()

```

This same pattern lets you stack several patch decorators together:

[Subject index](INDEX.md) · [Previous](using-side-effect-to-return-per-file-content.md) · [Continue](patch-decorators-code-example-class-mytest-unittest-testcase.md) · [Owning module, declaration or section: unittest.mock](mock-patching-methods.md)
