# unittest: `addTest()`, `addTests()`, `run()`, `debug()`, `countTestCases()`, `__iter__()`

addTest(*test*)

Append a `TestCase` or `TestSuite` to the suite.

 addTests(*tests*)

Append every test drawn from an iterable of `TestCase` and `TestSuite` instances into this test suite.

This amounts to looping over *tests* and invoking `addTest()` on each item.

`TestSuite` shares the following methods with `TestCase`:

 run(*result*)

Execute the tests belonging to this suite, gathering the outcome into the test result object handed in as *result*. Be aware that, in contrast to `TestCase.run()`, `TestSuite.run()` demands the result object as an argument.

 debug()

Execute the tests belonging to this suite while gathering no result. This lets exceptions thrown by the test propagate up to the caller and serves to support running tests beneath a debugger.

 countTestCases()

Yields the count of tests this test object stands for, counting all separate tests plus sub-suites.

 __iter__()

Tests bundled within a `TestSuite` are reached solely through iteration. Subclasses may furnish tests lazily by overriding `__iter__()`. Keep in mind that a single suite may have this method invoked more than once (say, while counting tests or checking for equality), so the tests yielded by repeated iterations ahead of `TestSuite.run()` have to match on every call iteration. Following `TestSuite.run()`, callers ought not depend on the tests this method yields unless they rely on a subclass overriding `TestSuite._removeTestAtIndex()` to keep test references.

Changed in version 3.2: Before this release the `TestSuite` reached tests directly instead of via iteration, so an override of `__iter__()` did not suffice to supply tests.

Changed in version 3.4: Before this release the `TestSuite` retained references to every `TestCase` once `TestSuite.run()` finished. Subclasses may reinstate that behavior by overriding `TestSuite._removeTestAtIndex()`.

When a `TestSuite` object is used as usual, a `TestRunner` invokes the `run()` method rather than the end-user test harness.

[Subject index](INDEX.md) · [Previous](unittest-testsuite-class.md) · [Continue](unittest-testloader-class.md) · [Owning module, declaration or section: unittest.TestSuite](unittest-testsuite-class.md) · [Owning module, declaration or section: Grouping tests](unittest-testsuite-class.md)
