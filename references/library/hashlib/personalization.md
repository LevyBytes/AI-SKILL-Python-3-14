# hashlib — Personalization

#### Personalization

There are times when it pays to compel a hash function to give back distinct digests for one and the same input across different uses. To quote the authors of the Skein hash function:

>

Our advice is that every application designer give this serious thought; across numerous protocols we have observed that a hash produced in one portion of the protocol becomes reusable in a wholly separate portion whenever two hash computations ran over similar or related data, letting the attacker coerce the application into matching the hash inputs. Personalizing each hash function the protocol employs shuts down this category of attack outright.

([The Skein Hash Function Family](https://www.schneier.com/wp-content/uploads/2016/02/skein.pdf), p. 21)

Hand bytes to the *person* argument and you tailor BLAKE2 to your own use:

```python
>>> from hashlib import blake2b
>>> FILES_HASH_PERSON = b'MyApp Files Hash'
>>> BLOCK_HASH_PERSON = b'MyApp Block Hash'
>>> h = blake2b(digest_size=32, person=FILES_HASH_PERSON)
>>> h.update(b'the same content')
>>> h.hexdigest()
'20d9cd024d4fb086aae819a1432dd2466de12947831b75c5a30cf2676095d3b4'
>>> h = blake2b(digest_size=32, person=BLOCK_HASH_PERSON)
>>> h.update(b'the same content')
>>> h.hexdigest()
'cf68fb5761b9c44e7878bfb2c4c9aea52264a80b75005e65619778de59f383a3'

```

Pairing that personalization with keyed mode is another route to spinning several distinct keys out of one.

```python
>>> from hashlib import blake2s
>>> from base64 import b64decode, b64encode
>>> orig_key = b64decode(b'Rm5EPJai72qcK3RGBpW3vPNfZy5OZothY+kHY6h21KM=')
>>> enc_key = blake2s(key=orig_key, person=b'kEncrypt').digest()
>>> mac_key = blake2s(key=orig_key, person=b'kMAC').digest()
>>> print(b64encode(enc_key).decode('utf-8'))
rbPb15S/Z9t+agffno5wuhB77VbRi6F9Iv2qIxU7WHw=
>>> print(b64encode(mac_key).decode('utf-8'))
G9GtHFE1YluXY1zWPlYk1e/nWfu0WSEb0KRcjhDeP/o=

```

[Subject index](INDEX.md) · [Previous](randomized-hashing.md) · [Owning module, declaration or section: hashlib](hashlib-secure-hashes-and-message-digests.md) · [Continue](tree-mode.md)
