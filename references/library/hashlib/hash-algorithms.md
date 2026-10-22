# hashlib — Hash algorithms

### Hash algorithms

Each kind of *hash* has a constructor method named after it. Every one of them yields a hash object exposing the same straightforward interface. By way of illustration: call `sha256()` to obtain a SHA-256 hash object. From there you can supply the object with [bytes-like objects](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) (typically [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes)) through the `update` method. Whenever you like, request the *digest* of everything concatenated together that you have provided up to now via the `digest()` or `hexdigest()` methods.

So that multithreading is possible, the Python [GIL](https://docs.python.org/3.14/glossary.html#term-GIL) is dropped while a hash is computed when more than 2047 bytes of data are handed over at once through its constructor or `.update` method.

The hash-algorithm constructors that this module always exposes are `sha1()`, `sha224()`, `sha256()`, `sha384()`, `sha512()`, `sha3_224()`, `sha3_256()`, `sha3_384()`, `sha3_512()`, `shake_128()`, `shake_256()`, `blake2b()`, and `blake2s()`. Typically `md5()` is present too, but it can be absent or disabled on the uncommon “FIPS compliant” Python builds. This set maps to `algorithms_guaranteed`.

Your Python distribution may expose still more algorithms if its `hashlib` was linked against an OpenSSL build offering them. Such extras *are not guaranteed available* across every installation and are reachable only by name through `new()`. Consult `algorithms_available`.

Warning

A number of algorithms carry documented hash collision weaknesses (MD5 and SHA1 among them). See [Attacks on cryptographic hash algorithms](https://en.wikipedia.org/wiki/Cryptographic_hash_function#Attacks_on_cryptographic_hash_algorithms) together with the hashlib-seealso section closing this document.

Added in version 3.6: The Keccak-based SHA3 plus SHAKE constructors — `sha3_224()`, `sha3_256()`, `sha3_384()`, `sha3_512()`, `shake_128()`, `shake_256()` — arrived here, as did `blake2b()` alongside `blake2s()`.

Changed in version 3.9: A keyword-only *usedforsecurity* argument, defaulting to `True`, was given to every hashlib constructor. Setting it false permits insecure or blocked hashing algorithms inside locked-down environments; passing `False` signals that the algorithm serves no security purpose — for example acting as a non-cryptographic one-way compression function.

Changed in version 3.9: When OpenSSL supplies them, hashlib now draws SHA3 and SHAKE from it.

Changed in version 3.12: Should the linked OpenSSL omit any of the MD5, SHA1, SHA2, or SHA3 algorithms, a verified implementation drawn from the [HACL* project](https://github.com/hacl-star/hacl-star) takes over instead.

[Subject index](INDEX.md) · [Previous](hashlib-secure-hashes-and-message-digests.md) · [Continue](usage.md) · [Owning module, declaration or section: hashlib](hashlib-secure-hashes-and-message-digests.md)
