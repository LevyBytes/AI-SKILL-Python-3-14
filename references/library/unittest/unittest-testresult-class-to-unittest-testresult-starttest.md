# unittest: `unittest.TestResult`, `wasSuccessful()`, `stop()`, `startTest()`

*class *unittest.TestResult

This class serves to assemble information on which tests passed and which fell short.

A `TestResult` object retains the outcomes of a group of tests. The `TestCase` and `TestSuite` classes see to it that outcomes are recorded correctly; test authors need not concern themselves with logging the result of tests.

Testing frameworks layered on `unittest` may wish to reach the `TestResult` object produced by running a group of tests for reporting purposes; the `TestRunner.run()` method returns a `TestResult` instance to that end.

When you examine the outcome of running a group of tests, these attributes on `TestResult` instances are the noteworthy ones:

 errors

A list holding 2-tuples of `TestCase` instances together with strings carrying formatted tracebacks. Every tuple stands for a test that threw an unexpected exception.

 failures

A list holding 2-tuples of `TestCase` instances together with strings carrying formatted tracebacks. Every tuple stands for a test where a failure was deliberately flagged through the assert* methods.

 skipped

A list holding 2-tuples of `TestCase` instances together with strings carrying the reason the test was skipped.

Added in version 3.1.

 expectedFailures

A list holding 2-tuples of `TestCase` instances together with strings carrying formatted tracebacks. Every tuple stands for an expected failure or error of the test case.

 unexpectedSuccesses

A list holding `TestCase` instances that were flagged as expected failures yet passed.

 collectedDurations

A list holding 2-tuples of test case names together with floats giving the elapsed time of each test that ran.

Added in version 3.12.

 shouldStop

Becomes `True` once test execution ought to halt via `stop()`.

 testsRun

The running total of tests executed thus far.

 buffer

When set to true, `sys.stdout` and `sys.stderr` get buffered across the span between `startTest()` and `stopTest()` being invoked. The gathered output only reaches the real `sys.stdout` and `sys.stderr` if the test fails or errors. Any such output also rides along with the failure / error message.

Added in version 3.2.

 failfast

When set to true, `stop()` gets invoked at the first failure or error, halting the test run.

Added in version 3.2.

 tb_locals

When set to true, local variables get displayed in tracebacks.

Added in version 3.5.

 wasSuccessful()

Returns `True` when every test run thus far has passed, otherwise yields `False`.

Changed in version 3.4: Yields `False` whenever any `unexpectedSuccesses` came from tests carrying the `expectedFailure()` decorator.

 stop()

You can invoke this method to indicate that the running set of tests ought to be aborted, by flipping the `shouldStop` attribute to `True`. `TestRunner` objects should honor this flag and return without executing any further tests.

For instance, the `TextTestRunner` class uses this feature to halt the test framework when a user signals a keyboard interrupt. Interactive tools that supply `TestRunner` implementations can apply it the same way.

The following methods of the `TestResult` class serve to keep the internal data structures up to date and may be extended in subclasses to meet extra reporting needs. This proves especially handy for building tools that offer interactive reporting as tests run.

 startTest(*test*)

Invoked when the test case *test* is about to run.

[Subject index](INDEX.md) · [Previous](unittest-testloader-discover.md) · [Continue](test-result-completion-error-and-expected-failure.md) · [Owning module, declaration or section: Loading and running tests](unittest-testloader-class.md)
