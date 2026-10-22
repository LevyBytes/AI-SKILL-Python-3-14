# Python 3.6.4 release candidate 1 / library / threads and concurrency

[bpo-31806](https://bugs.python.org/issue?@action=redirect&bpo=31806): Corrected the rounding of timeouts in time.sleep(), threading.Lock.acquire() and socket.socket.settimeout() so that negative timeouts in the range -1.0 to 0.0 round properly. These calls now block while waiting for events, the way they should; before, they behaved as non-blocking by mistake. Pablo Galindo wrote the patch.

[bpo-31516](https://bugs.python.org/issue?@action=redirect&bpo=31516): During shutdown, `threading.current_thread()` ought not hand back a dummy thread.

[bpo-32186](https://bugs.python.org/issue?@action=redirect&bpo=32186): While fetching the file size, io.FileIO.readall() and io.FileIO.read() now drop the GIL. This repairs the hang of every thread that an inaccessible NFS server used to cause. Nir Soffer wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
