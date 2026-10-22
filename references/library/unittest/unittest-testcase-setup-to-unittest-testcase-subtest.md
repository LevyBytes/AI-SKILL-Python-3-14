# unittest: `setUp()`, `tearDown()`, `setUpClass()`, `tearDownClass()`, `run()`, `skipTest()`, `subTest()`

setUp()

Invoked to set up the test fixture. It fires right before the test method runs; aside from [`AssertionError`](https://docs.python.org/3.14/library/exceptions.html#AssertionError) or `SkipTest`, whatever exception this method throws is treated as an error and not a test failure. By default this method is a no-op.

 tearDown()

Invoked right after the test method finishes and its result has been logged. It runs even when the test method threw, so subclass implementations may have to take special care when inspecting internal state. With the exception of [`AssertionError`](https://docs.python.org/3.14/library/exceptions.html#AssertionError) or `SkipTest`, any exception this method throws counts as one more error rather than a test failure (so the tally of reported errors goes up). It runs only when `setUp()` has succeeded, no matter how the test method turned out. By default this method is a no-op.

 setUpClass()

A class-level method that fires before the tests within one class execute. `setUpClass` receives the class as its sole argument and has to carry the [`classmethod()`](https://docs.python.org/3.14/library/functions.html#classmethod) decorator:

```python
@classmethod
def setUpClass(cls):
    ...

```

See Class and Module Fixtures for more details.

Added in version 3.2.

 tearDownClass()

A class-level method that fires once the tests within one class have finished. `tearDownClass` receives the class as its sole argument and has to carry the [`classmethod()`](https://docs.python.org/3.14/library/functions.html#classmethod) decorator:

```python
@classmethod
def tearDownClass(cls):
    ...

```

See Class and Module Fixtures for more details.

Added in version 3.2.

 run(*result=None*)

Execute the test, accumulating the outcome into the `TestResult` object handed in as *result*. When *result* is left out or is `None`, a throwaway result object gets built (via the `defaultTestResult()` method) and used instead. That result object is then handed back to whoever called `run()`.

You can get the identical behavior just by invoking the `TestCase` instance itself.

Changed in version 3.3: in earlier releases `run` handed back nothing, and invoking the instance behaved the same way.

 skipTest(*reason*)

Invoking this from within a test method or `setUp()` causes the present test to be skipped. See Skipping tests and expected failures for more information.

Added in version 3.1.

 subTest(*msg=None*, ***params*)

Yield a context manager that runs the wrapped block of code as a subtest. The optional *msg* and *params* are arbitrary values shown each time a subtest fails, so you can pinpoint them without ambiguity.

One test case may hold as many subtest declarations as you like, and those declarations may be nested to any depth.

See Distinguishing test iterations using subtests for more information.

Added in version 3.4.

[Subject index](INDEX.md) · [Previous](unittest-testcase-class.md) · [Continue](test-debugging-equality-and-instance-assertions.md) · [Owning module, declaration or section: unittest.TestCase](unittest-testcase-class.md) · [Owning module, declaration or section: Test cases](unittest-testcase-class.md)
