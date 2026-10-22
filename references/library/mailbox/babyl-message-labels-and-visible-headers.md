# mailbox.BabylMessage: `get_labels()`, `set_labels()`, `add_label()`, `remove_label()`, `get_visible()`, `set_visible()`, `update_visible()`

get_labels()

Return a list of labels on the message.

 set_labels(*labels*)

Set the list of labels on the message to *labels*.

 add_label(*label*)

Add *label* to the list of labels on the message.

 remove_label(*label*)

Remove *label* from the list of labels on the message.

 get_visible()

Return a `Message` instance carrying the message's visible headers as its headers and carrying an empty body.

 set_visible(*visible*)

Set the message's visible headers to match the headers in *message*. For the *visible* parameter, supply a `Message` instance, an [`email.message.Message`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message) instance, a string, or else a file-like object (one that ought to be open in text mode).

 update_visible()

When a `BabylMessage` instance's original headers are altered, the visible headers aren't automatically altered to match. This method refreshes the visible headers thus: every visible header that has a matching original header takes on the value of that original header, every visible header that lacks a matching original header gets dropped, and whichever of *Date*, *From*, *Reply-To*, *To*, *CC*, and *Subject* show up in the original headers yet not the visible ones get appended onto the visible headers.

When a `BabylMessage` instance is built from a `MaildirMessage` instance, these conversions occur:

| Resulting state | `MaildirMessage` state |
| --- | --- |
| “unseen” label | no S flag |
| “deleted” label | T flag |
| “answered” label | R flag |
| “forwarded” label | P flag |

When a `BabylMessage` instance is built from an `mboxMessage` or `MMDFMessage` instance, the *Status* and *X-Status* headers are left off and these conversions occur:

| Resulting state | `mboxMessage` or `MMDFMessage` state |
| --- | --- |
| “unseen” label | no R flag |
| “deleted” label | D flag |
| “answered” label | A flag |

When a `BabylMessage` instance is built from an `MHMessage` instance, these conversions occur:

| Resulting state | `MHMessage` state |
| --- | --- |
| “unseen” label | “unseen” sequence |
| “answered” label | “replied” sequence |

[Subject index](INDEX.md) · [Previous](mailbox-babylmessage-class.md) · [Continue](mailbox-mmdfmessage-class.md) · [Owning module, declaration or section: mailbox](mailbox-manipulate-mailboxes-in-various-formats.md) · [Owning module, declaration or section: mailbox.BabylMessage](mailbox-babylmessage-class.md) · [Owning module, declaration or section: `BabylMessage` objects](mailbox-babylmessage-class.md)
