# mailbox: `mailbox.Babyl`

### `Babyl` objects

 *class *mailbox.Babyl(*path*, *factory=None*, *create=True*)

A subclass of `Mailbox` for mailboxes held in Babyl format. The *factory* parameter is a callable object that takes a file-like message representation (one acting as though opened in binary mode) and returns a custom representation. When *factory* is `None`, `BabylMessage` serves as the default message representation. When *create* is `True`, the mailbox gets created should it not already exist.

Babyl is a single-file mailbox format that the Rmail mail user agent bundled with Emacs uses. A message's start is signalled by a line carrying the two characters Control-Underscore (`'\037'`) and Control-L (`'\014'`). A message's end is signalled by the start of the following message or, for the final message, a line carrying a Control-Underscore (`'\037'`) character.

Messages within a Babyl mailbox carry two sets of headers, original headers plus so-called visible headers. Visible headers are usually a subset of the original headers that have been reformatted or trimmed to look nicer. Each message in a Babyl mailbox additionally has an accompanying list of *labels*, that is, short strings recording extra information about the message, and a list of every user-defined label found in the mailbox lives in the Babyl options section.

`Babyl` instances carry all the methods of `Mailbox` plus the following:

[Subject index](INDEX.md) · [Previous](remove-to-close.md) · [Continue](mailbox-babyl-get-labels-to-mailbox-babyl-unlock.md) · [Owning module, declaration or section: mailbox](mailbox-manipulate-mailboxes-in-various-formats.md)
