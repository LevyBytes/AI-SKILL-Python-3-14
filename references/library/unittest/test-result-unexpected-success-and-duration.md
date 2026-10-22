# unittest: `addUnexpectedSuccess()`, `addSubTest()`, `addDuration()`

In its default form, the method tacks a tuple `(test, formatted_err)` onto the instance's `expectedFailures` attribute; here *formatted_err* is a traceback that has been formatted out of *err*.

 addUnexpectedSuccess(*test*)

Invoked when a test case *test* carrying the `expectedFailure()` decorator ends up passing anyway.

By default, the method adds the test onto the instance's `unexpectedSuccesses` attribute.

 addSubTest(*test*, *subtest*, *outcome*)

Invoked once a subtest wraps up. The *test* here is the test case that maps to the test method, while *subtest* is a bespoke `TestCase` instance that characterizes the subtest.

A *outcome* of [`None`](https://docs.python.org/3.14/library/constants.html#None) signals that the subtest passed. If it didn't, an exception was raised and *outcome* holds a tuple shaped like the one [`sys.exc_info()`](https://docs.python.org/3.14/library/sys.html#sys.exc_info) gives back: `(type, value, traceback)`.

On a successful outcome the default implementation takes no action; failing subtests, meanwhile, it logs the same way it would ordinary failures.

Added in version 3.4.

 addDuration(*test*, *elapsed*)

Invoked once the test case wraps up. The *elapsed* value gives the duration in seconds, counting the running of cleanup functions as well.

Added in version 3.12.

[Subject index](INDEX.md) · [Continue](unittest-texttestresult-class-to-unittest-defaulttestloader.md) · [Owning module, declaration or section: unittest.TestResult](unittest-testresult-class-to-unittest-testresult-starttest.md) · [Owning module, declaration or section: Loading and running tests](unittest-testloader-class.md) · [Owning module, declaration or section: addExpectedFailure](test-result-completion-error-and-expected-failure.md) · [Preceding source contract and version conditions](test-result-completion-error-and-expected-failure.md)
