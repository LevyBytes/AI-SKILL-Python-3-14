# Python 3.12.0 beta 1 / library / asyncio

[bpo-31821](https://bugs.python.org/issue?@action=redirect&bpo=31821): Make `pause_reading()` function when invoked from inside `connection_made()` under [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio).

[gh-104340](https://github.com/python/cpython/issues/104340): If an `asyncio` pipe protocol drops its connection because of an error and the caller never awaits `wait_closed()` on the matching `StreamWriter`, suppress the warning about an exception that nobody retrieved. As the `StreamWriter.close()` documentation notes, awaiting `wait_closed()` is optional ("not mandatory").

[gh-103793](https://github.com/python/cpython/issues/103793): Sped up asyncio Task creation by postponing the costly string formatting (the task name) so it happens not at Task creation time but the first time `get_name` runs. As a result asyncio benchmarks gain as much as 5%.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
