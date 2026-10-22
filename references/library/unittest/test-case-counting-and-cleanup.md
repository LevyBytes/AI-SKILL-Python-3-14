# unittest: `countTestCases()`, `defaultTestResult()`, `id()`, `shortDescription()`, `addCleanup()`, `enterContext()`, `doCleanups()`, `addClassCleanup()`, `enterClassContext()`, `doClassCleanups()`

The diff size emitted by assert methods that show diffs on failure is capped by this attribute. Its default is 80*8 characters. The assert methods governed by it are `assertSequenceEqual()` (along with every sequence comparison method that delegates down to it), `assertDictEqual()` and `assertMultiLineEqual()`.

Assigning `None` to `maxDiff` removes any cap on diff length.

Added in version 3.2.

To gather details about a test, testing frameworks may call these methods:

 countTestCases()

Yields the count of tests that this test object stands for. With `TestCase` instances, the result is always `1`.

 defaultTestResult()

Yields an instance of the test result class appropriate for this test case class (used when no separate result instance gets handed to the `run()` method).

With `TestCase` instances, the returned value is always a `TestResult` instance; `TestCase` subclasses ought to override this where needed.

 id()

Yields a string that identifies the particular test case. Typically this is the full name of the test method, complete with the module and class name.

 shortDescription()

Hands back a description of the test, or `None` when no description exists. By default this method yields the opening line of the test method’s docstring when one is present, otherwise `None`.

Changed in version 3.1: With 3.1, the behavior shifted so the test name was appended to the short description even when a docstring existed. That broke compatibility with unittest extensions, so appending the test name was relocated to the `TextTestResult` in Python 3.2.

 addCleanup(*function*, */*, **args*, ***kwargs*)

Register a function to run after `tearDown()` so resources consumed by the test get released. The functions execute in the opposite order from how they were registered (LIFO). At call time they receive whatever positional and keyword arguments were supplied to `addCleanup()` upon registration.

Should `setUp()` fail, so that `tearDown()` never runs, the registered cleanup functions still get invoked.

Added in version 3.1.

 enterContext(*cm*)

Step into the given [context manager](https://docs.python.org/3.14/glossary.html#term-context-manager). On success, register its [`__exit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__exit__) method as a cleanup through `addCleanup()` as well, then hand back what the [`__enter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__enter__) method produced.

Added in version 3.11.

 doCleanups()

Regardless of conditions, this method runs after `tearDown()`, or after `setUp()` when `setUp()` throws an exception.

Its job is to invoke every cleanup function that `addCleanup()` registered. Should you need the cleanup functions invoked *prior* to `tearDown()`, you may invoke `doCleanups()` on your own.

`doCleanups()` removes methods from the cleanup-function stack one by one, so you can invoke it whenever you like.

Added in version 3.1.

 *classmethod *addClassCleanup(*function*, */*, **args*, ***kwargs*)

Register a function to run after `tearDownClass()` so resources consumed by the test class get released. The functions execute in the opposite order from how they were registered (LIFO). At call time they receive whatever positional and keyword arguments were supplied to `addClassCleanup()` upon registration.

Should `setUpClass()` fail, so that `tearDownClass()` never runs, the registered cleanup functions still get invoked.

Added in version 3.8.

 *classmethod *enterClassContext(*cm*)

Step into the given [context manager](https://docs.python.org/3.14/glossary.html#term-context-manager). On success, register its [`__exit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__exit__) method as a cleanup through `addClassCleanup()` as well, then hand back what the [`__enter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__enter__) method produced.

Added in version 3.11.

 *classmethod *doClassCleanups()

Regardless of conditions, this method runs after `tearDownClass()`, or after `setUpClass()` when `setUpClass()` throws an exception.

Its job is to invoke every cleanup function that `addClassCleanup()` registered. Should you need the cleanup functions invoked *prior* to `tearDownClass()`, you may invoke `doClassCleanups()` on your own.

`doClassCleanups()` removes methods from the cleanup-function stack one by one, so you can invoke it whenever you like.

Added in version 3.8.

[Subject index](INDEX.md) · [Continue](isolated-async-test-case-lifecycle.md) · [Owning module, declaration or section: unittest.TestCase](unittest-testcase-class.md) · [Owning module, declaration or section: Test cases](unittest-testcase-class.md) · [Owning module, declaration or section: maxDiff](unittest-testcase-assertlistequal-to-unittest-testcase-fail.md) · [Preceding source contract and version conditions](unittest-testcase-assertlistequal-to-unittest-testcase-fail.md)
