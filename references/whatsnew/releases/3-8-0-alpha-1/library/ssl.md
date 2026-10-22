# Python 3.8.0 alpha 1 / library / ssl

[bpo-24334](https://bugs.python.org/issue?@action=redirect&bpo=24334): The ssl module had its internal implementation details tidied up. The SSLSocket now carries one fewer layer of indirection. The SSLSocket and SSLObject constructor now manage owner and session details. The channel binding implementation was made simpler.

[bpo-33127](https://bugs.python.org/issue?@action=redirect&bpo=33127): The ssl module now builds against LibreSSL 2.7.1.

[bpo-32257](https://bugs.python.org/issue?@action=redirect&bpo=32257): The ssl module now carries the OP_NO_RENEGOTIATION constant, on hand with OpenSSL 1.1.0h or 1.1.1.

[bpo-30622](https://bugs.python.org/issue?@action=redirect&bpo=30622): The ssl module now spots absent NPN support within LibreSSL.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
