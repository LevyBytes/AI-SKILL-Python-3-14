# Python 3.11.0 alpha 1 / library / hmac

[bpo-44145](https://bugs.python.org/issue?@action=redirect&bpo=44145): [`hmac`](https://docs.python.org/3.14/library/hmac.html#module-hmac) computations failed to release the GIL during their call to the OpenSSL `HMAC_Update` C API (introduced in 3.9). That accidentally blocked the parallel computation that other [`hashlib`](https://docs.python.org/3.14/library/hashlib.html#module-hashlib) algorithms allow.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
