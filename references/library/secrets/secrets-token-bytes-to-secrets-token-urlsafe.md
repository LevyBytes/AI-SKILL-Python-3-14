# secrets — Generating tokens

### Generating tokens

For uses such as password resets, hard-to-guess URLs, and the like, the `secrets` module supplies functions that generate secure tokens.

 secrets.token_bytes(*nbytes=None*)

Return a random byte string containing *nbytes* number of bytes.

If *nbytes* is not specified or `None`, `DEFAULT_ENTROPY` is used instead.

```pycon
>>> token_bytes(16)
b'\xebr\x17D*t\xae\xd4\xe3S\xb6\xe2\xebP1\x8b'

```

 secrets.token_hex(*nbytes=None*)

Return a random text string, in hexadecimal. The string has *nbytes* random bytes, each byte converted to two hex digits.

If *nbytes* is not specified or `None`, `DEFAULT_ENTROPY` is used instead.

```pycon
>>> token_hex(16)
'f9bf78b9a18ce6d46a0cd2b0b86df9da'

```

 secrets.token_urlsafe(*nbytes=None*)

Return a random URL-safe text string, containing *nbytes* random bytes. The text is Base64 encoded, so on average each byte results in approximately 1.3 characters.

If *nbytes* is not specified or `None`, `DEFAULT_ENTROPY` is used instead.

```pycon
>>> token_urlsafe(16)
'Drmhze6EPcv0fN_81Bj-nA'

```

[Subject index](INDEX.md) · [Previous](secrets-systemrandom-class-to-secrets-randbits.md) · [Continue](secrets-default-entropy.md) · [Owning module, declaration or section: secrets](secrets-generate-secure-random-numbers-for-managing-secrets.md)
