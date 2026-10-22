# unittest — Basic example

### Basic example

A wide assortment of tools for building and running tests comes with the `unittest` module. This section shows how just a small portion of those tools is enough for what most users need.

The short script below tests three string methods:

```python
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()

```

To build a test case, subclass `unittest.TestCase`. Each of the three separate tests is written as a method whose name begins with the letters `test`. This naming convention tells the test runner which methods stand for tests.

At the heart of every test sits a call to `assertEqual()` to confirm an expected result; to `assertTrue()` or `assertFalse()` to confirm a condition; or to `assertRaises()` to confirm that a particular exception gets raised. Using these methods rather than the [`assert`](https://docs.python.org/3.14/reference/simple_stmts.html#assert) statement lets the test runner gather every test result and turn out a report.

With the `setUp()` and `tearDown()` methods you can specify instructions to run before and after each test method. The section Organizing test code goes into them in greater depth.

The closing block illustrates one straightforward way to run the tests. A command-line interface to the test script is what `unittest.main()` supplies. Invoked from the command line, the script above yields output resembling this:

```python
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK

```

Supplying the `-v` option to your test script tells `unittest.main()` to switch on a higher level of verbosity, yielding the output shown next:

```python
test_isupper (__main__.TestStringMethods.test_isupper) ... ok
test_split (__main__.TestStringMethods.test_split) ... ok
test_upper (__main__.TestStringMethods.test_upper) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK

```

What the examples above showcase are the most frequently used `unittest` features, and these alone serve plenty of routine testing needs. The rest of this documentation builds up the complete feature set starting from first principles.

Changed in version 3.11: Having a test method return a value (anything besides the default `None`) is deprecated as of this release.

[Subject index](INDEX.md) · [Previous](unittest-unit-testing-framework.md) · [Continue](command-line-interface.md) · [Owning module, declaration or section: unittest](unittest-unit-testing-framework.md)
