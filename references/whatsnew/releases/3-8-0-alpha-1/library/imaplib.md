# Python 3.8.0 alpha 1 / library / imaplib

[bpo-18540](https://bugs.python.org/issue?@action=redirect&bpo=18540): The [`imaplib.IMAP4`](https://docs.python.org/3.14/library/imaplib.html#imaplib.IMAP4) and [`imaplib.IMAP4_SSL`](https://docs.python.org/3.14/library/imaplib.html#imaplib.IMAP4_SSL) classes now resolve correctly to the local host IP whenever the default value of the *host* parameter (`''`) is used.

[bpo-33336](https://bugs.python.org/issue?@action=redirect&bpo=33336): `imaplib` now permits the `MOVE` command inside `IMAP4.uid()` (RFC 6851: IMAP MOVE Extension) and possibly as a name for a supported method on an `IMAP4` object.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
