# Python 3.10.0 alpha 1 / tests / test

[bpo-41521](https://bugs.python.org/issue?@action=redirect&bpo=41521): In [`test.support`](https://docs.python.org/3.14/library/test.html#module-test.support), rename the `blacklist` parameter of [`check__all__()`](https://docs.python.org/3.14/library/test.html#test.support.check__all__) to `not_exported`.

[bpo-38377](https://bugs.python.org/issue?@action=redirect&bpo=38377): On Linux, bypass tests relying on multiprocessing whenever the current user is unable to create a file inside the `/dev/shm/` directory. Add the [`skip_if_broken_multiprocessing_synchronize()`](https://docs.python.org/3.14/library/test.html#test.support.skip_if_broken_multiprocessing_synchronize) function to the [`test.support`](https://docs.python.org/3.14/library/test.html#module-test.support) module.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
