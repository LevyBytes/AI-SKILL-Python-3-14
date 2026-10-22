# poplib: `poplib.error_proto`

`exception poplib.error_proto`

Thrown whenever this module hits any error (errors coming from the [`socket`](https://docs.python.org/3.14/library/socket.html#module-socket) module are left uncaught). Whatever caused it is handed to the constructor as a string.

See also

Module [`imaplib`](https://docs.python.org/3.14/library/imaplib.html#module-imaplib)

Python’s built-in IMAP module.

[Frequently Asked Questions About Fetchmail](http://www.catb.org/~esr/fetchmail/fetchmail-FAQ.html)

The **fetchmail** POP/IMAP client’s FAQ gathers notes on the ways POP3 servers differ and where they stray from the RFCs — handy reading if you ever build something on top of the POP protocol.

[Subject index](INDEX.md) · [Previous](poplib-pop3-ssl-class.md) · [Continue](pop3-set-debuglevel-to-pop3-utf8.md) · [Owning module, declaration or section: poplib](poplib-pop3-class.md)
