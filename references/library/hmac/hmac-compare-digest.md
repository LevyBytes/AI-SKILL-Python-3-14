# hmac: `hmac.compare_digest()`

hmac.compare_digest(*a*, *b*)

Return `a == b`. The technique it uses guards against timing analysis by not short-circuiting based on content, which suits it to cryptography. Both *a* and *b* have to share one type: either [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) (ASCII only, such as what `HMAC.hexdigest()` returns), or a [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object).

Note

Should *a* and *b* differ in length, or should an error arise, a timing attack could in principle expose facts about the types and lengths of *a* and *b* — though never their values.

Added in version 3.3.

Changed in version 3.10: Where it can, the function falls back on OpenSSL’s `CRYPTO_memcmp()` under the hood.

See also

Module [`hashlib`](https://docs.python.org/3.14/library/hashlib.html#module-hashlib)

The Python module providing secure hash functions.

[Subject index](INDEX.md) · [Previous](hmac-hmac-class-to-hmac-name.md) · [Continue](../html-entities/html-entities-html5-to-html-entities-codepoint2name.md) · [Owning module, declaration or section: hmac](hmac-new-to-hmac-digest.md)
