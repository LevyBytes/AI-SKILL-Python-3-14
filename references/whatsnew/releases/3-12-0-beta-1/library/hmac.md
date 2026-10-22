# Python 3.12.0 beta 1 / library / hmac

[gh-103256](https://github.com/python/cpython/issues/103256): Corrected a defect that made [`hmac`](https://docs.python.org/3.14/library/hmac.html#module-hmac) throw an exception whenever the chosen hash algorithm was missing from OpenSSL even though `hashlib` itself offered it separately. The fallback to the built-in now works as it should. Such a situation could arise, say, when your OpenSSL lacks SHA3 support yet you wish to compute `hmac.digest(b'K', b'M', 'sha3_256')`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
