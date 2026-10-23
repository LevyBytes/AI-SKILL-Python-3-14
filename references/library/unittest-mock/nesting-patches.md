# unittest.mock - Nesting patches

### Nesting patches

Reaching for patch as a context manager works nicely, yet stacking several patches leaves you with nested with statements that keep marching further to the right:

```python
>>> class MyTest(unittest.TestCase):
...
...     def test_foo(self):
...         with patch('mymodule.Foo') as mock_foo:
...             with patch('mymodule.Bar') as mock_bar:
...                 with patch('mymodule.Spam') as mock_spam:
...                     assert mymodule.Foo is mock_foo
...                     assert mymodule.Bar is mock_bar
...                     assert mymodule.Spam is mock_spam
...
>>> original = mymodule.Foo
>>> MyTest('test_foo').test_foo()
>>> assert mymodule.Foo is original

```

Pairing unittest `cleanup` functions with the [patch methods: start and stop](https://docs.python.org/3.14/library/unittest.mock.html#start-and-stop) lets us reach the very same outcome minus the nested indentation. A short helper method, `create_patch`, installs the patch and returns the mock it produced:

```python
>>> class MyTest(unittest.TestCase):
...
...     def create_patch(self, name):
...         patcher = patch(name)
...         thing = patcher.start()
...         self.addCleanup(patcher.stop)
...         return thing
...
...     def test_foo(self):
...         mock_foo = self.create_patch('mymodule.Foo')
...         mock_bar = self.create_patch('mymodule.Bar')
...         mock_spam = self.create_patch('mymodule.Spam')
...
...         assert mymodule.Foo is mock_foo
...         assert mymodule.Bar is mock_bar
...         assert mymodule.Spam is mock_spam
...
>>> original = mymodule.Foo
>>> MyTest('test_foo').run()
>>> assert mymodule.Foo is original

```

[Subject index](INDEX.md) · [Previous](mutable-mock-argument-deepcopy-example.md) · [Continue](mocking-a-dictionary-with-magicmock.md) · [Owning module, declaration or section: unittest.mock](mock-patching-methods.md)
