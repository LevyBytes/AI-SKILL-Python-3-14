# Python 3.11.0 alpha 7 / library / hashlib

[bpo-47101](https://bugs.python.org/issue?@action=redirect&bpo=47101): Under OpenSSL 3.0, [`hashlib.algorithms_available`](https://docs.python.org/3.14/library/hashlib.html#hashlib.algorithms_available) reports only those algorithms that activated crypto providers offer. Legacy algorithms stay hidden until the legacy provider gets loaded into the default OSSL context.

[bpo-47095](https://bugs.python.org/issue?@action=redirect&bpo=47095): The internal `_blake2` module of [`hashlib`](https://docs.python.org/3.14/library/hashlib.html#module-hashlib) now favors `libb2` from [https://www.blake2.net/](https://www.blake2.net/) ahead of the blake2 copy vendored with Python.

[bpo-47098](https://bugs.python.org/issue?@action=redirect&bpo=47098): tiny_sha3 now takes the place of the Keccak Code Package inside the internal `_sha3` module of [`hashlib`](https://docs.python.org/3.14/library/hashlib.html#module-hashlib). It serves as the fallback whenever Python is compiled without OpenSSL.

[bpo-45150](https://bugs.python.org/issue?@action=redirect&bpo=45150): Provide a [`hashlib.file_digest()`](https://docs.python.org/3.14/library/hashlib.html#hashlib.file_digest) helper to hash a file object efficiently.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
