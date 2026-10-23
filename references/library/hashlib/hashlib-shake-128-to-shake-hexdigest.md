# hashlib - SHAKE variable length digests

### SHAKE variable length digests

 hashlib.shake_128([*data*, ]***, *usedforsecurity=True*)

 hashlib.shake_256([*data*, ]***, *usedforsecurity=True*)

The `shake_128()` and `shake_256()` algorithms yield variable length digests offering length_in_bits//2 of security, capped at 128 or 256 bits. Because of that, their digest methods need a length supplied. The SHAKE algorithm imposes no ceiling on that length.

 shake.digest(*length*)

Hand back the digest of all the data given to `update()` up to this point. The result is a bytes object of size *length* that may carry any byte value spanning 0 through 255.

 shake.hexdigest(*length*)

Behaves like `digest()`, except the digest comes back as a string object twice as long made up solely of hexadecimal digits. That makes it safe to pass around through email or other non-binary channels.

Example use:

```python
>>> h = hashlib.shake_256(b'Nobody inspects the spammish repetition')
>>> h.hexdigest(20)
'44709d6fcb83d92a76dcb0b668c98e1b1d3dafe7'

```

[Subject index](INDEX.md) · [Previous](hash-digest-size-to-hash-copy.md) · [Continue](hashlib-file-digest.md) · [Owning module, declaration or section: hashlib](hashlib-secure-hashes-and-message-digests.md)
