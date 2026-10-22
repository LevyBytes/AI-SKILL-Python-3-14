# mailbox — Exceptions

### Exceptions

These exception classes are declared within the `mailbox` module:

`*exception *mailbox.Error`

The parent class from which every other module-specific exception descends.

`*exception *mailbox.NoSuchMailboxError`

Thrown when a mailbox was looked for but could not be located — for instance, when you create a `Mailbox` subclass pointing at a path that is absent (with the *create* parameter at `False`), or when you try to open a folder that is not there.

`*exception *mailbox.NotEmptyError`

Thrown when a mailbox holds content though it was supposed to be empty — for instance, when you go to delete a folder that still contains messages.

`*exception *mailbox.ExternalClashError`

Thrown when something outside the program's control, yet bound up with the mailbox, leaves it unable to continue — for instance, when a lock cannot be taken because another program is already holding it, or when a name meant to be unique turns out to already exist on disk.

`*exception *mailbox.FormatError`

Thrown when a file's contents resist parsing — for instance, when an `MH` instance tries to read a damaged `.mh_sequences` file.

[Subject index](INDEX.md) · [Previous](mailbox-mmdfmessage-construction-and-conversion.md) · [Continue](examples.md) · [Owning module, declaration or section: mailbox](mailbox-manipulate-mailboxes-in-various-formats.md)
