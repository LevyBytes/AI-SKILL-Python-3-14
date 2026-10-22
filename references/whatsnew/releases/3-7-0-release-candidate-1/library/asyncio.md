# Python 3.7.0 release candidate 1 / library / asyncio

[bpo-33694](https://bugs.python.org/issue?@action=redirect&bpo=33694): asyncio: Repair a race condition that loses data on pause_reading()/resume_reading() while the ProactorEventLoop is in use.

[bpo-33769](https://bugs.python.org/issue?@action=redirect&bpo=33769): asyncio/start_tls: Repair the error message; drop callbacks should an unhandled error occur; flag SSLTransport as closed once it gets aborted.

[bpo-33734](https://bugs.python.org/issue?@action=redirect&bpo=33734): asyncio/ssl: Repair the AttributeError, and raise the default handshake timeout

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
