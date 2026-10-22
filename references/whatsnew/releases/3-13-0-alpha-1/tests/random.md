# Python 3.13.0 alpha 1 / tests / random

[gh-109580](https://github.com/python/cpython/issues/109580): Bypass `test_perf_profiler` whenever Python is compiled with the ASAN, MSAN, or UBSAN sanitizer. On such a build Python crashes at random during this test. Victor Stinner authored the patch.

[gh-109276](https://github.com/python/cpython/issues/109276): libregrtest now invokes [`random.seed()`](https://docs.python.org/3.14/library/random.html#random.seed) ahead of running each individual test file when the `-r/--randomize` command line option is supplied. What's more, it also fires inside worker processes. This ought to help render tests more deterministic. Beforehand, it fired just once within the main process ahead of running every test file, and never within worker processes. Victor Stinner authored the patch.

[gh-110171](https://github.com/python/cpython/issues/110171): `libregrtest` from now on consistently assigns and reports `random.seed`, improving the reproducibility of tests. Supply the explicit random seed for tests through the `--randseed` flag.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
