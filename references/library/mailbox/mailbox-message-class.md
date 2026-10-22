# mailbox — `Message` objects

### `Message` objects

 *class *mailbox.Message(*message=None*)

A subclass of the [`email.message`](https://docs.python.org/3.14/library/email.message.html#module-email.message) module's [`Message`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message). Subclasses of `mailbox.Message` layer on mailbox-format-specific state and behavior.

Should *message* be omitted, the new instance comes into being in a default, empty state. Should *message* be an [`email.message.Message`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message) instance, its contents are copied; on top of that, any format-specific information is converted as far as possible should *message* be a `Message` instance. Should *message* be a string, a byte string, or a file, it ought to hold an [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html)-compliant message, which is read in and parsed. Files ought to be open in binary mode, though text mode files are tolerated for backward compatibility.

The format-specific state and behaviors that subclasses supply differ, but as a rule only the properties not tied to a particular mailbox are supported (even though, presumably, the properties are tied to a particular mailbox format). For instance, neither file offsets belonging to single-file mailbox formats nor file names belonging to directory-based mailbox formats are kept, since they pertain only to the original mailbox. But state along the lines of whether a user has read a message or flagged it as important is kept, since it pertains to the message itself.

Nothing requires that `Message` instances be used to represent messages fetched through `Mailbox` instances. In certain situations, the time and memory needed to produce `Message` representations might be unacceptable. For those situations, `Mailbox` instances additionally supply string and file-like representations, and a custom message factory may be given when a `Mailbox` instance is initialized.

[Subject index](INDEX.md) · [Previous](mailbox-mmdf-get-bytes-to-mailbox-mmdf-unlock.md) · [Continue](mailbox-maildirmessage-class.md) · [Owning module, declaration or section: mailbox](mailbox-manipulate-mailboxes-in-various-formats.md)
