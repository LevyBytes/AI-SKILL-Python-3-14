# mailbox.MHMessage: `get_sequences()`, `set_sequences()`, `add_sequence()`, `remove_sequence()`

get_sequences()

Return a list of the names of sequences that include this message.

 set_sequences(*sequences*)

Set the list of sequences that include this message.

 add_sequence(*sequence*)

Add *sequence* to the list of sequences that include this message.

 remove_sequence(*sequence*)

Remove *sequence* from the list of sequences that include this message.

When an `MHMessage` instance is built from a `MaildirMessage` instance, these conversions occur:

| Resulting state | `MaildirMessage` state |
| --- | --- |
| “unseen” sequence | no S flag |
| “replied” sequence | R flag |
| “flagged” sequence | F flag |

When an `MHMessage` instance is built from an `mboxMessage` or `MMDFMessage` instance, the *Status* and *X-Status* headers are left off and these conversions occur:

| Resulting state | `mboxMessage` or `MMDFMessage` state |
| --- | --- |
| “unseen” sequence | no R flag |
| “replied” sequence | A flag |
| “flagged” sequence | F flag |

When an `MHMessage` instance is built from a `BabylMessage` instance, these conversions occur:

| Resulting state | `BabylMessage` state |
| --- | --- |
| “unseen” sequence | “unseen” label |
| “replied” sequence | “answered” label |

[Subject index](INDEX.md) · [Previous](mailbox-mhmessage-class.md) · [Continue](mailbox-babylmessage-class.md) · [Owning module, declaration or section: mailbox](mailbox-manipulate-mailboxes-in-various-formats.md) · [Owning module, declaration or section: mailbox.MHMessage](mailbox-mhmessage-class.md) · [Owning module, declaration or section: `MHMessage` objects](mailbox-mhmessage-class.md)
