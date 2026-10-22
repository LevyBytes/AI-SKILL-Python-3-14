# unittest: `loadTestsFromTestCase()`, `loadTestsFromModule()`, `loadTestsFromName()`, `loadTestsFromNames()`, `getTestCaseNames()`

errors

The non-fatal errors run into while tests were loaded are kept in this list. The loader never clears it. Fatal errors get flagged by the responsible method throwing an exception up to the caller. Non-fatal errors additionally show up as a synthetic test that throws the original error once run.

Added in version 3.5.

`TestLoader` objects have the following methods:

 loadTestsFromTestCase(*testCaseClass*)

Yields a suite holding every test case found in the `TestCase`-derived `testCaseClass`.

One test case instance gets built for every method that `getTestCaseNames()` names. By default those are the method names that start with `test`. When `getTestCaseNames()` returns no methods yet the `runTest()` method exists, one test case is built for that method instead.

 loadTestsFromModule(*module*, ***, *pattern=None*)

Yields a suite holding every test case found in the supplied module. This method scans *module* for classes that derive from `TestCase` and builds one class instance per test method defined on the class.

Note

Although a hierarchy of `TestCase`-derived classes can help with sharing fixtures and helper functions, declaring test methods on base classes never meant for direct instantiation does not mesh well with this method. Even so, doing it can pay off when the fixtures differ and live in subclasses.

When a module supplies a `load_tests` function, it gets invoked to load the tests. This lets modules tailor how tests load. This is the load_tests protocol. The *pattern* argument is handed in as the third argument to `load_tests`.

Changed in version 3.2: Support for `load_tests` added.

Changed in version 3.5: A keyword-only *pattern* argument is now supported.

Changed in version 3.12: The unofficial, undocumented *use_load_tests* parameter is now gone.

 loadTestsFromName(*name*, *module=None*)

Yields a suite holding every test case derived from a string specifier.

The specifier *name* is a “dotted name” that can resolve to a module, a test case class, a test method inside a test case class, a `TestSuite` instance, or a callable object yielding a `TestCase` or `TestSuite` instance. The checks run in the sequence listed here; that is, a method on a candidate test case class gets treated as “a test method within a test case class” instead of “a callable object”.

As an example, suppose you have a module `SampleTests` holding a `TestCase`-derived class `SampleTestCase` with three test methods (`test_one()`, `test_two()`, and `test_three()`); the specifier `'SampleTests.SampleTestCase'` would make this method yield a suite running all three test methods. With the specifier `'SampleTests.SampleTestCase.test_two'` it would yield a test suite running only the `test_two()` test method. The specifier may point at modules and packages not yet imported; they get imported as a side-effect.

The method can optionally resolve *name* against the supplied *module*.

Changed in version 3.5: Should an [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError) or [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) arise while walking *name*, what gets returned is a synthetic test that throws that error once run. Such errors are folded into the errors gathered by self.errors.

 loadTestsFromNames(*names*, *module=None*)

Akin to `loadTestsFromName()`, except it accepts a sequence of names instead of one name. What it returns is a test suite carrying all the tests defined under each name.

 getTestCaseNames(*testCaseClass*)

Yields a sorted sequence of the method names located in *testCaseClass*; this ought to be a subclass of `TestCase`.

[Subject index](INDEX.md) · [Previous](unittest-testloader-class.md) · [Continue](unittest-testloader-discover.md) · [Owning module, declaration or section: unittest.TestLoader](unittest-testloader-class.md) · [Owning module, declaration or section: Loading and running tests](unittest-testloader-class.md)
