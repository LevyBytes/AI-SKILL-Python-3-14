# What’s New In Python 3.5 / imaplib - imaplib

### imaplib

Support for the [context manager](https://docs.python.org/3.14/glossary.html#term-context-manager) protocol is now part of the [`IMAP4`](https://docs.python.org/3.14/library/imaplib.html#imaplib.IMAP4) class. Inside a [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement, the block's end triggers the IMAP4 `LOGOUT` command on its own. (Contributed by Tarek Ziad? and Serhiy Storchaka in [bpo-4972](https://bugs.python.org/issue?@action=redirect&bpo=4972).)

Through the [`IMAP4.enable()`](https://docs.python.org/3.14/library/imaplib.html#imaplib.IMAP4.enable) method, the [`imaplib`](https://docs.python.org/3.14/library/imaplib.html#module-imaplib) module now handles [**RFC 5161**](https://datatracker.ietf.org/doc/html/rfc5161.html) (ENABLE Extension) along with [**RFC 6855**](https://datatracker.ietf.org/doc/html/rfc6855.html) (UTF-8 Support). Whether [**RFC 6855**](https://datatracker.ietf.org/doc/html/rfc6855.html) support has been turned on is reported by a new [`IMAP4.utf8_enabled`](https://docs.python.org/3.14/library/imaplib.html#imaplib.IMAP4.utf8_enabled) attribute. (Contributed by Milan Oberkirch, R. David Murray, and Maciej Szulik in [bpo-21800](https://bugs.python.org/issue?@action=redirect&bpo=21800).)

Following the RFCs' advice, the [`imaplib`](https://docs.python.org/3.14/library/imaplib.html#module-imaplib) module now encodes non-ASCII string usernames and passwords with UTF-8 automatically. (Contributed by Milan Oberkirch in [bpo-21800](https://bugs.python.org/issue?@action=redirect&bpo=21800).)

[Subject index](INDEX.md) · [Previous source section](idlelib-and-idle.md) · [Next source section](imghdr.md) · [Release/subject declaration](summary-release-highlights.md)
