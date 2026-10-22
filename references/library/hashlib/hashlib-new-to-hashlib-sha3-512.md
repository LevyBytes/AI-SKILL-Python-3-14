# hashlib — Constructors

### Constructors

 hashlib.new(*name*, [*data*, ]***, *usedforsecurity=True*)

Serves as a general-purpose constructor whose first parameter is the string *name* of the algorithm you want. It is also there to reach the hashes listed above plus whatever other algorithms your OpenSSL library happens to supply.

Calling `new()` with an algorithm name:

```python
>>> h = hashlib.new('sha256')
>>> h.update(b"Nobody inspects the spammish repetition")
>>> h.hexdigest()
'031edd7d41651593c5fe5c006fa5752b37fddff7bc4e843aa6af0c950f4b9406'

```

 hashlib.md5([*data*, ]***, *usedforsecurity=True*)

 hashlib.sha1([*data*, ]***, *usedforsecurity=True*)

 hashlib.sha224([*data*, ]***, *usedforsecurity=True*)

 hashlib.sha256([*data*, ]***, *usedforsecurity=True*)

 hashlib.sha384([*data*, ]***, *usedforsecurity=True*)

 hashlib.sha512([*data*, ]***, *usedforsecurity=True*)

 hashlib.sha3_224([*data*, ]***, *usedforsecurity=True*)

 hashlib.sha3_256([*data*, ]***, *usedforsecurity=True*)

 hashlib.sha3_384([*data*, ]***, *usedforsecurity=True*)

 hashlib.sha3_512([*data*, ]***, *usedforsecurity=True*)

Dedicated constructors like the ones above run quicker than feeding an algorithm name into `new()`.

[Subject index](INDEX.md) · [Previous](usage.md) · [Continue](hashlib-algorithms-guaranteed-to-hashlib-algorithms-available.md) · [Owning module, declaration or section: hashlib](hashlib-secure-hashes-and-message-digests.md)
