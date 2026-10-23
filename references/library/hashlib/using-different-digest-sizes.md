# hashlib - Using different digest sizes

#### Using different digest sizes

The digest size in BLAKE2 is configurable, reaching 64 bytes for BLAKE2b and 32 bytes for BLAKE2s. As an example, swapping SHA-1 for BLAKE2b while keeping the output size the same means instructing BLAKE2b to emit 20-byte digests:

```python
>>> from hashlib import blake2b
>>> h = blake2b(digest_size=20)
>>> h.update(b'Replacing SHA1 with the more secure function')
>>> h.hexdigest()
'd24f26cf8de66472d58d4e1b1774b4c9158b1f4c'
>>> h.digest_size
20
>>> len(h.digest())
20

```

Hash objects configured with differing digest sizes give wholly distinct outputs (a shorter hash is *not* a prefix of a longer one); BLAKE2b and BLAKE2s emit different outputs even when the output length matches:

```python
>>> from hashlib import blake2b, blake2s
>>> blake2b(digest_size=10).hexdigest()
'6fa1d8fcfd719046d762'
>>> blake2b(digest_size=11).hexdigest()
'eb6ec15daf9546254f0809'
>>> blake2s(digest_size=10).hexdigest()
'1bf21a98c78a1c376ae9'
>>> blake2s(digest_size=11).hexdigest()
'567004bf96e4a25773ebf4'

```

[Subject index](INDEX.md) · [Previous](simple-hashing.md) · [Continue](keyed-hashing.md) · [Owning module, declaration or section: hashlib](hashlib-secure-hashes-and-message-digests.md)
