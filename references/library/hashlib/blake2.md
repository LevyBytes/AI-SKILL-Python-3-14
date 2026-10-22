# hashlib — BLAKE2

### BLAKE2

[BLAKE2](https://www.blake2.net) is a cryptographic hash function defined in [**RFC 7693**](https://datatracker.ietf.org/doc/html/rfc7693.html) that comes in two flavors:

- **BLAKE2b**, tuned for 64-bit platforms, emitting digests of any size from 1 through 64 bytes,

- **BLAKE2s**, tuned for 8- to 32-bit platforms, emitting digests of any size from 1 through 32 bytes.

The capabilities BLAKE2 brings include **keyed mode** (standing in for [HMAC](https://en.wikipedia.org/wiki/Hash-based_message_authentication_code) more quickly and simply), plus **salted hashing**, then **personalization**, together with **tree hashing**.

The hash objects from this module conform to the API used by the standard library’s `hashlib` objects.

[Subject index](INDEX.md) · [Previous](hashlib-pbkdf2-hmac-to-hashlib-scrypt.md) · [Continue](hashlib-blake2b-to-hashlib-blake2s.md) · [Owning module, declaration or section: hashlib](hashlib-secure-hashes-and-message-digests.md)
