# hashlib — `hashlib` — Secure hashes and message digests

### `hashlib` — Secure hashes and message digests

**Source code:** [Lib/hashlib.py](https://github.com/python/cpython/tree/3.14/Lib/hashlib.py)

---

A single, shared interface to a broad collection of hashing algorithms is what this module exposes. Among them are the FIPS secure hash algorithms SHA224, SHA256, SHA384, SHA512, (defined in [the FIPS 180-4 standard](https://csrc.nist.gov/pubs/fips/180-4/upd1/final)), the SHA-3 family (defined in [the FIPS 202 standard](https://csrc.nist.gov/pubs/fips/202/final)), and the older algorithms SHA1 ([formerly part of FIPS](https://csrc.nist.gov/news/2023/decision-to-revise-fips-180-4)) along with MD5 (defined in internet [**RFC 1321**](https://datatracker.ietf.org/doc/html/rfc1321.html)).

Note

Should you need the adler32 or crc32 hash functions instead, look in the [`zlib`](https://docs.python.org/3.14/library/zlib.html#module-zlib) module.

[Subject index](INDEX.md) · [Continue](hash-algorithms.md)
