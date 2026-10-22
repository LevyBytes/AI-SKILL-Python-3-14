# Python 3.13.0 alpha 1 / tests / repaired test timeout inside test concurrent futures test wait

[gh-109594](https://github.com/python/cpython/issues/109594): Repaired test_timeout() inside test_concurrent_futures.test_wait. Drop the future that might or might not finish depending on whether it overruns the timeout. Hold onto the second future, which stays incomplete until wait() times out. Victor Stinner authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
