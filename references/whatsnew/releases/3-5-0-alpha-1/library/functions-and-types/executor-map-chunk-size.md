# Python 3.5.0 alpha 1 / library / concurrent futures executor map accepts chunksize argument tasks can batched within child

[bpo-11271](https://bugs.python.org/issue?@action=redirect&bpo=11271): concurrent.futures.Executor.map() now accepts a *chunksize* argument so tasks can be batched within child processes, boosting ProcessPoolExecutor performance. Dan O — Reilly supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../../release-overview/overview.md)
