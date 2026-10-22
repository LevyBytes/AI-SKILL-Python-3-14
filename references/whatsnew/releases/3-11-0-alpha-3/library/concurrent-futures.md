# Python 3.11.0 alpha 3 / library / concurrent futures

[bpo-44733](https://bugs.python.org/issue?@action=redirect&bpo=44733): Introduce `max_tasks_per_child` for [`concurrent.futures.ProcessPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor). With it, users can cap how many tasks one process runs before that process must be restarted.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
