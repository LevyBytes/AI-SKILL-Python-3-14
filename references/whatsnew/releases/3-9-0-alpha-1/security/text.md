# Python 3.9.0 alpha 1 / security / text

[bpo-37463](https://bugs.python.org/issue?@action=redirect&bpo=37463): ssl.match_hostname() will no longer take IPv4 addresses bearing extra text after the address, accepting only quad-dotted notation with no trailing whitespace. Certain inet_aton() implementations skip whitespace plus everything following it, for instance "127.0.0.1 whatever".

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
