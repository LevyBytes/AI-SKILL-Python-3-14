# Python 3.7.0 alpha 1 / library / hashlib

[bpo-30102](https://bugs.python.org/issue?@action=redirect&bpo=30102): On OpenSSL < 1.1.0 the ssl and hashlib modules now invoke OPENSSL_add_all_algorithms_noconf(). That call detects CPU features and turns on optimizations for certain CPU architectures such as POWER8. The patch builds on research by Gustavo Serra Scalet.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
