# Python 3.13.0 beta 1 / security / hashlib

[gh-117233](https://github.com/python/cpython/issues/117233): At build time, detect whether the OpenSSL-ish libcrypto library offers BLAKE2, SHA3, Shake, & truncated SHA512. This lets [`hashlib`](https://docs.python.org/3.14/library/hashlib.html#module-hashlib) operate with libraries lacking some of the algorithms that upstream OpenSSL provides.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
