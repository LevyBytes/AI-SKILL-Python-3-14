# Python 3.12.0 alpha 6 / security / hashlib

[gh-99108](https://github.com/python/cpython/issues/99108): Swap out the builtin hashlib MD5 and SHA1 implementations for verified equivalents drawn from the HACL* project.

[gh-99108](https://github.com/python/cpython/issues/99108): Swap the builtin [`hashlib`](https://docs.python.org/3.14/library/hashlib.html#module-hashlib) SHA2-384 and SHA2-512 implementations, which came from LibTomCrypt, for formally verified, side-channel-resistant code out of the [HACL*](https://github.com/hacl-star/hacl-star/) project. These builtins serve only as a fallback for when OpenSSL has not supplied the algorithms.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
