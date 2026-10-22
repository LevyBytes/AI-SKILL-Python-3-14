# Python 3.9.0 alpha 1 / tests / asyncio subprocess test timeout

[bpo-38614](https://bugs.python.org/issue?@action=redirect&bpo=38614): Repair test_communicate() within test_asyncio.test_subprocess so it relies on `support.LONG_TIMEOUT` (5 minutes) rather than a mere 1 minute.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
