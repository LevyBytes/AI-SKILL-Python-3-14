# What's New In Python 3.11 / hashlib - hashlib

### hashlib

- [`hashlib.blake2b()`](https://docs.python.org/3.14/library/hashlib.html#hashlib.blake2b) and [`hashlib.blake2s()`](https://docs.python.org/3.14/library/hashlib.html#hashlib.blake2s) now lean toward [libb2](https://www.blake2.net/) ahead of the copy bundled with Python. (Contributed by Christian Heimes in [bpo-47095](https://bugs.python.org/issue?@action=redirect&bpo=47095).)

- The private `_sha3` module that provides SHA3 and SHAKE algorithms now relies on *tiny_sha3* rather than the *Keccak Code Package*, trimming both source and binary footprint. The [`hashlib`](https://docs.python.org/3.14/library/hashlib.html#module-hashlib) module favors the optimized SHA3 and SHAKE builds supplied by OpenSSL. Only setups lacking OpenSSL support feel this change. (Contributed by Christian Heimes in [bpo-47098](https://bugs.python.org/issue?@action=redirect&bpo=47098).)

- [`hashlib.file_digest()`](https://docs.python.org/3.14/library/hashlib.html#hashlib.file_digest) was added, a convenience routine for hashing files or file-like objects efficiently. (Contributed by Christian Heimes in [gh-89313](https://github.com/python/cpython/issues/89313).)

[Subject index](INDEX.md) · [Previous source section](gzip.md) · [Next source section](idle-and-idlelib.md) · [Release/subject declaration](summary-release-highlights.md)
