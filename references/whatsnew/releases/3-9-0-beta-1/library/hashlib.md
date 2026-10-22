# Python 3.9.0 beta 1 / library / hashlib

[bpo-40637](https://bugs.python.org/issue?@action=redirect&bpo=40637): Built-in hash modules can from now on be turned off, or enabled selectively, via `configure --with-builtin-hashlib-hashes=sha3,blake1` or `--without-builtin-hashlib-hashes`.

[bpo-37630](https://bugs.python.org/issue?@action=redirect&bpo=37630): Where OpenSSL offers them, the [`hashlib`](https://docs.python.org/3.14/library/hashlib.html#module-hashlib) module is now able to draw on SHA3 hashes and the SHAKE XOF.

[bpo-40479](https://bugs.python.org/issue?@action=redirect&bpo=40479): The [`hashlib`](https://docs.python.org/3.14/library/hashlib.html#module-hashlib) builds successfully against OpenSSL 3.0.0-alpha2.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
