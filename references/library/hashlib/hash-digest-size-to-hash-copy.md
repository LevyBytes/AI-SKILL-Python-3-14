# hashlib - Hash Objects

### Hash Objects

These values come as constant attributes on the hash objects that the constructors hand back:

 hash.digest_size

How many bytes the resulting hash occupies.

 hash.block_size

How many bytes make up the hash algorithm’s internal block.

A hash object carries these attributes:

 hash.name

This hash’s canonical name, kept lowercase throughout and fit to feed to `new()` for building a further hash of the same kind.

Changed in version 3.4: CPython has carried the name attribute from the very start, yet it went unspecified formally before Python 3.4, so on certain platforms it may be absent.

A hash object offers these methods:

 hash.update(*data*)

Feed the [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) into the hash object. Calling it repeatedly amounts to one call passing every argument concatenated: `m.update(a); m.update(b)` is equivalent to `m.update(a+b)`.

 hash.digest()

Hand back the digest of all the data given to `update()` up to this point. The result is a bytes object of size `digest_size` that may carry any byte value spanning 0 through 255.

 hash.hexdigest()

Behaves like `digest()`, except the digest comes back as a string object twice as long made up solely of hexadecimal digits. That makes it safe to pass around through email or other non-binary channels.

 hash.copy()

Hand back a copy (“clone”) of the hash object. This lets you efficiently derive the digests of data that shares a common opening substring.

[Subject index](INDEX.md) · [Previous](hashlib-algorithms-guaranteed-to-hashlib-algorithms-available.md) · [Continue](hashlib-shake-128-to-shake-hexdigest.md) · [Owning module, declaration or section: hashlib](hashlib-secure-hashes-and-message-digests.md)
