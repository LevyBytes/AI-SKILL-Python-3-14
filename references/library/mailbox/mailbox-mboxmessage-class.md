# mailbox: `mailbox.mboxMessage`

### `mboxMessage` objects

 *class *mailbox.mboxMessage(*message=None*)

A message carrying mbox-specific behaviors. The *message* parameter carries the same meaning as with the `Message` constructor.

Messages within an mbox mailbox are kept together inside a single file. The sender's envelope address and the delivery time are usually kept in a line starting with "From " that serves to mark a message's start, though there's quite a bit of variation in the precise format of this data across mbox implementations. Flags signalling the message's state, such as whether it has been read or marked as important, are usually kept in *Status* and *X-Status* headers.

Conventional flags for mbox messages run as follows:

| Flag | Meaning | Explanation |
| --- | --- | --- |
| R | Read | Read |
| O | Old | Previously detected by MUA |
| D | Deleted | Marked for subsequent deletion |
| F | Flagged | Marked as important |
| A | Answered | Replied to |

The "R" and "O" flags reside in the *Status* header, while the "D", "F", and "A" flags reside in the *X-Status* header. The flags and headers usually show up in the order just mentioned.

`mboxMessage` instances supply the following methods:

[Subject index](INDEX.md) · [Previous](maildir-message-subdirectory-and-metadata.md) · [Continue](mbox-message-origin-and-flags.md) · [Owning module, declaration or section: mailbox](mailbox-manipulate-mailboxes-in-various-formats.md)
