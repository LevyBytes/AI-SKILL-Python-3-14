# Python 3.7.0 alpha 3 / library / threads and concurrency

[bpo-31806](https://bugs.python.org/issue?@action=redirect&bpo=31806): Corrected timeout rounding in time.sleep(), threading.Lock.acquire() and socket.socket.settimeout() so that negative timeouts in the -1.0 to 0.0 range round properly. Those functions will now block awaiting events as they should; before this fix the call wrongly behaved as non-blocking. Pablo Galindo supplied the patch.

[bpo-32186](https://bugs.python.org/issue?@action=redirect&bpo=32186): While obtaining the file size, io.FileIO.readall() and io.FileIO.read() now drop the GIL. This clears up a hang of every thread against an unreachable NFS server. Nir Soffer supplied the patch.

[bpo-31976](https://bugs.python.org/issue?@action=redirect&bpo=31976): Fixes a race condition arising when flushing a file is slow, which could cause a segfault if the file is closed from another thread.

[bpo-21423](https://bugs.python.org/issue?@action=redirect&bpo=21423): Add an initializer argument to {Process,Thread}PoolExecutor

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
