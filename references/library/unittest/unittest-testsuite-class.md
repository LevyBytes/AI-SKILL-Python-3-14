# unittest: `unittest.TestSuite`

### Grouping tests

 *class *unittest.TestSuite(*tests=()*)

A collection of separate test cases and test suites is what this class stands for. It offers the interface the test runner needs to run it like any other test case. Executing a `TestSuite` instance amounts to looping over the suite and running each test one by one.

When *tests* is supplied, it has to be an iterable of separate test cases or further test suites used to seed the suite at the start. Further methods exist for appending test cases and suites to the collection afterward.

`TestSuite` objects act largely like `TestCase` objects, except that they do not really implement a test. Their role instead is to bundle tests into groups meant to run together. A few extra methods let you append tests to `TestSuite` instances:

[Subject index](INDEX.md) · [Previous](unittest-functiontestcase-class.md) · [Continue](unittest-testsuite-addtest-to-unittest-testsuite-iter.md)
