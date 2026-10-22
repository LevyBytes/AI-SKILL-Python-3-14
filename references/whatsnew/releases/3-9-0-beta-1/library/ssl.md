# Python 3.9.0 beta 1 / library / ssl

[bpo-40515](https://bugs.python.org/issue?@action=redirect&bpo=40515): The [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl) and [`hashlib`](https://docs.python.org/3.14/library/hashlib.html#module-hashlib) modules now positively verify that OpenSSL was built with thread support. Thread support became mandatory in Python 3.7.0, and no-thread builds are no longer safe to use.

[bpo-40457](https://bugs.python.org/issue?@action=redirect&bpo=40457): The ssl module now copes with OpenSSL builds that lack the TLS 1.0 and 1.1 methods.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
