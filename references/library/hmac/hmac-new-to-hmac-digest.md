# hmac: `hmac.new()`, `hmac.digest()`

## hmac — Keyed-Hashing for Message Authentication

### `hmac` — Keyed-Hashing for Message Authentication

**Source code:** [Lib/hmac.py](https://github.com/python/cpython/tree/3.14/Lib/hmac.py)

---

This module carries out the HMAC algorithm laid out in [**RFC 2104**](https://datatracker.ietf.org/doc/html/rfc2104.html). Its interface lets you plug in any hash function that has a *fixed* digest size. Notably, extendable-output functions like SHAKE-128 or SHAKE-256 are not usable with HMAC.

 hmac.new(*key*, *msg=None*, *digestmod*)

Build and return a fresh hmac object. The secret key comes from *key*, a bytes or bytearray object. Should *msg* be supplied, the call `update(msg)` runs. The digest name, digest constructor, or module the HMAC object will rely on is *digestmod*; any name acceptable to [`hashlib.new()`](https://docs.python.org/3.14/library/hashlib.html#hashlib.new) works here. Even though it sits last in the signature, it must be given.

Changed in version 3.4: A bytes or bytearray object is now allowed for the *key* parameter. The *msg* parameter accepts whatever type [`hashlib`](https://docs.python.org/3.14/library/hashlib.html#module-hashlib) handles. A hash algorithm's name may serve as the *digestmod* parameter.

Changed in version 3.8: Supplying the *digestmod* argument is now mandatory. Hand it over as a keyword argument so things stay clean when no initial *msg* is on hand.

 hmac.digest(*key*, *msg*, *digest*)

Return the digest of *msg* for the supplied secret *key* and *digest*. This function matches `HMAC(key, msg, digest).digest()`, but draws on an optimized C or inline implementation that runs faster for messages that fit in memory. The *key*, *msg*, and *digest* parameters carry the same meaning they do in `new()`.

CPython implementation detail, that optimized C path kicks in solely when *digest* is a string naming a digest algorithm that OpenSSL backs.

Added in version 3.7.

[Subject index](INDEX.md) · [Continue](hmac-hmac-class-to-hmac-name.md)
