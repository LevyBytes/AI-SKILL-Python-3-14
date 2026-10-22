# unittest — Organizing test code — Section introduction and initial examples

### Organizing test code

Unit testing rests on *test cases* as its basic building blocks — individual scenarios that have to be set up and then checked for correctness. Within `unittest`, instances of `unittest.TestCase` stand for test cases. Crafting your own test cases means writing subclasses of `TestCase` or using `FunctionTestCase`.

A `TestCase` instance's testing code ought to be wholly self contained, so that it can run on its own or in any combination alongside any number of other test cases.

The most basic `TestCase` subclass need only implement a test method (that is, a method whose name begins with `test`) so as to carry out particular testing code:

```python
import unittest

class DefaultWidgetSizeTestCase(unittest.TestCase):
    def test_default_widget_size(self):
        widget = Widget('The widget')
        self.assertEqual(widget.size(), (50, 50))

```

Observe that to actually test anything, we reach for one of the assert* methods that the `TestCase` base class offers. A failing test raises an exception carrying an explanatory message, and `unittest` flags that test case as a *failure*. Exceptions of any other kind are handled as *errors*.

There can be a great many tests, and setting them up tends to repeat itself. Fortunately, we can pull set-up code out into a method named `setUp()`, which the testing framework calls automatically before each and every test we run:

```python
import unittest

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50,50),
                         'incorrect default size')

    def test_widget_resize(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150),
                         'wrong size after resize')

```

Note

What dictates the order the various tests run in is the sorting of the test method names according to the built-in ordering for strings.

Should the `setUp()` method raise an exception while the test runs, the framework regards the test as having hit an error, and the test method does not get executed.

In the same way, we can supply a `tearDown()` method to clean up once the test method has finished running:

```python
import unittest

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def tearDown(self):
        self.widget.dispose()

```

Provided `setUp()` succeeded, `tearDown()` runs no matter whether the test method passed or not.

This kind of working environment for the testing code goes by the name *test fixture*. For each individual test method, a fresh TestCase instance is built to serve as that method's own test fixture. Accordingly, `setUp()`, `tearDown()`, and `TestCase.__init__()` each run once per test.

Grouping your tests with TestCase implementations according to the features under test is the recommended practice. `unittest` offers a mechanism for that: the *test suite*, embodied by the `TestSuite` class of `unittest`. For the most part, a call to `unittest.main()` does just what you want, gathering up every one of the module's test cases on your behalf and running them.

Still, if you want to take charge of how your test suite is assembled, you can do so yourself:

```python
def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_default_widget_size'))
    suite.addTest(WidgetTestCase('test_widget_resize'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

```

Although you may keep the test case and test suite definitions in the very modules holding the code they exercise (for instance `widget.py`), several benefits come from putting the test code in a module of its own, such as `test_widget.py`:

[Subject index](INDEX.md) · [Previous](test-discovery.md) · [Continue](standalone-test-module-execution.md) · [Owning module, declaration or section: unittest](unittest-unit-testing-framework.md)
