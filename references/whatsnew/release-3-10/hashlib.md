# What's New In Python 3.10 / hashlib — hashlib

### hashlib

OpenSSL 1.1.1 or later is now mandatory for the hashlib module. (Contributed by Christian Heimes in [**PEP 644**](https://peps.python.org/pep-0644/) and [bpo-43669](https://bugs.python.org/issue?@action=redirect&bpo=43669).)

Early support for OpenSSL 3.0.0 has landed in the hashlib module. (Contributed by Christian Heimes in [bpo-38820](https://bugs.python.org/issue?@action=redirect&bpo=38820) and other issues.)

For [`pbkdf2_hmac()`](https://docs.python.org/3.14/library/hashlib.html#hashlib.pbkdf2_hmac), the pure-Python fallback is now deprecated. Going forward, PBKDF2-HMAC will be offered only when Python is built with OpenSSL support. (Contributed by Christian Heimes in [bpo-43880](https://bugs.python.org/issue?@action=redirect&bpo=43880).)

[Subject index](INDEX.md) · [Previous source section](glob.md) · [Next source section](hmac.md) · [Release/subject declaration](summary-release-highlights.md)
