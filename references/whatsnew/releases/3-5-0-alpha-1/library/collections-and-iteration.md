# Python 3.5.0 alpha 1 / library / collections and iteration

[bpo-21549](https://bugs.python.org/issue?@action=redirect&bpo=21549): A ?members? parameter was added to TarFile.list().

[bpo-19628](https://bugs.python.org/issue?@action=redirect&bpo=19628): A -r option now lets you set the recursion depth used by compileall.

[bpo-16531](https://bugs.python.org/issue?@action=redirect&bpo=16531): An (address, netmask) tuple argument is now accepted by ipaddress.IPv4Network and ipaddress.IPv6Network, making it straightforward to build network objects out of existing addresses.

[bpo-21424](https://bugs.python.org/issue?@action=redirect&bpo=21424): To cut down on tuple comparisons, heaqp.nlargest() and nmsmallest() were simplified and optimized.

[bpo-23302](https://bugs.python.org/issue?@action=redirect&bpo=23302): Set TCP_NODELAY=1 by default once an HTTPConnection is established. Dropped the hard-coded MSS since that optimization is no longer required once Nagle is disabled.

[bpo-21173](https://bugs.python.org/issue?@action=redirect&bpo=21173): len() on a WeakKeyDictionary was fixed for when .clear() had been invoked while an iterator was still alive.

[bpo-22095](https://bugs.python.org/issue?@action=redirect&bpo=22095): HTTPConnection.set_tunnel was fixed for the default port case, where the host header's port value had been set to "None". Demian Brecht supplied the patch.

[bpo-21321](https://bugs.python.org/issue?@action=redirect&bpo=21321): Once a slice is used up, itertools.islice() now drops its hold on the source iterator. Anton Afanasyev wrote this patch.

[bpo-6167](https://bugs.python.org/issue?@action=redirect&bpo=6167): When no argument is given, Scrollbar.activate() now hands back the name of the active element. Only 2 arguments are now ever accepted by Scrollbar.set().

[bpo-17826](https://bugs.python.org/issue?@action=redirect&bpo=17826): Assigning an iterable side_effect onto a mock function built by create_autospec is now functional. Kushal Das wrote the patch.

[bpo-22427](https://bugs.python.org/issue?@action=redirect&bpo=22427): TemporaryDirectory stops trying to clean up twice when used through a with statement inside a generator.

[bpo-16808](https://bugs.python.org/issue?@action=redirect&bpo=16808): Rather than a plain tuple, inspect.stack() now hands back a named tuple. Daniel Shahaf wrote the patch.

[bpo-19505](https://bugs.python.org/issue?@action=redirect&bpo=19505): Using reversed(), the items, keys, and values views belonging to OrderedDict now allow reverse iteration.

[bpo-21082](https://bugs.python.org/issue?@action=redirect&bpo=21082): Within os.makedirs, the process-wide umask is no longer set. Be aware this alters how makedirs behaves with exist_ok=True.

[bpo-23186](https://bugs.python.org/issue?@action=redirect&bpo=23186): Both ssl.SSLObject.shared_ciphers() and ssl.SSLSocket.shared_ciphers() were added so you can retrieve the cipher list the client offered during the handshake.

[bpo-21270](https://bugs.python.org/issue?@action=redirect&bpo=21270): tuple methods on mock.call objects are now overridden so that they work as ordinary call attributes.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
