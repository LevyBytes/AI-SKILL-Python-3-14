# What's New In Python 3.2 / New, Improved, and Deprecated Modules - email, mailbox

### New, Improved, and Deprecated Modules

Considerable maintenance work and quality upgrades have gone into Python's standard library.

For Python 3.2 the headline change is that the [`email`](https://docs.python.org/3.14/library/email.html#module-email) package, the [`mailbox`](https://docs.python.org/3.14/library/mailbox.html#module-mailbox) module, and the `nntplib` modules now behave properly under the bytes/text model in Python 3. Messages carrying mixed encodings are handled correctly for the very first time.

Across the standard library, encodings together with the text-versus-bytes distinction have received closer scrutiny. Notably, dealings with the operating system can now exchange non-ASCII data more reliably through the Windows MBCS encoding, locale-aware encodings, or UTF-8.

A further notable gain is the inclusion of much stronger support for *SSL* connections along with security certificates.

Furthermore, additional classes now provide a [context manager](https://docs.python.org/3.14/glossary.html#term-context-manager) so that resource clean-up can be done conveniently and dependably through a [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement.

[Subject index](INDEX.md) · [Previous source section](callable-builtin-and-language-changes.md) · [Next source section](email.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)
