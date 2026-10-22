# Python 3.8.0 alpha 1 / library / threads and concurrency

[bpo-33625](https://bugs.python.org/issue?@action=redirect&bpo=33625): Drop the GIL on `grp.getgrnam`, `grp.getgrgid`, `pwd.getpwnam` and `pwd.getpwuid` whenever reentrant variants of those functions exist. Patch by William Grzybowski.

[bpo-33674](https://bugs.python.org/issue?@action=redirect&bpo=33674): Corrected a race condition in SSLProtocol.connection_made() of asyncio.sslproto: kick off the handshake right away instead of relying on call_soon(). Formerly, data_received() might run ahead of the handshake starting, which made the handshake hang or fail.

[bpo-33613](https://bugs.python.org/issue?@action=redirect&bpo=33613): Corrected a race condition in `multiprocessing.semaphore_tracker` arising when the tracker is sent SIGINT before it manages to register signal handlers that ignore it.

[bpo-35283](https://bugs.python.org/issue?@action=redirect&bpo=35283): Introduced a deprecation warning covering the `threading.Thread.isAlive()` method. Patch by Donghee Na.

[bpo-26819](https://bugs.python.org/issue?@action=redirect&bpo=26819): Resolve a race condition affecting `ReadTransport.resume_reading` within the Windows proactor event loop.

- Resolve a failure within `typing.get_type_hints()` arising when ClassVar arrived as a string forward reference.

[bpo-33021](https://bugs.python.org/issue?@action=redirect&bpo=33021): Drop the GIL across fstat() calls, sidestepping a hang of every thread while calling mmap.mmap(), os.urandom(), and random.seed(). Patch by Nir Soffer.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
