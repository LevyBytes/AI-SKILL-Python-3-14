# mailbox: `mailbox.MH`

### `MH` objects

 *class *mailbox.MH(*path*, *factory=None*, *create=True*)

A subclass of `Mailbox` for mailboxes held in MH format. The *factory* parameter is a callable object taking a file-like message representation (one acting as though opened in binary mode) and returning a custom representation. When *factory* is `None`, `MHMessage` serves as the default message representation. When *create* is `True`, the mailbox gets created should it not already exist.

MH is a directory-based mailbox format devised for the MH Message Handling System, a mail user agent. Each message within an MH mailbox lives in its own file. An MH mailbox may hold other MH mailboxes (termed *folders*) on top of messages. Folders may be nested without limit. MH mailboxes additionally support *sequences*, which are named lists serving to logically group messages without shifting them into sub-folders. Sequences are defined in a file named `.mh_sequences` within each folder.

The `MH` class works with MH mailboxes, but it doesn't try to mimic every one of **mh**'s behaviors. In particular, it neither modifies nor is affected by the `context` or `.mh_profile` files that **mh** uses to keep its state and configuration.

`MH` instances carry all the methods of `Mailbox` plus the following:

Changed in version 3.13: Added support for folders lacking a `.mh_sequences` file.

[Subject index](INDEX.md) · [Previous](mailbox-mbox-get-bytes-to-mailbox-mbox-unlock.md) · [Continue](mailbox-mh-list-folders-to-mailbox-mh-pack.md) · [Owning module, declaration or section: mailbox](mailbox-manipulate-mailboxes-in-various-formats.md)
