# mailbox — mailbox.MMDFMessage construction and conversion

If you build an `MMDFMessage` instance from a `MaildirMessage` instance, a "From " line is produced out of the `MaildirMessage` instance's delivery date, and these conversions happen:

| Resulting state | `MaildirMessage` state |
| --- | --- |
| R flag | S flag |
| O flag | “cur” subdirectory |
| D flag | T flag |
| F flag | F flag |
| A flag | R flag |

If you build an `MMDFMessage` instance from an `MHMessage` instance, these conversions happen:

| Resulting state | `MHMessage` state |
| --- | --- |
| R flag and O flag | no “unseen” sequence |
| O flag | “unseen” sequence |
| F flag | “flagged” sequence |
| A flag | “replied” sequence |

If you build an `MMDFMessage` instance from a `BabylMessage` instance, these conversions happen:

| Resulting state | `BabylMessage` state |
| --- | --- |
| R flag and O flag | no “unseen” label |
| O flag | “unseen” label |
| D flag | “deleted” label |
| A flag | “answered” label |

If you build an `MMDFMessage` instance from an `mboxMessage` instance, the "From " line carries over and every flag lines up one-to-one:

| Resulting state | `mboxMessage` state |
| --- | --- |
| R flag | R flag |
| O flag | O flag |
| D flag | D flag |
| F flag | F flag |
| A flag | A flag |

[Subject index](INDEX.md) · [Continue](mailbox-error-to-mailbox-formaterror.md) · [Owning module, declaration or section: mailbox](mailbox-manipulate-mailboxes-in-various-formats.md) · [Owning module, declaration or section: mailbox.MMDFMessage construction and conversion](mailbox-mmdfmessage-class.md) · [Preceding source contract and version conditions](mmdf-message-origin-and-flags.md)
