# test - Writing Unit Tests for the `test` package - Code example: class TestFuncAcceptsSequencesMixin:

```python
class TestFuncAcceptsSequencesMixin:

    func = mySuperWhammyFunction

    def test_func(self):
        self.func(self.arg)

class AcceptLists(TestFuncAcceptsSequencesMixin, unittest.TestCase):
    arg = [1, 2, 3]

class AcceptStrings(TestFuncAcceptsSequencesMixin, unittest.TestCase):
    arg = 'abc'

class AcceptTuples(TestFuncAcceptsSequencesMixin, unittest.TestCase):
    arg = (1, 2, 3)

```

Keep in mind, when you follow this pattern, that every class deriving from [`unittest.TestCase`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase) gets executed as a test. The `TestFuncAcceptsSequencesMixin` class shown above carries no data, so it cannot run on its own; that is why it does not derive from `unittest.TestCase`.

See also

Test Driven Development

A book by Kent Beck on writing tests before code.

[Subject index](INDEX.md) · [Previous](cpython-unit-test-authoring-overview.md) · [Continue](running-tests-using-the-command-line-interface.md) · [Owning module, declaration or section: test](test-regression-tests-package-for-python.md) · [Owning module, declaration or section: Writing Unit Tests for the `test` package](cpython-unit-test-authoring-overview.md)
