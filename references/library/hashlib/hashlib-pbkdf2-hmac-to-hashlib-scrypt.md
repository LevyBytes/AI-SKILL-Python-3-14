# hashlib — Key derivation

### Key derivation

Algorithms for key derivation and key stretching exist to hash passwords securely. Simplistic approaches like `sha1(password)` hold up poorly against brute-force attacks. An effective password hashing function has to be tunable, slow, and carry a [salt](https://en.wikipedia.org/wiki/Salt_%28cryptography%29).

 hashlib.pbkdf2_hmac(*hash_name*, *password*, *salt*, *iterations*, *dklen=None*)

This function delivers the PKCS#5 password-based key derivation function 2. HMAC serves as its pseudorandom function.

The string *hash_name* names the hash digest algorithm wanted for HMAC, for instance ‘sha1’ or ‘sha256’. Both *password* and *salt* are taken as buffers of bytes. Applications and libraries ought to cap *password* at a reasonable length (say 1024). *salt* should run to roughly 16 bytes or more drawn from a proper source, such as [`os.urandom()`](https://docs.python.org/3.14/library/os.html#os.urandom).

Pick the count of *iterations* according to the hash algorithm and available computing power. As of 2022, several hundred thousand iterations of SHA-256 are recommended. For the reasoning behind that and guidance on selecting what suits your application, see *Appendix A.2.2* of [NIST-SP-800-132](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-132.pdf). The replies on the [stackexchange pbkdf2 iterations question](https://security.stackexchange.com/questions/3959/recommended-of-iterations-when-using-pbkdf2-sha256/) lay it out thoroughly.

In bytes, *dklen* sets how long the derived key is. Leaving *dklen* at `None` makes it default to the digest size of the *hash_name* hash algorithm — for SHA-512 that comes to 64.

```python
>>> from hashlib import pbkdf2_hmac
>>> our_app_iters = 500_000  # Application specific, read above.
>>> dk = pbkdf2_hmac('sha256', b'password', b'bad salt' * 2, our_app_iters)
>>> dk.hex()
'15530bba69924174860db778f2c6f8104d3aaf9d26241840c8c4a641c8d000a9'

```

This function is available only when Python is compiled with OpenSSL.

Added in version 3.4.

Changed in version 3.12: This function now exists solely on Python builds made with OpenSSL; the sluggish pure-Python version is gone.

 hashlib.scrypt(*password*, ***, *salt*, *n*, *r*, *p*, *maxmem=0*, *dklen=64*)

This function delivers the scrypt password-based key derivation function as laid out in [**RFC 7914**](https://datatracker.ietf.org/doc/html/rfc7914.html).

Both *password* and *salt* have to be [bytes-like objects](https://docs.python.org/3.14/glossary.html#term-bytes-like-object). Applications and libraries ought to cap *password* at a reasonable length (say 1024). *salt* should run to roughly 16 bytes or more drawn from a proper source, such as [`os.urandom()`](https://docs.python.org/3.14/library/os.html#os.urandom).

Here *n* gives the CPU/Memory cost factor, *r* the block size, and *p* the parallelization factor, while *maxmem* caps memory (the OpenSSL 1.1.0 default is 32 MiB). In bytes, *dklen* sets how long the derived key is.

Added in version 3.6.

[Subject index](INDEX.md) · [Previous](hashlib-file-digest.md) · [Continue](blake2.md) · [Owning module, declaration or section: hashlib](hashlib-secure-hashes-and-message-digests.md)
