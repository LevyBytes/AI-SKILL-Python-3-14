# unittest.mock — Mock for method calls on an object

### Mock for method calls on an object

Previously we patched a method right onto an object to confirm it was invoked properly. Another frequent pattern hands an object to a method (or to some piece of the system under test) and then verifies that the object is used correctly.

The straightforward `ProductionClass` shown here owns a `closer` method. Given an object, it invokes `close` on that object.

```python
>>> class ProductionClass:
...     def closer(self, something):
...         something.close()
...

```

So testing it means supplying an object equipped with a `close` method and confirming that it was invoked correctly.

```python
>>> real = ProductionClass()
>>> mock = Mock()
>>> real.closer(mock)
>>> mock.close.assert_called_with()

```

No effort is required from us to supply the 'close' method on our mock. Merely touching close brings it into being. Thus, if 'close' was never called beforehand, referencing it during the test will conjure it, yet [`assert_called_with()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock.assert_called_with) will throw a failure exception.

[Subject index](INDEX.md) · [Previous](mock-patching-methods.md) · [Continue](mocking-classes.md)
