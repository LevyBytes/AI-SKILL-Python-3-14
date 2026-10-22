# Python 3.7.0 alpha 1 / library / queue

[bpo-31326](https://bugs.python.org/issue?@action=redirect&bpo=31326): concurrent.futures.ProcessPoolExecutor.shutdown() now closes the call queue explicitly. On top of that, shutdown(wait=True) now joins the call queue thread as well, so a dangling thread is not leaked.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
