# unittest: `stopTest()`, `startTestRun()`, `stopTestRun()`, `addError()`, `addFailure()`, `addSuccess()`, `addSkip()`, `addExpectedFailure()`

stopTest(*test*)

Invoked once the test case *test* has run, no matter the outcome.

 startTestRun()

Invoked one time before any tests run.

Added in version 3.1.

 stopTestRun()

Invoked one time after all tests run.

Added in version 3.1.

 addError(*test*, *err*)

Invoked when the test case *test* throws an unexpected exception. *err* is a tuple shaped like the one [`sys.exc_info()`](https://docs.python.org/3.14/library/sys.html#sys.exc_info) returns: `(type, value, traceback)`.

By default it appends a tuple `(test, formatted_err)` onto the instance’s `errors` attribute, where *formatted_err* is a formatted traceback built from *err*.

 addFailure(*test*, *err*)

Invoked when the test case *test* flags a failure. *err* is a tuple shaped like the one [`sys.exc_info()`](https://docs.python.org/3.14/library/sys.html#sys.exc_info) returns: `(type, value, traceback)`.

By default it appends a tuple `(test, formatted_err)` onto the instance’s `failures` attribute, where *formatted_err* is a formatted traceback built from *err*.

 addSuccess(*test*)

Invoked when the test case *test* passes.

By default it performs no action.

 addSkip(*test*, *reason*)

Invoked upon the test case *test* being skipped. *reason* holds whatever justification the test offered for the skip.

By default it appends a tuple `(test, reason)` onto the instance’s `skipped` attribute.

 addExpectedFailure(*test*, *err*)

Invoked when the test case *test* fails or errors, yet was marked with the `expectedFailure()` decorator.

[Subject index](INDEX.md) · [Previous](unittest-testresult-class-to-unittest-testresult-starttest.md) · [Owning module, declaration or section: unittest.TestResult](unittest-testresult-class-to-unittest-testresult-starttest.md) · [Owning module, declaration or section: Loading and running tests](unittest-testloader-class.md) · [Required continuation of the source contract](test-result-unexpected-success-and-duration.md)
