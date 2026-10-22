# hashlib — Simple hashing

### Examples

#### Simple hashing

To hash some data, begin by building a hash object through the right constructor function (`blake2b()` or `blake2s()`), next feed it the data by invoking `update()` on the object, and at last pull the digest from the object by invoking `digest()` (or `hexdigest()` for a hex-encoded string).

```python
>>> from hashlib import blake2b
>>> h = blake2b()
>>> h.update(b'Hello world')
>>> h.hexdigest()
'6ff843ba685842aa82031d3f53c48b66326df7639a63d128974c5c14f31a0f33343a8c65551134ed1ae0f2b0dd2bb495dc81039e3eeb0aa1bb0388bbeac29183'

```

For a shortcut, hand the opening chunk of data straight to the constructor as the positional argument:

```python
>>> from hashlib import blake2b
>>> blake2b(b'Hello world').hexdigest()
'6ff843ba685842aa82031d3f53c48b66326df7639a63d128974c5c14f31a0f33343a8c65551134ed1ae0f2b0dd2bb495dc81039e3eeb0aa1bb0388bbeac29183'

```

Invoke `hash.update()` as often as required to build up the hash piece by piece:

```python
>>> from hashlib import blake2b
>>> items = [b'Hello', b' ', b'world']
>>> h = blake2b()
>>> for item in items:
...     h.update(item)
...
>>> h.hexdigest()
'6ff843ba685842aa82031d3f53c48b66326df7639a63d128974c5c14f31a0f33343a8c65551134ed1ae0f2b0dd2bb495dc81039e3eeb0aa1bb0388bbeac29183'

```

[Subject index](INDEX.md) · [Continue](using-different-digest-sizes.md) · [Owning module, declaration or section: hashlib](hashlib-secure-hashes-and-message-digests.md)
