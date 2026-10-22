# mailbox: `mailbox.Maildir`

### `Maildir` objects

 *class *mailbox.Maildir(*dirname*, *factory=None*, *create=True*)

A subclass of `Mailbox` for mailboxes held in Maildir format. The *factory* parameter is a callable object taking a file-like message representation (one acting as though opened in binary mode) and returning a custom representation. When *factory* is `None`, `MaildirMessage` serves as the default message representation. When *create* is `True`, the mailbox gets created should it not already exist.

When *create* is `True` and the *dirname* path exists, it'll be treated as an existing maildir without any attempt to verify its directory layout.

The name *dirname* rather than *path* is due to historical reasons.

Maildir is a directory-based mailbox format devised for the qmail mail transfer agent and by now broadly supported by other programs. Messages within a Maildir mailbox live in separate files inside a shared directory structure. This design lets Maildir mailboxes be reached and altered by several unrelated programs without data corruption, so file locking isn't needed.

Maildir mailboxes hold three subdirectories, specifically: `tmp`, `new`, and `cur`. Messages are created briefly in the `tmp` subdirectory and then shifted into the `new` subdirectory to wrap up delivery. A mail user agent may afterward shift the message into the `cur` subdirectory and stash information about the message's state in a special "info" section tacked onto its file name.

Folders in the style introduced by the Courier mail transfer agent are supported as well. Any subdirectory of the main mailbox counts as a folder when `'.'` leads off its name. `Maildir` represents folder names with the leading `'.'` stripped. A folder is itself a Maildir mailbox, yet it ought not to hold further folders. Rather, logical nesting gets signalled by using `'.'` to separate levels, e.g., "Archived.2005.07".

[Subject index](INDEX.md) · [Previous](mailbox-mailbox-contains-to-mailbox-mailbox-close.md) · [Continue](mailbox-maildir-list-folders-to-mailbox-maildir-remove-flag.md) · [Owning module, declaration or section: mailbox](mailbox-manipulate-mailboxes-in-various-formats.md)
