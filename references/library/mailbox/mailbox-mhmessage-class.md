# mailbox: `mailbox.MHMessage`

### `MHMessage` objects

 *class *mailbox.MHMessage(*message=None*)

A message carrying MH-specific behaviors. The *message* parameter carries the same meaning as with the `Message` constructor.

MH messages don't support marks or flags in the conventional sense, yet sequences are supported — these being logical groupings of arbitrary messages. Some mail reading programs (though not the standard **mh** and **nmh**) put sequences to use much as flags get used with other formats, as follows:

| Sequence | Explanation |
| --- | --- |
| unseen | Not read, but previously detected by MUA |
| replied | Replied to |
| flagged | Marked as important |

`MHMessage` instances supply the following methods:

[Subject index](INDEX.md) · [Previous](mbox-message-origin-and-flags.md) · [Continue](mh-message-sequences.md) · [Owning module, declaration or section: mailbox](mailbox-manipulate-mailboxes-in-various-formats.md)
