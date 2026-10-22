# Class and Module Fixtures

### Class and Module Fixtures

It is `TestSuite` that carries out fixtures at the class and module level. As soon as the suite meets a test belonging to a fresh class, it runs `tearDownClass()` for the class that came before (if there was one), then runs `setUpClass()` for the new class.

In much the same way, when a test comes from a module other than the prior test's, `tearDownModule` for the earlier module runs first, with `setUpModule` for the new module following.

Once every test has finished, the closing `tearDownClass` and `tearDownModule` are run.

Bear in mind that shared fixtures sit uneasily with [potential] capabilities such as test parallelization, and they undercut test isolation. Use them sparingly.

By default, the unittest test loaders arrange tests so that everything from one module and class sits together. The upshot is that `setUpClass` / `setUpModule` (and so on) fire precisely once for each class and module. Shuffle that order, however, so that tests from differing modules and classes end up side by side, and those shared fixture functions can fire several times across one run.

Suites whose ordering departs from the standard are not meant to use shared fixtures. For frameworks that would rather skip shared-fixture support, a `BaseTestSuite` is still available.

Whenever an exception surfaces inside one of the shared fixture functions, the test gets logged as an error. As there is no matching test instance to attach it to, an `_ErrorHolder` object - which mirrors the interface of a `TestCase` - stands in for that error. If you stick to the standard unittest test runner this nuance won't concern you, but as a framework author you may find it pertinent.

[Subject index](INDEX.md) · [Previous](load-tests-protocol.md) · [Continue](setupclass-and-teardownclass.md)
