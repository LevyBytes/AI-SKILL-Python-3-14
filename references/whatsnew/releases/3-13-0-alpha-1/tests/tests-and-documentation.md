# Python 3.13.0 alpha 1 / tests / tests and documentation

[gh-107178](https://github.com/python/cpython/issues/107178): Introduced the C API test for functions belonging to the Mapping Protocol, the Sequence Protocol, plus a handful of functions in the Object Protocol.

[gh-106714](https://github.com/python/cpython/issues/106714): test_capi: Repaired test_no_FatalError_infinite_loop() so it no longer writes a coredump, by leaning on test.support.SuppressCrashReport. Victor Stinner authored the patch.

[gh-109566](https://github.com/python/cpython/issues/109566): regrtest: Introduced the `--fast-ci` plus `--slow-ci` options. `--fast-ci` applies a 10-minute default timeout together with `-u all,-cpu` (omit the slowest tests). `--slow-ci` applies a 20-minute default timeout together with `-u all` (exercise every test). Victor Stinner authored the patch.

[gh-109425](https://github.com/python/cpython/issues/109425): libregrtest now decodes the stdout of test worker processes using the ?backslashreplace? error handler in order to log mangled stdout, in place of erroring out and dropping the stdout. Victor Stinner authored the patch.

[gh-108996](https://github.com/python/cpython/issues/108996): Introduced tests covering `msvcrt`.

[gh-108851](https://github.com/python/cpython/issues/108851): Repaired the `test_tomllib` recursion tests for WASI buildbots by lowering the recursion limit and deriving the deepest nested array/dict from whatever recursion limit is presently available. Victor Stinner authored the patch.

[gh-108834](https://github.com/python/cpython/issues/108834): Added a `--fail-rerun option` option onto regrtest: whenever a test fails and then passes once rerun under verbose mode, terminate the process with exit code 2 (error) in place of exit code 0 (success). Victor Stinner authored the patch.

[gh-110267](https://github.com/python/cpython/issues/110267): Introduced tests covering the pickling and copying of PyStructSequence objects. Xuehai Pan supplied the patch.

[gh-110088](https://github.com/python/cpython/issues/110088): Addressed test_asyncio timeouts by no longer gauging maximum duration, since a test ought not gauge CI performance. Only the minimum duration is measured once a task carries a timeout or delay. Brought `CLOCK_RES` into `test_asyncio.utils`. Victor Stinner authored the patch.

[gh-109276](https://github.com/python/cpython/issues/109276): regrtest: Should a test fail with ?env changed? while the ?rerun option is active, that test now reruns under verbose mode inside a brand-new process. Victor Stinner authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
