# Python 3.9.0 alpha 3 / library / imaplib

[bpo-38615](https://bugs.python.org/issue?@action=redirect&bpo=38615): An optional *timeout* parameter is now accepted by the constructors of [`IMAP4`](https://docs.python.org/3.14/library/imaplib.html#imaplib.IMAP4) and [`IMAP4_SSL`](https://docs.python.org/3.14/library/imaplib.html#imaplib.IMAP4_SSL). Alongside that, the [`open()`](https://docs.python.org/3.14/library/imaplib.html#imaplib.IMAP4.open) method gains an optional *timeout* parameter too. The change was carried into the overridden methods of `IMAP4_SSL` and [`IMAP4_stream`](https://docs.python.org/3.14/library/imaplib.html#imaplib.IMAP4_stream). Donghee Na wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
