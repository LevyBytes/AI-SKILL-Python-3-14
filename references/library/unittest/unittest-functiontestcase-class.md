# unittest: `unittest.FunctionTestCase`

*class *unittest.FunctionTestCase(*testFunc*, *setUp=None*, *tearDown=None*, *description=None*)

This class supplies the slice of the `TestCase` interface that lets the test runner drive the test, yet it omits the methods that test code uses to verify and report errors. Its purpose is to build test cases from legacy test code so that code can fold into a `unittest`-based test framework.

[Subject index](INDEX.md) · [Previous](isolated-async-test-case-lifecycle.md) · [Continue](unittest-testsuite-class.md) · [Owning module, declaration or section: Test cases](unittest-testcase-class.md)
