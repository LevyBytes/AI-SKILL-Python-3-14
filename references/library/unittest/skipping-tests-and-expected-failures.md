# unittest: Skipping tests and declaring expected failures

### Skipping tests and expected failures

Added in version 3.1.

Skipping individual test methods, and even entire classes of tests, is something Unittest supports. On top of that, it lets you flag a test as an "expected failure" — one that is broken and bound to fail, yet ought not to count as a failure on a `TestResult`.

To skip a test, you simply apply the `skip()` [decorator](https://docs.python.org/3.14/glossary.html#term-decorator) or one of its conditional variants, call `TestCase.skipTest()` from inside a `setUp()` or test method, or raise `SkipTest` directly.

Here is what basic skipping looks like:

```python
class MyTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(mylib.__version__ < (1, 3),
                     "not supported in this library version")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass

    def test_maybe_skipped(self):
        if not external_resource_available():
            self.skipTest("external resource not available")
        # test code that depends on the external resource
        pass

```

Running the example above in verbose mode gives this output:

```python
test_format (__main__.MyTestCase.test_format) ... skipped 'not supported in this library version'
test_nothing (__main__.MyTestCase.test_nothing) ... skipped 'demonstrating skipping'
test_maybe_skipped (__main__.MyTestCase.test_maybe_skipped) ... skipped 'external resource not available'
test_windows_support (__main__.MyTestCase.test_windows_support) ... skipped 'requires Windows'

----------------------------------------------------------------------
Ran 4 tests in 0.005s

OK (skipped=4)

```

Whole classes can be skipped in the same way methods are:

```python
@unittest.skip("showing class skipping")
class MySkippedTestCase(unittest.TestCase):
    def test_not_run(self):
        pass

```

The test can also be skipped from inside `TestCase.setUp()`. That comes in handy when some resource that must be set up isn't available.

For expected failures, use the `expectedFailure()` decorator.

```python
class ExpectedFailureTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")

```

Writing your own skipping decorators is easy: just make a decorator that invokes `skip()` on the test whenever it decides the test should be skipped. The decorator below skips the test unless the object passed in carries a certain attribute:

```python
def skipUnlessHasattr(obj, attr):
    if hasattr(obj, attr):
        return lambda func: func
    return unittest.skip("{!r} doesn't have {!r}".format(obj, attr))

```

Test skipping and expected failures are implemented by the decorators and exception that follow:

[Subject index](INDEX.md) · [Previous](re-using-old-test-code.md) · [Continue](unittest-skiptest.md) · [Owning module, declaration or section: unittest](unittest-unit-testing-framework.md)
