# mailbox: `mailbox.mbox`

### `mbox` objects

 *class *mailbox.mbox(*path*, *factory=None*, *create=True*)

A subclass of `Mailbox` for mailboxes held in mbox format. The *factory* parameter is a callable object taking a file-like message representation (one acting as though opened in binary mode) and returning a custom representation. When *factory* is `None`, `mboxMessage` serves as the default message representation. When *create* is `True`, the mailbox gets created should it not already exist.

The mbox format is the time-honored format for keeping mail on Unix systems. Every message within an mbox mailbox is kept in a single file, with each message's start signalled by a line whose first five characters are "From ".

Several variants of the mbox format exist to remedy perceived weaknesses in the original. For the sake of compatibility, `mbox` implements the original format, occasionally called *mboxo*. This means the *Content-Length* header, where present, is disregarded and that any occurrences of "From " at the start of a line within a message body are turned into ">From " when the message is stored, although occurrences of ">From " aren't turned into "From " when the message is read.

A few `Mailbox` methods that `mbox` implements warrant particular notes:

[Subject index](INDEX.md) · [Previous](mailbox-maildir-get-info-to-mailbox-maildir-get-file.md) · [Continue](mailbox-mbox-get-bytes-to-mailbox-mbox-unlock.md) · [Owning module, declaration or section: mailbox](mailbox-manipulate-mailboxes-in-various-formats.md)
