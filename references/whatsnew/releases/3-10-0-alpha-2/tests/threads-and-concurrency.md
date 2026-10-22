# Python 3.10.0 alpha 2 / tests / threads and concurrency

[bpo-41739](https://bugs.python.org/issue?@action=redirect&bpo=41739): Repairs test_logging.test_race_between_set_target_and_flush(); to stop leaking live threads, the test now blocks until every thread has finished.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
