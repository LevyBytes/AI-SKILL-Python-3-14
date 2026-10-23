# ssl - Random generation

### Random generation

 ssl.RAND_bytes(*num*, */*)

Hand back *num* bytes of cryptographically strong pseudo-randomness. An `SSLError` is thrown if the current RAND method doesn't support the operation or if the PRNG hasn't been seeded with sufficient data. To inspect the PRNG's state call `RAND_status()`, and to seed it call `RAND_add()`.

In nearly every application, [`os.urandom()`](https://docs.python.org/3.14/library/os.html#os.urandom) is the better pick.

For what makes a generator cryptographically strong, see the Wikipedia entry [Cryptographically secure pseudorandom number generator (CSPRNG)](https://en.wikipedia.org/wiki/Cryptographically_secure_pseudorandom_number_generator).

Added in version 3.3.

 ssl.RAND_status()

Yield `True` when the SSL pseudo-random number generator already holds ‘enough’ randomness from seeding, and `False` if not. To add to the randomness of that generator, reach for `ssl.RAND_egd()` and `ssl.RAND_add()`.

 ssl.RAND_add(*bytes*, *entropy*, */*)

Feed the supplied *bytes* into the SSL pseudo-random number generator. The *entropy* argument (a float) gives a floor on how much entropy the string holds (so passing `0.0` is always safe). Sources of entropy are covered further in [**RFC 1750**](https://datatracker.ietf.org/doc/html/rfc1750.html).

Changed in version 3.5: Writable [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) is now accepted.

[Subject index](INDEX.md) · [Previous](ssl-sslerror-to-ssl-certificateerror.md) · [Continue](ssl-cert-time-to-seconds-to-ssl-get-default-verify-paths.md) · [Owning module, declaration or section: ssl](ssl-tls-ssl-wrapper-for-socket-objects.md)
