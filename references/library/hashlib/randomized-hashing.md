# hashlib — Randomized hashing

#### Randomized hashing

Supplying the *salt* parameter lets users bring randomization into the hash function. Such randomized hashing helps guard against collision attacks aimed at the hash function backing digital signatures.

>

The intended scenario for randomized hashing is one in which a first party — the message preparer — assembles all or some of a message that a second party, the message signer, will then sign. Where that preparer can locate collisions in a cryptographic hash function (that is, a pair of messages that yield one shared hash value), they could craft plausible message variants sharing an identical hash value and digital signature yet carrying divergent effects (for instance, moving $1,000,000 into an account in place of $10). Although collision resistance has always been a chief design goal for cryptographic hash functions, the present focus on breaking them could leave any particular cryptographic hash function with weaker collision resistance than anticipated. By lowering the chance that a preparer manages to produce two or more messages which end up sharing the same hash value over the course of generating the digital signature, randomized hashing grants the signer extra protection — even when finding collisions for the hash function is computationally feasible. That said, when every part of the message originates with the signer, applying randomized hashing can cut into the security a digital signature affords.

([NIST SP-800-106 “Randomized Hashing for Digital Signatures”](https://csrc.nist.gov/pubs/sp/800/106/final))

Within BLAKE2 the salt enters the hash function just once during initialization, instead of being fed into every compression function.

Warning

Passwords should not be hashed with *Salted hashing* (or plain hashing) under BLAKE2 — nor under any other general-purpose cryptographic hash function like SHA-256. Further details appear in the [BLAKE2 FAQ](https://www.blake2.net/#qa).

```python
>>> import os
>>> from hashlib import blake2b
>>> msg = b'some message'
>>> # Calculate the first hash with a random salt.
>>> salt1 = os.urandom(blake2b.SALT_SIZE)
>>> h1 = blake2b(salt=salt1)
>>> h1.update(msg)
>>> # Calculate the second hash with a different random salt.
>>> salt2 = os.urandom(blake2b.SALT_SIZE)
>>> h2 = blake2b(salt=salt2)
>>> h2.update(msg)
>>> # The digests are different.
>>> h1.digest() != h2.digest()
True

```

[Subject index](INDEX.md) · [Previous](keyed-hashing.md) · [Continue](personalization.md) · [Owning module, declaration or section: hashlib](hashlib-secure-hashes-and-message-digests.md)
