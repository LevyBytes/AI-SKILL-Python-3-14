# What's New In Python 3.6 / hashlib — hashlib

### hashlib

[`hashlib`](https://docs.python.org/3.14/library/hashlib.html#module-hashlib) works with OpenSSL 1.1.0. The lowest version we suggest is 1.0.2. (Contributed by Christian Heimes in [bpo-26470](https://bugs.python.org/issue?@action=redirect&bpo=26470).)

BLAKE2 hash functions joined the module. [`blake2b()`](https://docs.python.org/3.14/library/hashlib.html#hashlib.blake2b) and [`blake2s()`](https://docs.python.org/3.14/library/hashlib.html#hashlib.blake2s) are present at all times and cover the complete BLAKE2 feature set. (Contributed by Christian Heimes in [bpo-26798](https://bugs.python.org/issue?@action=redirect&bpo=26798); the underlying code came from Dmitry Chestnykh and Samuel Neves. Its documentation was authored by Dmitry Chestnykh.)

The SHA-3 hash functions [`sha3_224()`](https://docs.python.org/3.14/library/hashlib.html#hashlib.sha3_224), [`sha3_256()`](https://docs.python.org/3.14/library/hashlib.html#hashlib.sha3_256), [`sha3_384()`](https://docs.python.org/3.14/library/hashlib.html#hashlib.sha3_384), [`sha3_512()`](https://docs.python.org/3.14/library/hashlib.html#hashlib.sha3_512), together with the SHAKE hash functions [`shake_128()`](https://docs.python.org/3.14/library/hashlib.html#hashlib.shake_128) and [`shake_256()`](https://docs.python.org/3.14/library/hashlib.html#hashlib.shake_256) joined the lineup. (Contributed by Christian Heimes in [bpo-16113](https://bugs.python.org/issue?@action=redirect&bpo=16113). The supporting Keccak Code Package was authored by the following:)

> Guido Bertoni, Joan Daemen, Michaël Peeters, Gilles Van Assche, and Ronny Van Keer.

The password-based key derivation function [`scrypt()`](https://docs.python.org/3.14/library/hashlib.html#hashlib.scrypt) can now be used given OpenSSL 1.1.0 or later. (Contributed by Christian Heimes in [bpo-27928](https://bugs.python.org/issue?@action=redirect&bpo=27928).)

### http.client

[Subject index](INDEX.md) · [Previous source section](fileinput.md) · [Release/subject declaration](summary-release-highlights.md) · [Following release/subject continuation](http-client.md)
