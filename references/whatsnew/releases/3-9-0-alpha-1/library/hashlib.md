# Python 3.9.0 alpha 1 / library / hashlib

[bpo-9216](https://bugs.python.org/issue?@action=redirect&bpo=9216): The hashlib constructors now accept a usedforsecurity flag to indicate that a hashing algorithm is not being employed in a security context.

[bpo-38132](https://bugs.python.org/issue?@action=redirect&bpo=38132): The OpenSSL hashlib wrapper now adopts a more straightforward implementation. A number of Macros and useless caches were removed. The hash name is now sourced from OpenSSL’s EVP. The algorithm name is unchanged, save that it is now consistently lower case.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
