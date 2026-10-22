# imaplib: `IMAP4.PROTOCOL_VERSION`, `IMAP4.debug`, `IMAP4.utf8_enabled`

IMAP4.PROTOCOL_VERSION

The most recent supported protocol in the `CAPABILITY` response from the server.

 IMAP4.debug

An integer value governing debugging output. Its initial value comes from the module variable `Debug`. Values above three trace every command.

 IMAP4.utf8_enabled

A boolean value that is ordinarily `False`, but flips to `True` once an `enable()` command succeeds for the `UTF8=ACCEPT` capability.

Added in version 3.5.

[Subject index](INDEX.md) · [Previous](imap4-setquota-to-imap4-xatom.md) · [Continue](imap4-example.md) · [Owning module, declaration or section: imaplib](imaplib-imap4-class-to-imap4-readonly.md) · [Owning module, declaration or section: IMAP4 Objects](imap4-append-to-imap4-getquota.md)
