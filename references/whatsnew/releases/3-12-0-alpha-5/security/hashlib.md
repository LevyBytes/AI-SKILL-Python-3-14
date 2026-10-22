# Python 3.12.0 alpha 5 / security / hashlib

[gh-99108](https://github.com/python/cpython/issues/99108): Swap out the builtin [`hashlib`](https://docs.python.org/3.14/library/hashlib.html#module-hashlib) SHA2-224 and SHA2-256 routines, which came from LibTomCrypt, for formally verified and side-channel resistant code drawn from the [HACL*](https://github.com/hacl-star/hacl-star/) project. These builtins still serve only as a fallback whenever OpenSSL lacks them.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
