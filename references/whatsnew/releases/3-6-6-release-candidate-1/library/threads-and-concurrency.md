# Python 3.6.6 release candidate 1 / library / threads and concurrency

[bpo-26819](https://bugs.python.org/issue?@action=redirect&bpo=26819): Settled a race condition affecting `ReadTransport.resume_reading` within the Windows proactor event loop.

[bpo-33021](https://bugs.python.org/issue?@action=redirect&bpo=33021): The GIL is now released across fstat() calls, which prevents every thread from hanging during mmap.mmap(), os.urandom(), and random.seed(). Nir Soffer supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
