# Python 3.10.0 alpha 1 / library / ssl

[bpo-30008](https://bugs.python.org/issue?@action=redirect&bpo=30008): Make the [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl) code work with OpenSSL 1.1.x builds compiled using `no-deprecated` and `--api=1.1.0`.

[bpo-41056](https://bugs.python.org/issue?@action=redirect&bpo=41056): Corrected a NULL pointer dereference inside the ssl module triggered by a MemoryError during the keylog callback. (discovered by Coverity)

[bpo-41235](https://bugs.python.org/issue?@action=redirect&bpo=41235): Corrected the error handling within [`ssl.SSLContext.load_dh_params()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.load_dh_params).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
