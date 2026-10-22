# mailbox: `mailbox.MMDFMessage`

### `MMDFMessage` objects

 *class *mailbox.MMDFMessage(*message=None*)

A message carrying MMDF-specific behaviors. The *message* parameter carries the same meaning as with the `Message` constructor.

As with a message in an mbox mailbox, MMDF messages are kept with the sender's address and the delivery date in an opening line starting with "From ". Likewise, flags signalling the message's state are usually kept in *Status* and *X-Status* headers.

Conventional flags for MMDF messages match those of mbox message and run as follows:

| Flag | Meaning | Explanation |
| --- | --- | --- |
| R | Read | Read |
| O | Old | Previously detected by MUA |
| D | Deleted | Marked for subsequent deletion |
| F | Flagged | Marked as important |
| A | Answered | Replied to |

The "R" and "O" flags reside in the *Status* header, while the "D", "F", and "A" flags reside in the *X-Status* header. The flags and headers usually show up in the order just mentioned.

`MMDFMessage` instances supply the following methods, which match those supplied by `mboxMessage`:

[Subject index](INDEX.md) · [Previous](babyl-message-labels-and-visible-headers.md) · [Continue](mmdf-message-origin-and-flags.md) · [Owning module, declaration or section: mailbox](mailbox-manipulate-mailboxes-in-various-formats.md)
