# Python 3.9.0 alpha 1 / tests / test

[bpo-37261](https://bugs.python.org/issue?@action=redirect&bpo=37261): Repair [`test.support.catch_unraisable_exception()`](https://docs.python.org/3.14/library/test.html#test.support.catch_unraisable_exception): its __exit__() method now disregards the unraisable exception that arises while clearing its `unraisable` attribute.

[bpo-38614](https://bugs.python.org/issue?@action=redirect&bpo=38614): Introduce timeout constants into [`test.support`](https://docs.python.org/3.14/library/test.html#module-test.support): [`LOOPBACK_TIMEOUT`](https://docs.python.org/3.14/library/test.html#test.support.LOOPBACK_TIMEOUT), [`INTERNET_TIMEOUT`](https://docs.python.org/3.14/library/test.html#test.support.INTERNET_TIMEOUT), [`SHORT_TIMEOUT`](https://docs.python.org/3.14/library/test.html#test.support.SHORT_TIMEOUT) and [`LONG_TIMEOUT`](https://docs.python.org/3.14/library/test.html#test.support.LONG_TIMEOUT).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
