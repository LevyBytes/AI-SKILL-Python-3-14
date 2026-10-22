# Python 3.8.0 alpha 4 / library / decimal

[bpo-36385](https://bugs.python.org/issue?@action=redirect&bpo=36385): IPv4 octets are no longer turned away for looking ambiguously octal. Any leading zeros are simply skipped and are no longer read as marking octal octets. Every octet is read as a decimal value. An octet may still span no more than three digits, leading zeroes included.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
