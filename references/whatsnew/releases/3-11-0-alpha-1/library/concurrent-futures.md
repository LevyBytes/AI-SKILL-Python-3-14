# Python 3.11.0 alpha 1 / library / concurrent futures

[bpo-43234](https://bugs.python.org/issue?@action=redirect&bpo=43234): Executors that are not [`concurrent.futures.ThreadPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor) instances can no longer be supplied to `loop.set_default_executor()`, completing a deprecation begun in Python 3.8. Illia Volochii authored the change.

[bpo-45021](https://bugs.python.org/issue?@action=redirect&bpo=45021): Closed a possible deadlock arising at shutdown of forked children whenever the [`concurrent.futures`](https://docs.python.org/3.14/library/concurrent.futures.html#module-concurrent.futures) module is in play

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
