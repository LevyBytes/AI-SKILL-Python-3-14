# hashlib — Keyed hashing

#### Keyed hashing

Authentication can lean on keyed hashing as a faster, simpler stand-in for the [Hash-based message authentication code](https://en.wikipedia.org/wiki/HMAC) (HMAC). Owing to the indifferentiability property carried over from BLAKE, BLAKE2 may safely run in prefix-MAC mode.

The snippet here demonstrates obtaining a (hex-encoded) 128-bit authentication code for the message `b'message data'` under key `b'pseudorandom key'`:

```python
>>> from hashlib import blake2b
>>> h = blake2b(key=b'pseudorandom key', digest_size=16)
>>> h.update(b'message data')
>>> h.hexdigest()
'3d363ff7401e02026f4a4687d4863ced'

```

For a hands-on case, a web application can symmetrically sign cookies handed to users and afterward verify them to confirm they were not tampered with:

```python
>>> from hashlib import blake2b
>>> from hmac import compare_digest
>>>
>>> SECRET_KEY = b'pseudorandomly generated server secret key'
>>> AUTH_SIZE = 16
>>>
>>> def sign(cookie):
...     h = blake2b(digest_size=AUTH_SIZE, key=SECRET_KEY)
...     h.update(cookie)
...     return h.hexdigest().encode('utf-8')
>>>
>>> def verify(cookie, sig):
...     good_sig = sign(cookie)
...     return compare_digest(good_sig, sig)
>>>
>>> cookie = b'user-alice'
>>> sig = sign(cookie)
>>> print("{0},{1}".format(cookie.decode('utf-8'), sig))
user-alice,b'43b3c982cf697e0c5ab22172d1ca7421'
>>> verify(cookie, sig)
True
>>> verify(b'user-bob', sig)
False
>>> verify(cookie, b'0102030405060708090a0b0c0d0e0f00')
False

```

While a native keyed hashing mode exists, BLAKE2 can naturally also serve inside an HMAC construction with the [`hmac`](https://docs.python.org/3.14/library/hmac.html#module-hmac) module:

```python
>>> import hmac, hashlib
>>> m = hmac.new(b'secret key', digestmod=hashlib.blake2s)
>>> m.update(b'message')
>>> m.hexdigest()
'e3c8102868d28b5ff85fc35dda07329970d1a01e273c37481326fe0c861c8142'

```

[Subject index](INDEX.md) · [Previous](using-different-digest-sizes.md) · [Continue](randomized-hashing.md) · [Owning module, declaration or section: hashlib](hashlib-secure-hashes-and-message-digests.md)
