# hashlib — Credits

### Credits

The minds behind [BLAKE2](https://www.blake2.net) were *Jean-Philippe Aumasson*, *Samuel Neves*, *Zooko Wilcox-O’Hearn*, and *Christian Winnerlein*, who built on the [SHA-3](https://en.wikipedia.org/wiki/Secure_Hash_Algorithms) finalist [BLAKE](https://web.archive.org/web/20200918190133/https://131002.net/blake/) — itself the work of *Jean-Philippe Aumasson*, *Luca Henzen*, *Willi Meier*, and *Raphael C.-W. Phan*.

At its heart sits the algorithm from the [ChaCha](https://cr.yp.to/chacha.html) cipher, a design by *Daniel J. Bernstein*.

What ships in the stdlib grows out of the [pyblake2](https://pythonhosted.org/pyblake2/) module, which *Dmitry Chestnykh* authored on top of a C implementation by *Samuel Neves*. The accompanying docs came across from [pyblake2](https://pythonhosted.org/pyblake2/), also penned by *Dmitry Chestnykh*.

Porting some of the C over to Python was the work of *Christian Heimes*.

A public domain dedication, set out below, covers the C hash-function implementation, the extension code, and these docs alike:

>

So far as the law allows, every copyright plus any related or neighboring right the author(s) hold over this software has been placed into the public domain across the whole world. No warranty of any kind accompanies this software as it is handed out.

A copy of the CC0 Public Domain Dedication ought to have reached you together with this software. Should it be missing, look at [https://creativecommons.org/publicdomain/zero/1.0/](https://creativecommons.org/publicdomain/zero/1.0/).

These individuals pitched in on development or released their changes to the project and to the public domain under the Creative Commons Public Domain Dedication 1.0 Universal:

- *Alexandr Sokolovskiy*

See also

Module [`hmac`](https://docs.python.org/3.14/library/hmac.html#module-hmac)

The module that builds message authentication codes out of hashes.

Module [`base64`](https://docs.python.org/3.14/library/base64.html#module-base64)

A further option for encoding binary hashes so they survive non-binary environments.

[https://nvlpubs.nist.gov/nistpubs/fips/nist.fips.180-4.pdf](https://nvlpubs.nist.gov/nistpubs/fips/nist.fips.180-4.pdf)

FIPS 180-4, the publication covering Secure Hash Algorithms.

[https://csrc.nist.gov/pubs/fips/202/final](https://csrc.nist.gov/pubs/fips/202/final)

FIPS 202, the publication that sets out the SHA-3 Standard.

[https://www.blake2.net/](https://www.blake2.net/)

Official BLAKE2 website.

[https://en.wikipedia.org/wiki/Cryptographic_hash_function](https://en.wikipedia.org/wiki/Cryptographic_hash_function)

A Wikipedia entry laying out which algorithms carry known weaknesses and what those weaknesses imply for using them.

[https://www.ietf.org/rfc/rfc8018.txt](https://www.ietf.org/rfc/rfc8018.txt)

PKCS #5: Password-Based Cryptography Specification Version 2.1

[https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-132.pdf](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-132.pdf)

The NIST guidance covering Password-Based Key Derivation.

[Subject index](INDEX.md) · [Previous](tree-mode.md) · [Owning module, declaration or section: hashlib](hashlib-secure-hashes-and-message-digests.md)
