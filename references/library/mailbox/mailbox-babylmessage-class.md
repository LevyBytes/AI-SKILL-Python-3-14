# mailbox: `mailbox.BabylMessage`

### `BabylMessage` objects

 *class *mailbox.BabylMessage(*message=None*)

A message carrying Babyl-specific behaviors. The *message* parameter carries the same meaning as with the `Message` constructor.

Certain message labels, dubbed *attributes*, are defined by convention to hold special meanings. The attributes run as follows:

| Label | Explanation |
| --- | --- |
| unseen | Not read, but previously detected by MUA |
| deleted | Marked for subsequent deletion |
| filed | Copied to another file or mailbox |
| answered | Replied to |
| forwarded | Forwarded |
| edited | Modified by the user |
| resent | Resent |

By default, Rmail shows only visible headers. The `BabylMessage` class, however, leans on the original headers because they are more complete. Visible headers may be reached explicitly if you wish.

`BabylMessage` instances supply the following methods:

[Subject index](INDEX.md) · [Previous](mh-message-sequences.md) · [Continue](babyl-message-labels-and-visible-headers.md) · [Owning module, declaration or section: mailbox](mailbox-manipulate-mailboxes-in-various-formats.md)
