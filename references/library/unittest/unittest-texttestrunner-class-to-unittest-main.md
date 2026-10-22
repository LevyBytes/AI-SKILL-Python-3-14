# unittest: `unittest.TextTestRunner`, `_makeResult()`, `run()`, `unittest.main()`

*class *unittest.TextTestRunner(*stream=None*, *descriptions=True*, *verbosity=1*, *failfast=False*, *buffer=False*, *resultclass=None*, *warnings=None*, ***, *tb_locals=False*, *durations=None*)

A no-frills test runner that writes its results out to a stream. Should *stream* be `None` (the default), [`sys.stderr`](https://docs.python.org/3.14/library/sys.html#sys.stderr) serves as the output stream. While the class offers a handful of tunable parameters, at heart it stays quite plain. GUI programs that drive test suites are expected to supply their own runners instead, and those runners should take `**kwargs`, given that the way runners are constructed shifts as new unittest features land.

Out of the box, this runner surfaces [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning), [`PendingDeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#PendingDeprecationWarning), [`ResourceWarning`](https://docs.python.org/3.14/library/exceptions.html#ResourceWarning) and [`ImportWarning`](https://docs.python.org/3.14/library/exceptions.html#ImportWarning), even those that are normally [ignored by default](https://docs.python.org/3.14/library/warnings.html#warning-ignored). You can change this by reaching for Python's `-Wd` or `-Wa` options (refer to [Warning control](https://docs.python.org/3.14/using/cmdline.html#using-on-warnings)) and keeping *warnings* set to `None`.

Changed in version 3.2: Added the *warnings* parameter.

Changed in version 3.2: The default stream now resolves to [`sys.stderr`](https://docs.python.org/3.14/library/sys.html#sys.stderr) when the object is instantiated, no longer at the moment of import.

Changed in version 3.5: Added the *tb_locals* parameter.

Changed in version 3.12: Added the *durations* parameter.

 _makeResult()

This method hands back the `TestResult` instance that `run()` makes use of. You aren't meant to invoke it yourself, though a subclass may override it to swap in a custom `TestResult`.

What `_makeResult()` does is instantiate whatever class or callable was handed to the `TextTestRunner` constructor through its `resultclass` argument. Absent a `resultclass`, it falls back on `TextTestResult`. The result class gets built with these arguments:

```python
stream, descriptions, verbosity

```

 run(*test*)

Serving as the primary public entry point into the `TextTestRunner`, this method accepts either a `TestSuite` or a `TestCase` instance. It builds a `TestResult` via `_makeResult()`, runs the test(s), and writes the outcome to stdout.

 unittest.main(*module='__main__'*, *defaultTest=None*, *argv=None*, *testRunner=None*, *testLoader=unittest.defaultTestLoader*, *exit=True*, *verbosity=1*, *failfast=None*, *catchbreak=None*, *buffer=None*, *warnings=None*)

A command-line program that pulls a batch of tests out of *module* and executes them; its chief purpose is to let test modules be run with ease. The most basic way to use this function is to drop the line below at the foot of a test script:

```python
if __name__ == '__main__':
    unittest.main()

```

For more verbose reporting while your tests run, supply the verbosity argument:

```python
if __name__ == '__main__':
    unittest.main(verbosity=2)

```

The *defaultTest* argument holds either one test's name or an iterable of test names, to be run whenever *argv* names no tests. When it is left out or set to `None` and *argv* likewise carries no test names, every test discovered in *module* is run.

You may give the *argv* argument as a list of options for the program, where the leading element stands for the program name. Leave it out or pass `None`, and the contents of [`sys.argv`](https://docs.python.org/3.14/library/sys.html#sys.argv) are taken instead.

For the *testRunner* argument you may pass either a test runner class or an instance of one you have already built. Normally `main` invokes [`sys.exit()`](https://docs.python.org/3.14/library/sys.html#sys.exit) with a code that reports whether the run succeeded (0) or failed (1). A code of 5 means that nothing was run and nothing was skipped.

Your *testLoader* argument must be a `TestLoader` instance, and where you give none it falls back to `defaultTestLoader`.

You can drive `main` from the interactive interpreter by handing it the argument `exit=False`, which prints the outcome to standard output and skips the call to [`sys.exit()`](https://docs.python.org/3.14/library/sys.html#sys.exit):

```python
>>> from unittest import main
>>> main(module='test_module', exit=False)

```

As for the *failfast*, *catchbreak* and *buffer* parameters, each behaves just like its identically named command-line option.

The *warnings* argument sets the [warning filter](https://docs.python.org/3.14/library/warnings.html#warning-filter) to apply during the test run. Should you leave it unset, it stays `None` whenever a `-W` option is handed to **python** (consult [Warning control](https://docs.python.org/3.14/using/cmdline.html#using-on-warnings)); otherwise it takes the value `'default'`.

When you call `main`, what comes back is an object whose `result` attribute carries the run's outcome as a `unittest.TestResult`.

Changed in version 3.1: The *exit* parameter was added.

Changed in version 3.2: Introduced the *verbosity*, *failfast*, *catchbreak*, *buffer* and *warnings* parameters.

Changed in version 3.4: Broadened *defaultTest* so that it now takes an iterable of test names as well.

[Subject index](INDEX.md) · [Previous](unittest-texttestresult-class-to-unittest-defaulttestloader.md) · [Continue](load-tests-protocol.md) · [Owning module, declaration or section: Loading and running tests](unittest-testloader-class.md)
