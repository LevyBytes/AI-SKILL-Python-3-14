# Python 3.5.3 release candidate 1 / tests / threads and concurrency

[bpo-27787](https://bugs.python.org/issue?@action=redirect&bpo=27787): Invoke gc.collect() ahead of checking every test for "dangling threads", given that those dangling threads are weak references.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
