# Python 3.6.0 beta 1 / tests / threads and concurrency

[bpo-27787](https://bugs.python.org/issue?@action=redirect&bpo=27787): Run gc.collect() ahead of each test's "dangling threads" check, because those dangling threads are weak references.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
