# Python 3.7.0 beta 2 / library / ssl

[bpo-30622](https://bugs.python.org/issue?@action=redirect&bpo=30622): The ssl module now spots absent NPN support within LibreSSL.

[bpo-24334](https://bugs.python.org/issue?@action=redirect&bpo=24334): The internal workings of the ssl module were tidied up. The SSLSocket carries one fewer layer of indirection. Owner along with session information are now managed by the SSLSocket and SSLObject constructor. The channel binding implementation has been made simpler.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
