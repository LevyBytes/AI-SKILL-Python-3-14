# unittest: `unittest.IsolatedAsyncioTestCase`, `asyncSetUp()`, `asyncTearDown()`, `addAsyncCleanup()`, `enterAsyncContext()`, `run()`

*class *unittest.IsolatedAsyncioTestCase(*methodName='runTest'*)

This class exposes an API resembling `TestCase` while additionally permitting coroutines to serve as test functions.

Added in version 3.8.

 loop_factory

The *loop_factory* handed to [`asyncio.Runner`](https://docs.python.org/3.14/library/asyncio-runner.html#asyncio.Runner). In subclasses, override it with [`asyncio.EventLoop`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.EventLoop) so the asyncio policy system is bypassed.

Added in version 3.13.

 *async *asyncSetUp()

Invoked to set up the test fixture. It runs after `TestCase.setUp()`. It runs just before the test method is invoked; apart from [`AssertionError`](https://docs.python.org/3.14/library/exceptions.html#AssertionError) or `SkipTest`, any exception this method throws counts as an error instead of a test failure. By default it performs no action.

 *async *asyncTearDown()

Invoked right after the test method has run and the result was recorded. It runs ahead of `tearDown()`. It runs even when the test method threw an exception, so subclass implementations may have to be especially cautious about verifying internal state. Apart from [`AssertionError`](https://docs.python.org/3.14/library/exceptions.html#AssertionError) or `SkipTest`, any exception this method throws counts as an extra error instead of a test failure (which raises the overall tally of reported errors). It runs only when `asyncSetUp()` succeeds, no matter how the test method turns out. By default it performs no action.

 addAsyncCleanup(*function*, */*, **args*, ***kwargs*)

A coroutine usable as a cleanup function may be passed to this method.

 *async *enterAsyncContext(*cm*)

Step into the given [asynchronous context manager](https://docs.python.org/3.14/glossary.html#term-asynchronous-context-manager). On success, register its [`__aexit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__aexit__) method as a cleanup through `addAsyncCleanup()` as well, then hand back what the [`__aenter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__aenter__) method produced.

Added in version 3.11.

 run(*result=None*)

Establishes a fresh event loop for running the test, gathering the outcome into the `TestResult` object handed in as *result*. When *result* is left out or set to `None`, a throwaway result object gets built (via the `defaultTestResult()` method) and used. The caller of `run()` receives the result object back. Once the test finishes, every task in the event loop is cancelled.

An example illustrating the order:

```python
from unittest import IsolatedAsyncioTestCase

events = []

class Test(IsolatedAsyncioTestCase):

    def setUp(self):
        events.append("setUp")

    async def asyncSetUp(self):
        self._async_connection = await AsyncConnection()
        events.append("asyncSetUp")

    async def test_response(self):
        events.append("test_response")
        response = await self._async_connection.get("https://example.com")
        self.assertEqual(response.status_code, 200)
        self.addAsyncCleanup(self.on_cleanup)

    def tearDown(self):
        events.append("tearDown")

    async def asyncTearDown(self):
        await self._async_connection.close()
        events.append("asyncTearDown")

    async def on_cleanup(self):
        events.append("cleanup")

if __name__ == "__main__":
    unittest.main()

```

Once the test has run, `events` will hold `["setUp", "asyncSetUp", "test_response", "asyncTearDown", "tearDown", "cleanup"]`.

[Subject index](INDEX.md) · [Previous](test-case-counting-and-cleanup.md) · [Continue](unittest-functiontestcase-class.md) · [Owning module, declaration or section: Test cases](unittest-testcase-class.md)
