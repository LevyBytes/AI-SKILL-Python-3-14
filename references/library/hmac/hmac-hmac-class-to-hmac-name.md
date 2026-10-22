# hmac: `hmac.HMAC`, `HMAC.update()`, `HMAC.digest()`, `HMAC.hexdigest()`, `HMAC.copy()`, `HMAC.digest_size`, `HMAC.block_size`, `HMAC.name`

*class *hmac.HMAC

An HMAC object has the following methods:

 HMAC.update(*msg*)

Feed *msg* into the hmac object. Calling this repeatedly amounts to one call over the concatenation of all the arguments: `m.update(a); m.update(b)` comes out the same as `m.update(a + b)`.

Changed in version 3.4: The *msg* parameter now takes whatever type [`hashlib`](https://docs.python.org/3.14/library/hashlib.html#module-hashlib) supports.

 HMAC.digest()

Return the digest of the bytes fed to the `update()` method up to now. The bytes object that comes back matches the *digest_size* of the digest handed to the constructor in length. It may hold non-ASCII bytes, NUL bytes included.

Warning

When you check the result of `digest()` against an externally supplied digest in a verification routine, prefer the `compare_digest()` function over the `==` operator to cut down the exposure to timing attacks.

 HMAC.hexdigest()

Behaves like `digest()`, only the digest comes back as a string of twice the length holding nothing but hexadecimal digits. That makes it convenient for passing the value safely through email or other non-binary channels.

Warning

When you check the result of `hexdigest()` against an externally supplied digest in a verification routine, prefer the `compare_digest()` function over the `==` operator to cut down the exposure to timing attacks.

 HMAC.copy()

Return a copy (“clone”) of the hmac object. This is useful for computing the digests of strings that share a common initial substring efficiently.

A hash object has the following attributes:

 HMAC.digest_size

The size of the resulting HMAC digest in bytes.

 HMAC.block_size

The internal block size of the hash algorithm in bytes.

Added in version 3.4.

 HMAC.name

The canonical name of this HMAC, always lowercase, e.g. `hmac-md5`.

Added in version 3.4.

Changed in version 3.10: Removed the undocumented attributes `HMAC.digest_cons`, `HMAC.inner`, and `HMAC.outer`.

This module also provides the following helper function:

[Subject index](INDEX.md) · [Previous](hmac-new-to-hmac-digest.md) · [Continue](hmac-compare-digest.md) · [Owning module, declaration or section: hmac](hmac-new-to-hmac-digest.md)
