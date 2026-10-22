# Python 3.5.0 alpha 1 / library / build and platforms

[bpo-21121](https://bugs.python.org/issue?@action=redirect&bpo=21121): Third-party C extensions are no longer compelled to compile under -Werror=declaration-after-statement.

[bpo-22733](https://bugs.python.org/issue?@action=redirect&bpo=22733): Corrected ffi_prep_args so it zero-extends argument values properly on 64-bit Windows.

[bpo-18643](https://bugs.python.org/issue?@action=redirect&bpo=18643): socket.socketpair() was added on Windows.

[bpo-22449](https://bugs.python.org/issue?@action=redirect&bpo=22449): Within ssl.SSLContext.load_default_certs, the SSL_CERT_DIR and SSL_CERT_FILE environmental variables are now consulted on Windows.

[bpo-22902](https://bugs.python.org/issue?@action=redirect&bpo=22902): On Linux the "ip" command now serves to find the MAC address within uuid.getnode(). Bruno Cauet supplied the patch.

[bpo-18314](https://bugs.python.org/issue?@action=redirect&bpo=18314): On Windows, Unlink will now clear away junctions too. Kim Gräsman wrote the patch.

[bpo-10650](https://bugs.python.org/issue?@action=redirect&bpo=10650): The non-standard ‘watchexp’ parameter has been dropped from the Python build of the Decimal.quantize() method. The C build had never carried it.

[bpo-21719](https://bugs.python.org/issue?@action=redirect&bpo=21719): On Windows, the `st_file_attributes` field was added to os.stat_result.

[bpo-22018](https://bugs.python.org/issue?@action=redirect&bpo=22018): Under Windows, sockets are now accepted by signal.set_wakeup_fd() as well. The consequence is that Python takes on a dependency on the WinSock library.

[bpo-21704](https://bugs.python.org/issue?@action=redirect&bpo=21704): A build failure in _multiprocessing arising when semaphores are absent was fixed. Arfrever Frehtes Taifersar Arahesis wrote the patch.

[bpo-21356](https://bugs.python.org/issue?@action=redirect&bpo=21356): ssl.RAND_egd() was made optional so LibreSSL is supported. Whether the function exists is verified at compile time. Bernard Spil wrote the patch.

[bpo-22287](https://bugs.python.org/issue?@action=redirect&bpo=22287): Where it exists on UNIX, _PyTime_gettimeofday() now relies on clock_gettime(CLOCK_REALTIME). The knock-on effect is that Python now links against librt on Solaris and on Linux (specifically when glibc predates 2.17).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
