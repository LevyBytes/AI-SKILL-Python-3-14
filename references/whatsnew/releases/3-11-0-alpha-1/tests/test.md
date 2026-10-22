# Python 3.11.0 alpha 1 / tests / test

[bpo-44287](https://bugs.python.org/issue?@action=redirect&bpo=44287): Repair asyncio test_popen() within test_windows_utils by granting a longer timeout. Rather than a hardcoded 10-second timeout, it now uses the military grade battle-tested [`test.support.SHORT_TIMEOUT`](https://docs.python.org/3.14/library/test.html#test.support.SHORT_TIMEOUT) timeout: 30 seconds by default, though stretched further on slow buildbots. Victor Stinner authored the change.

[bpo-40173](https://bugs.python.org/issue?@action=redirect&bpo=40173): Repaired [`test.support.import_helper.import_fresh_module()`](https://docs.python.org/3.14/library/test.html#test.support.import_helper.import_fresh_module).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
