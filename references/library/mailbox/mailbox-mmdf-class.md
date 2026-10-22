# mailbox: `mailbox.MMDF`

### `MMDF` objects

 *class *mailbox.MMDF(*path*, *factory=None*, *create=True*)

A subclass of `Mailbox` for mailboxes held in MMDF format. The *factory* parameter is a callable object that takes a file-like message representation (one acting as though opened in binary mode) and returns a custom representation. When *factory* is `None`, `MMDFMessage` serves as the default message representation. When *create* is `True`, the mailbox gets created should it not already exist.

MMDF is a single-file mailbox format devised for the Multichannel Memorandum Distribution Facility, a mail transfer agent. Each message takes the same shape as an mbox message but is wrapped both before and after by lines carrying four Control-A (`'\001'`) characters. Just as with the mbox format, each message's start is signalled by a line whose first five characters are "From ", but further occurrences of "From " aren't turned into ">From " when messages are stored, since the extra message separator lines keep such occurrences from being mistaken for the starts of later messages.

A few `Mailbox` methods that `MMDF` implements warrant particular notes:

[Subject index](INDEX.md) · [Previous](mailbox-babyl-get-labels-to-mailbox-babyl-unlock.md) · [Continue](mailbox-mmdf-get-bytes-to-mailbox-mmdf-unlock.md) · [Owning module, declaration or section: mailbox](mailbox-manipulate-mailboxes-in-various-formats.md)
