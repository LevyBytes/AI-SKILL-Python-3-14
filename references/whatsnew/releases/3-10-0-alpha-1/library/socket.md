# Python 3.10.0 alpha 1 / library / socket

[bpo-39651](https://bugs.python.org/issue?@action=redirect&bpo=39651): Resolved a race condition inside the `call_soon_threadsafe()` method of `asyncio.ProactorEventLoop`: when the self-pipe socket is already closed, it now does nothing.

[bpo-25920](https://bugs.python.org/issue?@action=redirect&bpo=25920): On macOS, [`socket.getaddrinfo()`](https://docs.python.org/3.14/library/socket.html#socket.getaddrinfo) no longer takes an internal lock to guard against race conditions while calling `getaddrinfo()`, a call that has been thread-safe ever since macOS 10.5. This change applied when compiling Python targeting macOS 10.4 or earlier ? a configuration that did not describe the python.org macOS installer. Python 3.9 needs macOS 10.6 or later. That internal lock had triggered sporadic hangs on fork whenever a second thread happened to be running `socket.getaddrinfo()`. The same lock was active on FreeBSD prior to 5.3, OpenBSD prior to 201311, and NetBSD prior to 4.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
