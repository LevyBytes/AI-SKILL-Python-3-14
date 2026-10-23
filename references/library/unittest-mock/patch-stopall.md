# unittest.mock - patch methods: start and stop

### patch methods: start and stop

Every patcher carries `start()` and `stop()` methods. They ease patching inside `setUp` methods, or wherever you'd rather do several patches without stacking decorators or with statements.

To employ them, invoke `patch()`, `patch.object()` or `patch.dict()` as usual and hold on to the `patcher` object returned. Then call `start()` to install the patch and `stop()` to reverse it.

When `patch()` is making a mock for you, that mock comes back from the `patcher.start` call.

```python
>>> patcher = patch('package.module.ClassName')
>>> from package import module
>>> original = module.ClassName
>>> new_mock = patcher.start()
>>> assert module.ClassName is not original
>>> assert module.ClassName is new_mock
>>> patcher.stop()
>>> assert module.ClassName is original
>>> assert module.ClassName is not new_mock

```

One common application is performing several patches inside the `setUp` method of a [`TestCase`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase):

```python
>>> class MyTest(unittest.TestCase):
...     def setUp(self):
...         self.patcher1 = patch('package.module.Class1')
...         self.patcher2 = patch('package.module.Class2')
...         self.MockClass1 = self.patcher1.start()
...         self.MockClass2 = self.patcher2.start()
...
...     def tearDown(self):
...         self.patcher1.stop()
...         self.patcher2.stop()
...
...     def test_something(self):
...         assert package.module.Class1 is self.MockClass1
...         assert package.module.Class2 is self.MockClass2
...
>>> MyTest('test_something').run()

```

Caution

When you adopt this approach you have to make sure the patching gets “undone” by calling `stop`. That can prove trickier than expected, since a `tearDown` won't run if an exception is raised within the `setUp`. [`unittest.TestCase.addCleanup()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.addCleanup) eases this:

```python
>>> class MyTest(unittest.TestCase):
...     def setUp(self):
...         patcher = patch('package.module.Class')
...         self.MockClass = patcher.start()
...         self.addCleanup(patcher.stop)
...
...     def test_something(self):
...         assert package.module.Class is self.MockClass
...

```

A further perk is that holding on to the `patcher` object is no longer necessary.

You can also halt every patch that has been started by calling `patch.stopall()`.

 patch.stopall()

Stop all active patches. Only stops patches started with `start`.

[Subject index](INDEX.md) · [Previous](patch-multiple.md) · [Continue](patch-builtins.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md)
