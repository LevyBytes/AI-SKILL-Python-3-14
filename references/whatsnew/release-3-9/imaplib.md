# What's New In Python 3.9 / imaplib - imaplib

### imaplib

The constructors of [`IMAP4`](https://docs.python.org/3.14/library/imaplib.html#imaplib.IMAP4) and [`IMAP4_SSL`](https://docs.python.org/3.14/library/imaplib.html#imaplib.IMAP4_SSL) gained an optional *timeout* parameter. Alongside this, the [`open()`](https://docs.python.org/3.14/library/imaplib.html#imaplib.IMAP4.open) method also gained an optional *timeout* parameter. The change was carried through to the overridden methods on `IMAP4_SSL` and [`IMAP4_stream`](https://docs.python.org/3.14/library/imaplib.html#imaplib.IMAP4_stream). (Contributed by Donghee Na in [bpo-38615](https://bugs.python.org/issue?@action=redirect&bpo=38615).)

A new [`imaplib.IMAP4.unselect()`](https://docs.python.org/3.14/library/imaplib.html#imaplib.IMAP4.unselect) method is available. `imaplib.IMAP4.unselect()` releases the server-side resources tied to the selected mailbox and moves the server back to the authenticated state. It carries out the same operations as [`imaplib.IMAP4.close()`](https://docs.python.org/3.14/library/imaplib.html#imaplib.IMAP4.close), with the difference that none of the messages in the mailbox currently selected get permanently deleted. (Contributed by Donghee Na in [bpo-40375](https://bugs.python.org/issue?@action=redirect&bpo=40375).)

[Subject index](INDEX.md) · [Previous source section](idle-and-idlelib.md) · [Next source section](importlib.md) · [Release/subject declaration](summary-release-highlights.md)
