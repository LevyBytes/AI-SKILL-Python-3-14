# What's New In Python 3.9 / hashlib — hashlib

### hashlib

When OpenSSL provides them, the [`hashlib`](https://docs.python.org/3.14/library/hashlib.html#module-hashlib) module can henceforth draw on SHA3 hashes plus the SHAKE XOF. (Contributed by Christian Heimes in [bpo-37630](https://bugs.python.org/issue?@action=redirect&bpo=37630).)

You can now switch off the builtin hash modules through `./configure --without-builtin-hashlib-hashes`, or turn on a subset, for instance `./configure --with-builtin-hashlib-hashes=sha3,blake2`, to compel use of the OpenSSL-backed implementation. (Contributed by Christian Heimes in [bpo-40479](https://bugs.python.org/issue?@action=redirect&bpo=40479))

[Subject index](INDEX.md) · [Previous source section](gc.md) · [Next source section](http.md) · [Release/subject declaration](summary-release-highlights.md)
