# hashlib - Attributes

### Attributes

Hashlib exposes these constant module attributes:

 hashlib.algorithms_guaranteed

A set holding the names of the hash algorithms that this module guarantees on every platform. Observe that ‘md5’ appears here even though certain upstream vendors ship an unusual “FIPS compliant” Python build that leaves it out.

Added in version 3.2.

 hashlib.algorithms_available

A set holding the names of the hash algorithms the current Python interpreter can access. Passing any of these names to `new()` will be accepted. `algorithms_guaranteed` is always contained within it. A single algorithm can show up more than once in this set under various names (courtesy of OpenSSL).

Added in version 3.2.

[Subject index](INDEX.md) · [Previous](hashlib-new-to-hashlib-sha3-512.md) · [Continue](hash-digest-size-to-hash-copy.md) · [Owning module, declaration or section: hashlib](hashlib-secure-hashes-and-message-digests.md)
