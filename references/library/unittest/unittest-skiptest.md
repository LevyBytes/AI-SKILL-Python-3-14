# unittest: `unittest.skip()`, `unittest.skipIf()`, `unittest.skipUnless()`, `unittest.expectedFailure`, `unittest.SkipTest`

@unittest.skip(*reason*)

Skip the decorated test unconditionally. The *reason* ought to spell out why the test is being skipped.

 @unittest.skipIf(*condition*, *reason*)

Skip the decorated test if *condition* is true.

 @unittest.skipUnless(*condition*, *reason*)

Skip the decorated test unless *condition* is true.

 @unittest.expectedFailure

Flag the test as an expected failure or error. Should the test fail or error within the test function itself (as opposed to within one of the *test fixture* methods), it counts as a success. Should the test pass, it counts as a failure.

 *exception *unittest.SkipTest(*reason*)

Raising this exception skips a test.

In general you can reach for `TestCase.skipTest()` or one of the skipping decorators rather than raising this on your own.

Tests that are skipped won't have `setUp()` or `tearDown()` run around them. Skipped classes won't have `setUpClass()` or `tearDownClass()` run. Skipped modules won't have `setUpModule()` or `tearDownModule()` run.

[Subject index](INDEX.md) · [Previous](skipping-tests-and-expected-failures.md) · [Continue](distinguishing-test-iterations-using-subtests.md) · [Owning module, declaration or section: unittest](unittest-unit-testing-framework.md) · [Owning module, declaration or section: Skipping tests and expected failures](skipping-tests-and-expected-failures.md)
