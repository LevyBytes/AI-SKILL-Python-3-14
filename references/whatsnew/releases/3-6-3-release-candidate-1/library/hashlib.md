# Python 3.6.3 release candidate 1 / library / hashlib

[bpo-30102](https://bugs.python.org/issue?@action=redirect&bpo=30102): On OpenSSL < 1.1.0 the ssl and hashlib modules now invoke OPENSSL_add_all_algorithms_noconf(). That function senses CPU features and switches on optimizations for certain CPU architectures, POWER8 among them. The patch grew out of research by Gustavo Serra Scalet.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
