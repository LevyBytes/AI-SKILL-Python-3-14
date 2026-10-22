# Python 3.14.0 alpha 1 / tests / tests and documentation

[gh-124213](https://github.com/python/cpython/issues/124213): Recognize when the test suite executes inside a systemd-nspawn container started with the `--suppress-sync=true` option, and bypass the `test_os` and `test_mmap` tests that break in that situation.

[gh-121921](https://github.com/python/cpython/issues/121921): Adjust `Lib/test/crashers/bogus_code_obj.py` so that it once more crashes the way it should.

[gh-119727](https://github.com/python/cpython/issues/119727): Provide a `--single-process` command line option for the Python test runner (regrtest). Patch by Victor Stinner.

[gh-119273](https://github.com/python/cpython/issues/119273): The Python test runner no longer launches TTY-using tests (for example test_ioctl) inside a process group (via `setsid()`). Formerly such TTY-using tests were skipped. Patch by Victor Stinner.

[gh-119050](https://github.com/python/cpython/issues/119050): regrtest test runner: bring XML support to the refleak checker (-R option). Patch by Victor Stinner.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
