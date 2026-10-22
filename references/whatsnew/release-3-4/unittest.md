# What's New In Python 3.4 / unittest — unittest

### unittest

The [`TestCase`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase) class has a new method, [`subTest()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.subTest), yielding a context manager whose [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) block turns into a "sub-test". Such a context manager lets a test method spin up subtests on the fly by, for example, invoking the `subTest` context manager within a loop. One single test method can in this way emit any number of individually identified and individually counted tests, every one of which runs even should one or several of them fail. As an example:

```python
class NumbersTest(unittest.TestCase):
    def test_even(self):
        for i in range(6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)

```

will produce six subtests, each labeled in the unittest verbose output by a tag built from the variable name `i` paired with a specific value for it (`i=0`, `i=1`, etc). Refer to [Distinguishing test iterations using subtests](https://docs.python.org/3.14/library/unittest.html#subtests) for this example in full. (Contributed by Antoine Pitrou in [bpo-16997](https://bugs.python.org/issue?@action=redirect&bpo=16997).)

[`unittest.main()`](https://docs.python.org/3.14/library/unittest.html#unittest.main) now takes an iterable of test names for *defaultTest*, whereas formerly it would only take one single test name supplied as a string. (Contributed by Jyrki Pulliainen in [bpo-15132](https://bugs.python.org/issue?@action=redirect&bpo=15132).)

Should [`SkipTest`](https://docs.python.org/3.14/library/unittest.html#unittest.SkipTest) be raised while tests are being discovered (that is, at the module level in the test file), it now gets reported as a skip in place of an error. (Contributed by Zach Ware in [bpo-16935](https://bugs.python.org/issue?@action=redirect&bpo=16935).)

[`discover()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestLoader.discover) will now sort whatever files it finds so that test runs keep a stable order. (Contributed by Martin Melin and Jeff Ramnani in [bpo-16709](https://bugs.python.org/issue?@action=redirect&bpo=16709).)

[`TestSuite`](https://docs.python.org/3.14/library/unittest.html#unittest.TestSuite) will release each test reference the moment that test finishes, provided the run passed. Under interpreters that perform garbage collection, a passing test may then be reclaimed once no other reference remains to it. You can opt out of this behavior by subclassing `TestSuite` and supplying your own `_removeTestAtIndex` method. (Contributed by Tom Wardill, Matt McClure, and Andrew Svetlov in [bpo-11798](https://bugs.python.org/issue?@action=redirect&bpo=11798).)

A fresh test-assertion context manager, [`assertLogs()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertLogs), confirms that a wrapped section of code produces a log entry through the [`logging`](https://docs.python.org/3.14/library/logging.html#module-logging) module. Out of the box any logger and a severity of `INFO` or above will satisfy it, yet you may pin down both a specific logger name and a different floor for the logging level. Whatever the context manager hands back can be inspected for the [`LogRecord`](https://docs.python.org/3.14/library/logging.html#logging.LogRecord)s and/or the rendered text that ended up being logged. (Contributed by Antoine Pitrou in [bpo-18937](https://bugs.python.org/issue?@action=redirect&bpo=18937).)

Discovery of tests is now compatible with namespace packages (Contributed by Claudiu Popa in [bpo-17457](https://bugs.python.org/issue?@action=redirect&bpo=17457).)

[`unittest.mock`](https://docs.python.org/3.14/library/unittest.mock.html#module-unittest.mock) objects will now consult the spec signatures while comparing calls, so a given argument can be paired up by its position or by its name rather than purely by position. (Contributed by Antoine Pitrou in [bpo-17015](https://bugs.python.org/issue?@action=redirect&bpo=17015).)

[`mock_open()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.mock_open) objects have gained `readline` and `readlines` methods. (Contributed by Toshio Kuratomi in [bpo-17467](https://bugs.python.org/issue?@action=redirect&bpo=17467).)

[Subject index](INDEX.md) · [Previous source section](urllib.md) · [Release/subject declaration](release-highlights.md) · [Next source section](venv.md)
