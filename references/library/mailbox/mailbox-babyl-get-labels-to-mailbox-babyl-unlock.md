# mailbox.Babyl: `get_labels()`, `get_file()`, `lock()`, `unlock()`

get_labels()

Return a list giving the names of every user-defined label that the mailbox uses.

Note

To work out which labels exist in the mailbox, the actual messages are examined rather than the list of labels in the Babyl options section, yet the Babyl section gets updated each time the mailbox is modified.

A few `Mailbox` methods that `Babyl` implements warrant particular notes:

 get_file(*key*)

Within Babyl mailboxes, a message's headers aren't kept contiguous with the message's body. To produce a file-like representation, the headers and body get copied together into an [`io.BytesIO`](https://docs.python.org/3.14/library/io.html#io.BytesIO) instance, whose API matches that of a file. Consequently the file-like object is genuinely independent of the underlying mailbox but saves no memory relative to a string representation.

 lock()

 unlock()

Three locking schemes come into play—dot locking plus, where they're available, the `flock()` and `lockf()` system calls.

See also

[Format of Version 5 Babyl Files](https://quimby.gnus.org/notes/BABYL)

A specification of the Babyl format.

[Reading Mail with Rmail](https://www.gnu.org/software/emacs/manual/html_node/emacs/Rmail.html)

The Rmail manual, with some information on Babyl semantics.

[Subject index](INDEX.md) · [Previous](mailbox-babyl-class.md) · [Continue](mailbox-mmdf-class.md) · [Owning module, declaration or section: mailbox](mailbox-manipulate-mailboxes-in-various-formats.md) · [Owning module, declaration or section: mailbox.Babyl](mailbox-babyl-class.md) · [Owning module, declaration or section: `Babyl` objects](mailbox-babyl-class.md)
