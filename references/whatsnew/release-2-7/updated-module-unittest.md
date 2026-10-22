# What’s New in Python 2.7 / Updated module: unittest — unittest

### Updated module: unittest

The [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest) module received substantial improvements, and a large number of capabilities were introduced. Michael Foord implemented the bulk of these capabilities, except where stated otherwise. A separately downloadable build of the upgraded module, meant for Python releases 2.4 through 2.6, ships as the `unittest2` package, available from [unittest2](https://pypi.org/project/unittest2/).

Invoked at the command line, the module is able to locate tests on its own. While it lacks the sophistication of [py.test](https://pytest.org) or [nose](https://nose.readthedocs.io/), it offers a straightforward means of running tests held across a group of package directories. As an illustration, the command below will scan the `test/` subdirectory for any importable test files whose names match `test*.py`:

```python
python -m unittest discover -s test

```

For additional information, see the [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest) module documentation. (Developed in [bpo-6001](https://bugs.python.org/issue?@action=redirect&bpo=6001).)

A few other fresh options are now accepted by the [`main()`](https://docs.python.org/3.14/library/unittest.html#unittest.main) function:

- [`-b`](https://docs.python.org/3.14/library/unittest.html#cmdoption-unittest-b) or `--buffer` holds the standard output and standard error streams in a buffer while each test runs. Should the test succeed, whatever output it produced is thrown away; should it fail, the buffered output gets shown.

- [`-c`](https://docs.python.org/3.14/library/unittest.html#cmdoption-unittest-c) or `--catch` arranges for the control-C interrupt to receive gentler handling. Rather than halting the test process at once, the test currently in progress will finish and then the partial results gathered up to the point of interruption will be reported. For the impatient, hitting control-C a second time forces an immediate stop.

This control-C handler attempts to steer clear of trouble in cases where the code under test or the tests themselves have installed a signal handler of their own; it does so by detecting that a signal handler was previously registered and invoking it. Should that approach fail to suit you, a [`removeHandler()`](https://docs.python.org/3.14/library/unittest.html#unittest.removeHandler) decorator exists to flag tests whose control-C handling ought to be turned off.

- [`-f`](https://docs.python.org/3.14/library/unittest.html#cmdoption-unittest-f) or `--failfast` halts the test run the moment a test fails, rather than pressing on to run the remaining tests. (Suggested by Cliff Dyer and implemented by Michael Foord; [bpo-8074](https://bugs.python.org/issue?@action=redirect&bpo=8074).)

When run in verbose mode, the progress output now displays ‘x’ for expected failures and ‘u’ for unexpected successes. (Contributed by Benjamin Peterson.)

To skip a test, test cases may raise the [`SkipTest`](https://docs.python.org/3.14/library/unittest.html#unittest.SkipTest) exception ([bpo-1034053](https://bugs.python.org/issue?@action=redirect&bpo=1034053)).

When [`assertEqual()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertEqual), [`assertTrue()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertTrue), and [`assertFalse()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertFalse) fail, their error messages now carry more detail. Setting the [`longMessage`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.longMessage) attribute on your [`TestCase`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase) classes to true causes both the built-in error message and whatever extra message you supply to be printed on a failure. (Added by Michael Foord; [bpo-5663](https://bugs.python.org/issue?@action=redirect&bpo=5663).)

Called without a callable object to run, the [`assertRaises()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertRaises) method now hands back a context handler. As an example, you may write the following:

```python
with self.assertRaises(KeyError):
    {}['foo']

```

(Implemented by Antoine Pitrou; [bpo-4444](https://bugs.python.org/issue?@action=redirect&bpo=4444).)

Fixtures for setup and teardown at the module and class level are now available. A module may include [`setUpModule()`](https://docs.python.org/3.14/library/unittest.html#unittest.setUpModule) and [`tearDownModule()`](https://docs.python.org/3.14/library/unittest.html#unittest.tearDownModule) functions. A class may carry [`setUpClass()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.setUpClass) and [`tearDownClass()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.tearDownClass) methods, which have to be declared as class methods (by means of `@classmethod` or an equivalent). The test runner calls these functions and methods whenever it moves on to a test case belonging to a different module or class.

The [`addCleanup()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.addCleanup) and [`doCleanups()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.doCleanups) methods were introduced. With `addCleanup()` you can register cleanup functions that run no matter what (after [`setUp()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.setUp) when `setUp()` fails, otherwise after [`tearDown()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.tearDown)). This makes allocating and freeing resources during tests far more straightforward ([bpo-5679](https://bugs.python.org/issue?@action=redirect&bpo=5679)).

Several new methods were introduced to supply more specialized tests. A good many of these methods originated with Google engineers for their own test suites; Gregory P. Smith, Michael Foord, and GvR collaborated on folding them into Python’s edition of [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest).

- [`assertIsNone()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertIsNone) and [`assertIsNotNone()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertIsNotNone) accept a single expression and confirm that its result either is or is not `None`.

- [`assertIs()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertIs) and [`assertIsNot()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertIsNot) accept two values and determine whether or not those two values resolve to the same object. (Added by Michael Foord; [bpo-2578](https://bugs.python.org/issue?@action=redirect&bpo=2578).)

- [`assertIsInstance()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertIsInstance) and [`assertNotIsInstance()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertNotIsInstance) test whether the object in question is an instance of a given class, or of one class within a tuple of classes. (Added by Georg Brandl; [bpo-7031](https://bugs.python.org/issue?@action=redirect&bpo=7031).)

- [`assertGreater()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertGreater), [`assertGreaterEqual()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertGreaterEqual), [`assertLess()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertLess), and [`assertLessEqual()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertLessEqual) put two quantities up against each other.

- [`assertMultiLineEqual()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertMultiLineEqual) puts two strings side by side, and when they differ, it presents a useful comparison spotlighting where the two strings diverge. This comparison now happens automatically whenever Unicode strings are checked with [`assertEqual()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertEqual).

- [`assertRegexpMatches()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertRegex) and [`assertNotRegexpMatches()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertNotRegex) verify whether the first argument is a string that does or does not match the regular expression given as the second argument ([bpo-8038](https://bugs.python.org/issue?@action=redirect&bpo=8038)).

- [`assertRaisesRegexp()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertRaisesRegex) verifies that a given exception gets raised, and in addition confirms that the exception’s string representation matches the supplied regular expression.

- [`assertIn()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertIn) and [`assertNotIn()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertNotIn) check whether *first* is or is not contained in *second*.

- [`assertItemsEqual()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertCountEqual) checks whether two supplied sequences hold the same elements.

- [`assertSetEqual()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertSetEqual) checks whether two sets match, and on an error it reports only the points where the sets differ.

- In the same vein, [`assertListEqual()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertListEqual) and [`assertTupleEqual()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertTupleEqual) put the named types up against each other and lay out any differences without always printing the values in full; these methods now run automatically when lists and tuples are compared via [`assertEqual()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertEqual). On a broader note, [`assertSequenceEqual()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertSequenceEqual) puts two sequences side by side and can additionally verify whether both sequences belong to a given type.

- [`assertDictEqual()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertDictEqual) puts two dictionaries up against each other and reports the differences; it now runs automatically when you compare two dictionaries through [`assertEqual()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertEqual). `assertDictContainsSubset()` verifies that each key/value pair found in *first* also appears in *second*.

- [`assertAlmostEqual()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertAlmostEqual) and [`assertNotAlmostEqual()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertNotAlmostEqual) check whether *first* and *second* come out roughly equal. The method may either round their difference to an optionally given number of *places* (with 7 as the default) and weigh it against zero, or insist that the difference stay below a provided *delta* value.

- [`loadTestsFromName()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestLoader.loadTestsFromName) correctly respects the [`suiteClass`](https://docs.python.org/3.14/library/unittest.html#unittest.TestLoader.suiteClass) attribute belonging to the [`TestLoader`](https://docs.python.org/3.14/library/unittest.html#unittest.TestLoader). (Fixed by Mark Roddy; [bpo-6866](https://bugs.python.org/issue?@action=redirect&bpo=6866).)

- A fresh hook allows you to broaden the [`assertEqual()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertEqual) method so it copes with new data types. The [`addTypeEqualityFunc()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.addTypeEqualityFunc) method accepts a type object together with a function. That function comes into play when both objects under comparison are of the named type. It ought to compare the two objects and raise an exception when they fail to match; ideally the function should also explain why the two objects don’t line up, in much the same way the new sequence comparison methods do.

[`unittest.main()`](https://docs.python.org/3.14/library/unittest.html#unittest.main) now accepts an optional `exit` argument. When false, `main()` skips the call to [`sys.exit()`](https://docs.python.org/3.14/library/sys.html#sys.exit), which lets `main()` be driven from the interactive interpreter. (Contributed by J. Pablo Fernández; [bpo-3379](https://bugs.python.org/issue?@action=redirect&bpo=3379).)

[`TestResult`](https://docs.python.org/3.14/library/unittest.html#unittest.TestResult) gains new [`startTestRun()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestResult.startTestRun) and [`stopTestRun()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestResult.stopTestRun) methods, which are invoked right before and right after a test run. (Contributed by Robert Collins; [bpo-5728](https://bugs.python.org/issue?@action=redirect&bpo=5728).)

On account of all these additions, `unittest.py` had grown unwieldy in size, so the module was converted into a package and its code divided across multiple files (by Benjamin Peterson). None of this alters the way the module is imported or used.

See also

[https://web.archive.org/web/20210619163128/http://www.voidspace.org.uk/python/articles/unittest2.shtml](https://web.archive.org/web/20210619163128/http://www.voidspace.org.uk/python/articles/unittest2.shtml)

Covers the new features, the way to use them, and the reasoning behind the various design choices. (By Michael Foord.)

[Subject index](INDEX.md) · [Previous source section](ttk-themed-widgets-for-tk.md) · [Release/subject declaration](the-future-for-python-2-x.md) · [Next source section](updated-module-elementtree-1-3.md)
