# Python 3.9.0 alpha 2 / tests / test

[bpo-38614](https://bugs.python.org/issue?@action=redirect&bpo=38614): Swap the hardcoded timeout constants used in tests for these new [`test.support`](https://docs.python.org/3.14/library/test.html#module-test.support) constants: [`LOOPBACK_TIMEOUT`](https://docs.python.org/3.14/library/test.html#test.support.LOOPBACK_TIMEOUT), [`INTERNET_TIMEOUT`](https://docs.python.org/3.14/library/test.html#test.support.INTERNET_TIMEOUT), [`SHORT_TIMEOUT`](https://docs.python.org/3.14/library/test.html#test.support.SHORT_TIMEOUT) and [`LONG_TIMEOUT`](https://docs.python.org/3.14/library/test.html#test.support.LONG_TIMEOUT). Tuning these four timeout constants across all tests at the same time is now far simpler, with no need to touch each individual test file.

[bpo-38991](https://bugs.python.org/issue?@action=redirect&bpo=38991): [`test.support`](https://docs.python.org/3.14/library/test.html#module-test.support): the `run_python_until_end()`, `assert_python_ok()` and `assert_python_failure()` functions no longer trim whitespace off stderr. The `test.support.strip_python_stderr()` function is gone.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
