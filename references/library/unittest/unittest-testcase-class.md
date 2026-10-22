# unittest: `unittest.TestCase`

### Test cases

 *class *unittest.TestCase(*methodName='runTest'*)

Within the `unittest` world, instances of the `TestCase` class stand for the individual logical units of testing. The design intent is for this class to serve as a base, where concrete subclasses supply the actual tests. It supplies the interface the test runner relies on to drive each test, plus the methods that test code calls to detect and report the various failure kinds.

A given `TestCase` instance executes exactly one base method — the one called *methodName*. For the vast majority of `TestCase` work, you will leave *methodName* alone and keep the default `runTest()` method as-is rather than overriding it.

Changed in version 3.2: you can now construct a `TestCase` with no *methodName* supplied at all. That eases trying out `TestCase` directly within the interactive interpreter.

A `TestCase` instance exposes three categories of methods: one set drives the test run, a second set is what the test body uses to assert conditions and flag failures, and a final set offers inquiry calls for collecting details about the test itself.

The first category (driving the test run) comprises:

[Subject index](INDEX.md) · [Continue](unittest-testcase-setup-to-unittest-testcase-subtest.md)
