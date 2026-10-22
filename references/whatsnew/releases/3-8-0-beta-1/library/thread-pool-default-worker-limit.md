# Python 3.8.0 beta 1 / library / switches default max workers threadpoolexecutor away cpu count over min cpu count

[bpo-35279](https://bugs.python.org/issue?@action=redirect&bpo=35279): Switches the default *max_workers* on `ThreadPoolExecutor` away from `cpu_count() * 5` over to `min(32, cpu_count() + 4)`. The earlier figure grew absurdly big on machines with many cores.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
