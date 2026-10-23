# unittest.mock - Creating a mock from an existing object

### Creating a mock from an existing object

A pitfall of overusing mocking is that it ties your tests to your mocks' implementation instead of to your actual code. Imagine a class providing `some_method`. While testing a separate class, you hand it a mock of this object that *also* provides `some_method`. Should you later refactor the first class so it drops `some_method`, your tests will keep passing even though your code is now broken!

[`Mock`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock) lets you supply an object to act as the mock's specification via the *spec* keyword argument. Touching methods or attributes on the mock that are absent from your specification object instantly raises an attribute error. Change the implementation of your specification, and tests relying on that class start failing right away without your needing to instantiate the class within those tests.

```python
>>> mock = Mock(spec=SomeClass)
>>> mock.old_method()
Traceback (most recent call last):
   ...
AttributeError: Mock object has no attribute 'old_method'. Did you mean: 'class_method'?

```

Supplying a specification additionally turns on smarter matching of calls made against the mock, no matter whether certain parameters arrived as positional or keyword arguments:

```python
>>> def f(a, b, c): pass
...
>>> mock = Mock(spec=f)
>>> mock(1, 2, 3)
<Mock name='mock()' id='140161580456576'>
>>> mock.assert_called_with(a=1, b=2, c=3)

```

To extend this smarter matching to method calls on the mock as well, reach for [auto-speccing](https://docs.python.org/3.14/library/unittest.mock.html#auto-speccing).

For a tighter specification that blocks both setting and getting of arbitrary attributes, use *spec_set* in place of *spec*.

[Subject index](INDEX.md) · [Previous](mocking-asynchronous-context-manager.md) · [Continue](using-side-effect-to-return-per-file-content.md) · [Owning module, declaration or section: unittest.mock](mock-patching-methods.md)
