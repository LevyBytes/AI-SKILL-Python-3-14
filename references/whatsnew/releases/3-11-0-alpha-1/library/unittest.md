# Python 3.11.0 alpha 1 / library / unittest

[bpo-30856](https://bugs.python.org/issue?@action=redirect&bpo=30856): The [`unittest.TestResult`](https://docs.python.org/3.14/library/unittest.html#unittest.TestResult) methods [`addFailure()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestResult.addFailure), [`addError()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestResult.addError), [`addSkip()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestResult.addSkip), and [`addSubTest()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestResult.addSubTest) now fire the moment a test raises an exception or a subtest concludes. Earlier they fired only once the test cleanup had wrapped up.

[bpo-25894](https://bugs.python.org/issue?@action=redirect&bpo=25894): [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest) henceforth splits skipped subtests from failed ones in every report: distinct characters in default mode and distinct lines under verbose mode. Additionally, the test description now prints for errors arising in method, class, and module cleanups.

[bpo-5846](https://bugs.python.org/issue?@action=redirect&bpo=5846): The [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest) functions below were deprecated, with removal targeted for Python 3.13:

  - `findTestCases()`

  - `makeSuite()`

  - `getTestCaseNames()`

Use [`TestLoader`](https://docs.python.org/3.14/library/unittest.html#unittest.TestLoader) methods instead:

  - [`unittest.TestLoader.loadTestsFromModule()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestLoader.loadTestsFromModule)

  - [`unittest.TestLoader.loadTestsFromTestCase()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestLoader.loadTestsFromTestCase)

  - [`unittest.TestLoader.getTestCaseNames()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestLoader.getTestCaseNames)

Erlend E. Aasland authored the change.

[bpo-36674](https://bugs.python.org/issue?@action=redirect&bpo=36674): When either the surrounding class or the individual test method carries a skipping decorator, [`unittest.TestCase.debug()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.debug) will now raise [`unittest.SkipTest`](https://docs.python.org/3.14/library/unittest.html#unittest.SkipTest).

[bpo-45162](https://bugs.python.org/issue?@action=redirect&bpo=45162): Stripped out a batch of long-deprecated [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest) capabilities:

  - The ?`fail*`? plus ?`assert*`? aliases that shadowed [`TestCase`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase) methods.

[bpo-41620](https://bugs.python.org/issue?@action=redirect&bpo=41620): [`run()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.run) now invariably hands back a [`TestResult`](https://docs.python.org/3.14/library/unittest.html#unittest.TestResult) instance. It used to hand back `None` whenever the test class or method bore a skipping decorator.

[bpo-43913](https://bugs.python.org/issue?@action=redirect&bpo=43913): Cleared up defects in how [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest) tears down classes and modules:

  - Anything registered via [`addModuleCleanup()`](https://docs.python.org/3.14/library/unittest.html#unittest.addModuleCleanup) went uncalled unless the user had declared `tearDownModule()` somewhere in their test module.

  - Anything registered via [`addClassCleanup()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.addClassCleanup) went uncalled if `tearDownClass` had been set to `None`.

  - The buffering inside [`TestResult`](https://docs.python.org/3.14/library/unittest.html#unittest.TestResult) failed to cooperate with anything registered through `addClassCleanup()` and `addModuleCleanup()`.

  - Failures inside functions registered with `addClassCleanup()` and `addModuleCleanup()` were mishandled while running in buffered and debug modes.

  - Failures within `setUpModule()` and within functions registered via `addModuleCleanup()` surfaced out of order.

  - Plus a handful of smaller defects.

[bpo-44955](https://bugs.python.org/issue?@action=redirect&bpo=44955): The [`stopTestRun()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestResult.stopTestRun) method is now invariably paired with a [`startTestRun()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestResult.startTestRun) call on the [`TestResult`](https://docs.python.org/3.14/library/unittest.html#unittest.TestResult) objects that [`run()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.run) creates implicitly. Earlier it stayed uncalled for test methods and classes that carried a skipping decorator.

[bpo-44911](https://bugs.python.org/issue?@action=redirect&bpo=44911): [`IsolatedAsyncioTestCase`](https://docs.python.org/3.14/library/unittest.html#unittest.IsolatedAsyncioTestCase) will stop raising an exception while it cancels leaked tasks. Bar Harel authored this patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
