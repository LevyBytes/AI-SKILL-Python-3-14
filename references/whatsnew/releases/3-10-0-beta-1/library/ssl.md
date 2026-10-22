# Python 3.10.0 beta 1 / library / ssl

[bpo-43522](https://bugs.python.org/issue?@action=redirect&bpo=43522): Resolve a problem affecting [`hostname_checks_common_name`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.hostname_checks_common_name). OpenSSL does not carry hostflags across from *struct SSL_CTX* into *struct SSL*.

[bpo-43920](https://bugs.python.org/issue?@action=redirect&bpo=43920): OpenSSL 3.0.0: when cadata holds no valid certificate, [`load_verify_locations()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.load_verify_locations) now reports one consistent error message.

[bpo-42854](https://bugs.python.org/issue?@action=redirect&bpo=42854): Internally the [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl) module now relies on `SSL_read_ex` and `SSL_write_ex`. Those functions can read and write data exceeding 2 GB. A zero-length write no longer trips a protocol violation error.

[bpo-43880](https://bugs.python.org/issue?@action=redirect&bpo=43880): [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl) now emits DeprecationWarning for the OP_NO_SSL/TLS* options, outdated TLS versions, outdated protocols, plus other capabilities deprecated as far back as Python 3.6, 3.7, or OpenSSL 1.1.0.

[bpo-43794](https://bugs.python.org/issue?@action=redirect&bpo=43794): Introduce the [`ssl.OP_IGNORE_UNEXPECTED_EOF`](https://docs.python.org/3.14/library/ssl.html#ssl.OP_IGNORE_UNEXPECTED_EOF) constants (OpenSSL 3.0.0)

[bpo-43788](https://bugs.python.org/issue?@action=redirect&bpo=43788): The header files carrying [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl) error codes are now tied to a specific OpenSSL version. Exceptions will now display the right reason and library codes. The `make_ssl_data.py` script was rewritten so it draws on OpenSSL’s text file of error codes.

[bpo-36076](https://bugs.python.org/issue?@action=redirect&bpo=36076): SNI support was added to [`ssl.get_server_certificate()`](https://docs.python.org/3.14/library/ssl.html#ssl.get_server_certificate).

[bpo-18369](https://bugs.python.org/issue?@action=redirect&bpo=18369): Certificate and PrivateKey classes joined the ssl module. Loading certificates and keys straight from a memory buffer is now also possible.

[bpo-31870](https://bugs.python.org/issue?@action=redirect&bpo=31870): A *timeout* parameter was added to the [`ssl.get_server_certificate()`](https://docs.python.org/3.14/library/ssl.html#ssl.get_server_certificate) function.

[bpo-40849](https://bugs.python.org/issue?@action=redirect&bpo=40849): Exposed the X509_V_FLAG_PARTIAL_CHAIN ssl flag

[bpo-35114](https://bugs.python.org/issue?@action=redirect&bpo=35114): As documented, [`ssl.RAND_status()`](https://docs.python.org/3.14/library/ssl.html#ssl.RAND_status) now hands back a boolean rather than `1` or `0`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
