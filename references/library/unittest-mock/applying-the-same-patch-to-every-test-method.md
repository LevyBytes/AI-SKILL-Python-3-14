# unittest.mock - Applying the same patch to every test method

### Applying the same patch to every test method

When you need the same set of patches across a number of test methods, the straightforward route is to stack the patch decorators on each one. That tends to feel like pointless duplication. As an alternative, [`patch()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.patch) (in any of its forms) can serve as a class decorator, which spreads the patches across every test method on that class. Here a test method counts as any method whose name begins with `test`:

```python
>>> @patch('mymodule.SomeClass')
... class MyTest(unittest.TestCase):
...
...     def test_one(self, MockSomeClass):
...         self.assertIs(mymodule.SomeClass, MockSomeClass)
...
...     def test_two(self, MockSomeClass):
...         self.assertIs(mymodule.SomeClass, MockSomeClass)
...
...     def not_a_test(self):
...         return 'something'
...
>>> MyTest('test_one').test_one()
>>> MyTest('test_two').test_two()
>>> MyTest('test_two').not_a_test()
'something'

```

A different strategy for handling patches relies on the [patch methods: start and stop](https://docs.python.org/3.14/library/unittest.mock.html#start-and-stop). With those, you can relocate the patching into your `setUp` and `tearDown` methods.

```python
>>> class MyTest(unittest.TestCase):
...     def setUp(self):
...         self.patcher = patch('mymodule.foo')
...         self.mock_foo = self.patcher.start()
...
...     def test_foo(self):
...         self.assertIs(mymodule.foo, self.mock_foo)
...
...     def tearDown(self):
...         self.patcher.stop()
...
>>> MyTest('test_foo').run()

```

Going this route means you have to guarantee the patch is "undone" via a call to `stop`. That turns out to be trickier than expected, since a failure raised inside setUp means tearDown never runs. Using [`unittest.TestCase.addCleanup()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.addCleanup) smooths this over:

```python
>>> class MyTest(unittest.TestCase):
...     def setUp(self):
...         patcher = patch('mymodule.foo')
...         self.addCleanup(patcher.stop)
...         self.mock_foo = patcher.start()
...
...     def test_foo(self):
...         self.assertIs(mymodule.foo, self.mock_foo)
...
>>> MyTest('test_foo').run()

```

[Subject index](INDEX.md) · [Previous](mocking-a-generator-method.md) · [Continue](mocking-unbound-methods.md) · [Owning module, declaration or section: unittest.mock](mock-patching-methods.md)
