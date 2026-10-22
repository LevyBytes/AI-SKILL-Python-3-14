# Python 3.7.0 alpha 3 / tests / tests and documentation

[bpo-28668](https://bugs.python.org/issue?@action=redirect&bpo=28668): test.support.requires_multiprocessing_queue has been removed. Where the semaphore implementation is missing or broken, skip those tests with test.support.import_module(?multiprocessing.synchronize?) instead.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
