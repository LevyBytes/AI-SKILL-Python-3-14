# Python 3.5.0 beta 3 / core and builtins / text and unicode

[bpo-24467](https://bugs.python.org/issue?@action=redirect&bpo=24467): Corrected a potential buffer over-read in bytearray. A bytearray object now always reserves room for a trailing null byte, so its buffer stays null-terminated at all times.

- Upgrade to Unicode 8.0.0.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
