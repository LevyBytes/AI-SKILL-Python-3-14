# Python 3.6.0 alpha 1 / library / threads and concurrency

[bpo-25304](https://bugs.python.org/issue?@action=redirect&bpo=25304): Introduced asyncio.run_coroutine_threadsafe(). With it a coroutine can be handed off to a loop from a separate thread, and you get back a concurrent.futures.Future. Authored by Vincent Michel.

[bpo-25319](https://bugs.python.org/issue?@action=redirect&bpo=25319): Upon reinitialization of a threading.Event, the underlying condition ought to rely on a plain lock instead of a recursive one.

- The getaddrinfo lookup is skipped when the host has already been resolved. A. Jesse Jiryu Davis contributed this patch.

[bpo-26590](https://bugs.python.org/issue?@action=redirect&bpo=26590): Added a safe finalizer for the _socket.socket type; it releases the GIL before closing the socket.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
