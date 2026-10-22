# Python 3.7.0 beta 1 / library / concurrent futures

[bpo-32596](https://bugs.python.org/issue?@action=redirect&bpo=32596): `concurrent.futures` imports `ThreadPoolExecutor` and `ProcessPoolExecutor` lazily (by way of [**PEP 562**](https://peps.python.org/pep-0562/)). This renders `import asyncio` roughly 15% quicker since asyncio relies on only `ThreadPoolExecutor` by default.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
