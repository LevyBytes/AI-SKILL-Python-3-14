# hashlib — Usage

### Usage

To get the digest of the byte string `b"Nobody inspects the spammish repetition"`:

```python
>>> import hashlib
>>> m = hashlib.sha256()
>>> m.update(b"Nobody inspects")
>>> m.update(b" the spammish repetition")
>>> m.digest()
b'\x03\x1e\xdd}Ae\x15\x93\xc5\xfe\\\x00o\xa5u+7\xfd\xdf\xf7\xbcN\x84:\xa6\xaf\x0c\x95\x0fK\x94\x06'
>>> m.hexdigest()
'031edd7d41651593c5fe5c006fa5752b37fddff7bc4e843aa6af0c950f4b9406'

```

In more compact form:

```python
>>> hashlib.sha256(b"Nobody inspects the spammish repetition").hexdigest()
'031edd7d41651593c5fe5c006fa5752b37fddff7bc4e843aa6af0c950f4b9406'

```

[Subject index](INDEX.md) · [Previous](hash-algorithms.md) · [Continue](hashlib-new-to-hashlib-sha3-512.md) · [Owning module, declaration or section: hashlib](hashlib-secure-hashes-and-message-digests.md)
