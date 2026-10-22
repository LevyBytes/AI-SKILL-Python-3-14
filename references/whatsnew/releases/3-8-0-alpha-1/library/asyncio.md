# Python 3.8.0 alpha 1 / library / asyncio

[bpo-33769](https://bugs.python.org/issue?@action=redirect&bpo=33769): asyncio/start_tls: Corrected the error message; cancel callbacks should an unhandled error arise; flag SSLTransport as closed once it is aborted.

[bpo-33734](https://bugs.python.org/issue?@action=redirect&bpo=33734): asyncio/ssl: Corrected an AttributeError and raised the default handshake timeout

[bpo-34323](https://bugs.python.org/issue?@action=redirect&bpo=34323): [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio): Improve the `IocpProactor.close()` logging: hold off 1 second ahead of the first log line, then emit a log entry each second. Record as well how many seconds have elapsed since `close()` was invoked.

[bpo-32710](https://bugs.python.org/issue?@action=redirect&bpo=32710): Resolved memory leaks within the asyncio ProactorEventLoop when an overlapped operation fails.

[bpo-32710](https://bugs.python.org/issue?@action=redirect&bpo=32710): Resolved a memory leak in asyncio within the ProactorEventLoop whenever a `ReadFile()` or `WSASend()` overlapped operation fails right away: free the internal buffer.

[bpo-33833](https://bugs.python.org/issue?@action=redirect&bpo=33833): Corrected a bug in asyncio where ProactorSocketTransport logs AssertionError when force closed during write.

[bpo-33694](https://bugs.python.org/issue?@action=redirect&bpo=33694): asyncio: Resolved a race condition that lost data on pause_reading()/resume_reading() while the ProactorEventLoop is in use.

[bpo-34687](https://bugs.python.org/issue?@action=redirect&bpo=34687): asyncio on Windows now defaults to ProactorEventLoop rather than SelectorEventLoop.

[bpo-34263](https://bugs.python.org/issue?@action=redirect&bpo=34263): The asyncio event loop no longer hands timeouts that exceed a single day to epoll/select etc.

[bpo-35394](https://bugs.python.org/issue?@action=redirect&bpo=35394): Give the asyncio abstract protocols empty slots.

[bpo-35380](https://bugs.python.org/issue?@action=redirect&bpo=35380): Turn on TCP_NODELAY on Windows for the proactor asyncio event loop.

[bpo-30064](https://bugs.python.org/issue?@action=redirect&bpo=30064): Employ add_done_callback() across the sock_* asyncio API to drop the reader/writer subscription promptly upon calcellation.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
